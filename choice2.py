import tkinter as tk
import random 
from resource import skill_dict
from tkinter import messagebox  

class Choice2:
    def __init__(self, parent_window, investigator_name, back_callback):
        self.parent = parent_window
        self.investigator_name = investigator_name
        self.back_callback = back_callback
        self.choice2_main()
    

    def choice2_main(self):
        self.clear_parent()
        self.main_frame = tk.Frame(self.parent)
        self.main_frame.pack(fill = "both", expand = True)
    
        self.skill = tk.StringVar()
        self.value = tk.StringVar()
        skill_showcase_1 = tk.Label(self.main_frame, bg = "yellow",width = 30, font=("微软雅黑", 12),
                                textvariable = self.skill)
        skill_showcase_1.pack()
        skill_showcase_2 = tk.Label(self.main_frame, bg = "yellow",width = 5, font=("微软雅黑", 20),
                                textvariable = self.value)
        skill_showcase_2.pack()

        assistant_title = tk.Label(self.main_frame, text = "请选择要投掷的值:", font=("微软雅黑", 12), width = 30, 
                                height = 2)
        assistant_title.pack()

        start = tk.Button(self.main_frame, text = "别愣着，快确认！", width = 20, 
                    height = 2, command=self.get_input)
        start.pack(pady = 10)
        skill_name = tk.StringVar()
        self.skill_name_showcase =tk.Listbox(self.main_frame, listvariable=skill_name, font=("微软雅黑", 12))
        index = 0
        for ski in skill_dict:
            self.skill_name_showcase.insert("end", ski)
            if skill_dict[ski] > 0:
                self.skill_name_showcase.itemconfig(index, {"fg": "gray"})
            else:
                self.skill_name_showcase.itemconfig(index, {"fg": "black"}) 
            index += 1
        self.skill_name_showcase.pack()

        back_btn = tk.Button(self.main_frame,
                    text="觉得这个方式太无聊？\n换一种！",
                    command=self.back_callback)
        back_btn.pack(pady=10)


    def get_input(self):
        selection = self.skill_name_showcase.curselection()
        if not selection:
            messagebox.showwarning("开发者怒了！", "你是想给空气数值吗？")
            return
        
        index = selection[0]
        value = self.skill_name_showcase.get(selection[0])

        if skill_dict[value] > 0:
            messagebox.showwarning("开发者怒了！", "这是天命五, 不是刷分!")
            return

        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        dice3 = random.randint(1,6)
        final_value = (dice1 + dice2 + dice3)*5
        self.skill.set(f"{value} = 3D6*5 = ({dice1} + {dice2} + {dice3})*5 =")
        self.value.set(final_value)
        skill_dict[value] = final_value
        self.skill_name_showcase.itemconfig(index, {"fg": "gray"})
            
    
    def clear_parent(self):
        for widget in self.parent.winfo_children():
            widget.destroy()
