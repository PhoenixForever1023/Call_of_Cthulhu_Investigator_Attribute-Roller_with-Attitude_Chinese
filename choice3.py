import tkinter as tk
import random 
from resource import skill_dict, comment_sentence
from tkinter import messagebox  

class Choice3:
    def __init__(self, parent_window, investigator_name, back_callback):
        self.parent = parent_window
        self.investigator_name = investigator_name
        self.back_callback = back_callback
        self.choice3_main()

    def choice3_main(self):
        self.clear_parent()
        self.main_frame = tk.Frame(self.parent)
        self.main_frame.pack(fill = "both", expand = True)

        notice = tk.Label(self.main_frame, text = f"{self.investigator_name}, 来体验一下刺激的龟——速生成吧！\n这次就来(被迫)投这个吧：", 
                          font = ("华文细黑", 12))
        notice.pack()

        skill_frame = tk.Frame(self.main_frame)
        skill_frame.pack(pady=20)

        self.skill = tk.StringVar()
        show_random_skill = tk.Label(skill_frame, text = self.skill, width = 5, bg = "Yellow", font = ("Times New Roman", 20),
                                    textvariable=self.skill)
        show_random_skill.pack(side = "left", padx = 10)

        self.skill_value = tk.StringVar()
        show_random_skill_value = tk.Label(skill_frame, text=self.skill_value, width = 5, bg = "Yellow", font = ("Times New Roman", 20),
                                           textvariable= self.skill_value)
        show_random_skill_value.pack(side = "left", padx = 10)

        available_skill = [key for key, value in skill_dict.items() if value == 0]
        if available_skill:
            self.random_skill = random.choice(available_skill)
            self.skill.set(self.random_skill)
        else:
            messagebox.showwarning("开发者怒了！","技能已满！骰子过劳！")
            self.remaining_clicks = 0
            self.back_to_main()
            return

        self.temp_dice = 0    
        self.skill_value.set(self.temp_dice)

        roll = tk.Button(self.main_frame, text = "点击此处开始投掷！", font = ("华文细黑", 12),
                         command= self.roll_skill_value)
        roll.pack(pady=10)
        self.remaining_clicks = 3

        back_frame = tk.Frame(self.main_frame)
        back_frame.pack(pady=20)

        re_set = tk.Button(back_frame, text="这个技能投完了？\n那就下一个！",
                           command = self.re_set_skill)
        re_set.pack(side = "left", padx=10)

        back_btn = tk.Button(back_frame,
                    text="觉得这个方式太慢了？\n随时可以切换！",
                    command=self.back_to_main)
        back_btn.pack(side = "left", padx=10)

    def roll_skill_value(self):
        if self.remaining_clicks<= 0:
            messagebox.showwarning("开发者怒了！","再加下去要变成神话生物了！")
            return
        
        self.remaining_clicks -= 1
        dice = random.randint(1,6)
        messagebox.showinfo(f"{self.investigator_name}的命运正在转动", f"生了！是 {dice} ！")
        self.temp_dice += dice*5
        self.skill_value.set(self.temp_dice)

        if self.remaining_clicks == 0:
            skill_dict[self.random_skill] = self.temp_dice
            comment = tk.StringVar()
            comment_share = tk.Label(self.main_frame, text=comment, font = ("华文细黑", 15),
                                           textvariable= comment)
            comment_share.pack(pady=10)

            if self.temp_dice <= 40:
                comment.set(comment_sentence[0])
            elif 40< self.temp_dice<=65:
                comment.set(comment_sentence[1])
            else:
                comment.set(comment_sentence[2])
    
    def re_set_skill(self):
        if self.remaining_clicks>0:
            messagebox.showwarning("开发者怒了！","骰子可都在等着你呢！")
            return
        self.clear_parent()
        self.choice3_main()

    def back_to_main(self):
        if 3>self.remaining_clicks>0:
            messagebox.showwarning("开发者怒了！","骰子可都在等着你呢！")
            return
        self.clear_parent()
        self.back_callback()
    
    def clear_parent(self):
        for widget in self.parent.winfo_children():
            widget.destroy()
