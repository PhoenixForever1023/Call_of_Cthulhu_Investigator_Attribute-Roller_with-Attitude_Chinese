import tkinter as tk
from choice2 import Choice2 as c2
from choice3 import Choice3 as c3
from finale import Finale
from tkinter import messagebox 
from resource import skill_dict
import random
import copy

class COCGenerater:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("调查员天命五暴躁生成器")
        self.root.geometry("600x500")
        self.shared_data = {"Investigator Name": ""}
        self.result_list = []
        self.round = 5
        self.create_start_page()


    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()


    def create_start_page(self):
        self.clear_window()
        assistant_title = tk.Label(self.root, text = "恭喜你！一个新的调查员牛马即将诞生！", font=("华文细黑", 12), width = 30, 
                           height = 2)
        assistant_title.pack(pady = 10)

        enter_reminder = tk.Label(self.root, text = "请输入调查员的姓名:", font = ("华文细黑", 10), width = 20,
                          height = 2)
        enter_reminder.pack()

        self.invesigator_name =tk.Entry(self.root, font = ("华文细黑", 10), width = 20 )
        self.invesigator_name.pack()

        start = tk.Button(self.root, text = "点击被骰子概率学暴揍",font = ("华文细黑", 10), width = 20, 
                  height = 2, command = self.get_user_input)
        start.pack(pady = 20)


    def get_user_input(self):
        name = self.invesigator_name.get()

        if not name.strip():
            messagebox.showwarning("开发者怒了！","你的调查员是叫'佚名'吗?")
        else:
            self.shared_data["Investigator Name"] = name
            self.show_success_message()
    

    def show_success_message(self):
        self.clear_window()
        success_label = tk.Label(self.root, text = f"{self.shared_data['Investigator Name']} 从蛋里蹦出来了！\n三种天命五模式供你选择:",
                                 font = ("华文细黑", 12))
        success_label.pack(pady = 10)

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady = 10)

        choice1 = tk.Button(button_frame, text = "极速生成！", font = ("华文细黑", 11), command=lambda: self.go_choice(1))
        choice1.pack(side = "left", padx = 10)

        choice2 = tk.Button(button_frame, text = "分步生成！", font = ("华文细黑", 11), command=lambda: self.go_choice(2))
        choice2.pack(side = "left", padx = 10)

        choice3 = tk.Button(button_frame, text = "刺激生成！", font = ("华文细黑", 11), command=lambda: self.go_choice(3))
        choice3.pack(side = "left", padx = 10)

        self.show_message()
        reset_frame = tk.Frame(self.root)
        reset_frame.pack(pady = 20)
        reset_skill = tk.Button(reset_frame, text = "这次投完了？\n速速下一次！", width = 10, command = self.reset_tianmingwu)
        reset_skill.pack(side = "left",padx=10)
        back_btn = tk.Button(reset_frame, text = "名字不够帅？\n返回在此", width = 10, command = self.create_start_page)
        back_btn.pack(side = "left",padx = 10)


    def show_message(self):
        print_information  = "\n".join([f"{key}:   {value}" for key, value in skill_dict.items()])
        total = 0
        for key in skill_dict:
            total += skill_dict[key]
        information = tk.Label(self.root, text = f"{self.shared_data['Investigator Name']}现在长这样：\n\n{print_information}\n total:   {total} (不含运)", font = ("华文细黑", 12))
        information.pack()


    def go_choice(self, choice):
        self.shared_data["Mode"] = choice
        if choice == 1:
            self.choice1()
        elif choice == 2:
            self.choice2_instance = c2(
            self.root, 
            self.shared_data["Investigator Name"],
            lambda: self.show_success_message()
            )
        elif choice == 3:
            self.choice3_instance = c3(
            self.root, 
            self.shared_data["Investigator Name"],
            lambda: self.show_success_message()
            )


    def choice1(self):
        finish = 0
        for skill in skill_dict:
            if skill_dict[skill] != 0:
                finish += 1
        if finish == 8:                           
            messagebox.showwarning("开发者怒了！", "这是天命五, 不是刷分!")
            self.already_generated = True
            return
        if hasattr(self, "already_generated") and self.already_generated:
            messagebox.showwarning("开发者怒了！", "这是天命五, 不是刷分!")
        else:
            for ski in skill_dict:
                if skill_dict[ski] == 0:
                    dice1 = random.randint(1,6)
                    dice2 = random.randint(1,6)
                    dice3 = random.randint(1,6)
                    final_value = (dice1 + dice2 + dice3)*5
                    skill_dict[ski] = final_value
            self.already_generated = True
            self.show_success_message()
            messagebox.showinfo("一键出分就是爽快!",f"骰子已经把{self.shared_data['Investigator Name']}的命运告诉了我……" )


    def reset_tianmingwu(self):
        current_result = copy.deepcopy(skill_dict) 
        self.result_list.append(current_result)
        
        for skill in skill_dict:
            if skill_dict[skill] == 0:
                messagebox.showwarning("开发者怒了！", "投都没投完，赶着去见奈亚吗!")
                self.result_list.pop()
                return
            else:
                skill_dict[skill] = 0
        if hasattr(self, 'already_generated'):
            self.already_generated = False
        self.round -= 1
        if self.round != 0:
            messagebox.showinfo(f"{self.shared_data['Investigator Name']}再度踏上轮回……", f"还剩{self.round}次，能找到心仪的答案吗？")
            self.clear_window()
            self.show_success_message()
        else:
            messagebox.showinfo(f"{self.shared_data['Investigator Name']}再度踏上轮回……", "这是……最后的答案了……")
            self.finale_instance = Finale(
            self.root, 
            self.shared_data["Investigator Name"],
            self.result_list
            )
        

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = COCGenerater()
    app.run()


        
            