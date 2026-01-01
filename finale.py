import tkinter as tk
import sys
from tkinter import messagebox  

class Finale:
    def __init__(self, parent_window, investigator_name, result_list):
        self.parent = parent_window
        self.investigator_name = investigator_name
        self.result_list = result_list
        self.final_result = {}
        self.finale_main()
        

    def finale_main(self):
        self.clear_parent()
        self.main_frame = tk.Frame(self.parent)
        self.main_frame.pack(fill = "both", expand = True)

        show_welcome = tk.Label(self.main_frame, 
                                text = f"请查收{self.investigator_name}的天命五！\n选一个最合适的吧!\n", 
                                font = ("华文细黑", 12))
        show_welcome.pack()

        self.result_tianmingwu = tk.StringVar()
        r1 = tk.Radiobutton(self.main_frame, text = "第一个！", variable=self.result_tianmingwu, 
                            value = 1, font = ("华文细黑", 12), command=self.get_print_selection)
        r1.pack()
        r2 = tk.Radiobutton(self.main_frame, text = "第二个！", variable=self.result_tianmingwu, 
                            value = 2, font = ("华文细黑", 12), command=self.get_print_selection)
        r2.pack()
        r3 = tk.Radiobutton(self.main_frame, text = "第三个！", variable=self.result_tianmingwu, 
                            value = 3, font = ("华文细黑", 12), command=self.get_print_selection)
        r3.pack()
        r4 = tk.Radiobutton(self.main_frame, text = "第四个！", variable=self.result_tianmingwu, 
                            value = 4, font = ("华文细黑", 12), command=self.get_print_selection)
        r4.pack()
        r5 = tk.Radiobutton(self.main_frame, text = "第五个！", variable=self.result_tianmingwu, 
                            value =5, font = ("华文细黑", 12), command=self.get_print_selection)
        r5.pack()

        confirm = tk.Button(self.main_frame, text="确定好了\n就选这个！", font = ("华文细黑", 12),command = self.end)
        confirm.pack(side="bottom", pady=(0, 30))

    def get_print_selection(self):
        index = int(self.result_tianmingwu.get()) - 1
        self.final_result = self.result_list[index]
        self.print_selection()
    
    def print_selection(self):
        print_information = "\n".join([f"{key}:   {value}" for key, value in self.final_result.items()])
        total = sum(self.final_result.values())

        if not hasattr(self, 'info_label')  or not self.info_label.winfo_exists():
            self.info_label = tk.Label(self.main_frame, text="", font=("华文细黑", 12))
            self.info_label.pack()
        
        self.info_label.config(text=f"\n\n{print_information}\n total:   {total} (不含运)")
        

    def end(self):
        response = messagebox.askyesno(f"{self.investigator_name}的命运从此掷下", 
                                  f"想好了噢！\n一旦确认就无法更改了！")
        if response:
            self.clear_parent()
            self.main_frame = tk.Frame(self.parent)
            self.main_frame.pack(fill="both", expand=True)

            show_thankyou = tk.Label(self.main_frame, 
                                text = f"最后版本的天命五！\n\n你已经是个合格的调查员，\n可以直面阿撒托斯了！\n\n{self.investigator_name}的八维表格：", 
                                font = ("华文细黑", 12))
            show_thankyou.pack()
            self.print_selection()
            byebye = tk.Button(self.main_frame,
                               text="退出在此！！！\n祝你调查一路顺风！", font=("华文细黑", 10), 
                               command = lambda: sys.exit(0))
            byebye.pack(pady = 25)

        else: 
            return

        
    def clear_parent(self):
        for widget in self.parent.winfo_children():
            widget.destroy()