import customtkinter as ctk
from tkinter import messagebox, Tk, Label
import math

class App(Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Calculator")
        self.geometry(f"{455}x{490}+{450}+{100}")
        self.iconbitmap("icons\Calculator_30001.ico")
        self.resizable(False, False)
        
        # frame1 ----------------------------------------------------------------
        self.Frame1 = ctk.CTkFrame(self, width=450, height=450, fg_color="black")
        self.Frame1.grid(row=0, column=0, padx=2, pady=2)
        
        # frame1_1 --------------------------------------------------------------
        self.Frame1_1 = ctk.CTkFrame(self.Frame1, width=440, height=100, fg_color="black")
        self.Frame1_1.grid(row=0, column=0, padx=5, pady=5)
        
        self.lbl_calculator = ctk.CTkLabel(self.Frame1_1, text="Calculator",
                    font=("Arial", 30, "bold"), text_color="white", fg_color="black")
        self.lbl_calculator.pack(padx=2, pady=5)
        
        self.text_box = ctk.CTkEntry(self.Frame1_1, width=430, height=50,
                                     font=("Arial", 20), bg_color="black")
        self.text_box.pack(padx=2, pady=5)
        
        # frame1_2 --------------------------------------------------------------
        self.Frame1_2 = ctk.CTkFrame(self.Frame1, width=440, height=330, fg_color="black")
        self.Frame1_2.grid(row=1, column=0, padx=5, pady=5)
        
        self.add_btn(self.Frame1_2, "clear", "#700725", 0, 0, self.clear)
        self.add_btn(self.Frame1_2, "<=", "#700725", 0, 1, self.back)
        self.add_btn(self.Frame1_2, "(", "#264235", 0, 2,
                     lambda x="(": self.add_text_box(x))
        self.add_btn(self.Frame1_2, ")", "#264235", 0, 3,
                     lambda x=")": self.add_text_box(x))
        
        self.add_btn(self.Frame1_2, "1", "#264235", 1, 0,
                     lambda x="1": self.add_text_box(x))
        self.add_btn(self.Frame1_2, "2", "#264235", 1, 1,
                     lambda x="2": self.add_text_box(x))
        self.add_btn(self.Frame1_2, "3", "#264235", 1, 2,
                     lambda x="3": self.add_text_box(x))
        self.add_btn(self.Frame1_2, "+", "#264235", 1, 3,
                     lambda x="+": self.add_text_box(x))
        
        self.add_btn(self.Frame1_2, "4", "#264235", 2, 0,
                     lambda x="4": self.add_text_box(x))
        self.add_btn(self.Frame1_2, "5", "#264235", 2, 1,
                     lambda x="5": self.add_text_box(x))
        self.add_btn(self.Frame1_2, "6", "#264235", 2, 2,
                     lambda x="6": self.add_text_box(x))
        self.add_btn(self.Frame1_2, "-", "#264235", 2, 3,
                     lambda x="-": self.add_text_box(x))
        
        self.add_btn(self.Frame1_2, "7", "#264235", 3, 0,
                     lambda x="7": self.add_text_box(x))
        self.add_btn(self.Frame1_2, "8", "#264235", 3, 1,
                     lambda x="8": self.add_text_box(x))
        self.add_btn(self.Frame1_2, "9", "#264235", 3, 2,
                     lambda x="9": self.add_text_box(x))
        self.add_btn(self.Frame1_2, "*", "#264235", 3, 3,
                     lambda x="*": self.add_text_box(x))
        
        self.add_btn(self.Frame1_2, ".", "#264235", 4, 0,
                     lambda x=".": self.add_text_box(x))
        self.add_btn(self.Frame1_2, "0", "#264235", 4, 1,
                     lambda x="0": self.add_text_box(x))
        self.add_btn(self.Frame1_2, "=", "#264235", 4, 2,
                     self.result)
        self.add_btn(self.Frame1_2, "/", "#264235", 4, 3,
                     lambda x="/": self.add_text_box(x))
        
        self.add_btn(self.Frame1_2, ",", "#264235", 5, 0,
                     lambda x=",": self.add_text_box(x))
        self.add_btn(self.Frame1_2, "Scientific", "#3648a3", 5, 1,
                     self.open_calc2)
        
    def add_btn(self, master, text, color, row, column, command):
        self.btn = ctk.CTkButton(master=master, text=text,
                font=("Arial", 20, "bold"), width=100,
                height=50, fg_color=color, command=command)
        self.btn.grid(row=row, column=column, padx=5, pady=5)
    
    def clear(self):
        self.text_box.delete(0, ctk.END)
        self.text_box.focus_set()
    
    def back(self):
        text = self.text_box.get()[:-1]
        self.clear()
        self.text_box.insert(0, text)
    
    def add_text_box(self, x):
        if x in ["1", "2", "3", "+", "4", "5", "6", "-", "7", "8", "9", "*", "0", "/", ".", ")", "(", ","]:
            text = self.text_box.get()
            text += x
            self.clear()
            self.text_box.insert(0, text)
    
    def result(self):
        try:
            text = self.text_box.get().lstrip("0")
            self.clear()
            self.text_box.insert(0, eval(text))
        except:
            messagebox.showerror("Error", "اعداد وارد شده درست نیست")
    
    def open_calc2(self):
        self.geometry(f"{970}x{490}+{220}+{100}")
        self.Frame2 = ctk.CTkFrame(self, width=450, height=480, fg_color="black")
        self.Frame2.grid(row=0, column=1, padx=2, pady=2)
        # frame2_1 --------------------------------------------------------------
        self.Frame2_1 = ctk.CTkFrame(self.Frame2, width=440, height=100, fg_color="black")
        self.Frame2_1.grid(row=0, column=0, padx=5, pady=5)
        
        self.lbl_Scientific = ctk.CTkLabel(self.Frame2_1, text="Scientific",
                        font=("Arial", 50, "bold"), text_color="white", fg_color="black")
        self.lbl_Scientific.pack(padx=2, pady=5, ipadx=105, ipady=39)
        
        # frame2_2 --------------------------------------------------------------
        self.Frame2_2 = ctk.CTkFrame(self.Frame2, width=440, height=330, fg_color="black")
        self.Frame2_2.grid(row=1, column=0, padx=5, pady=5)
        
        self.add_btn(self.Frame2_2, "sqrt", "#264235", 0, 0,
                    lambda x="sqrt": self.result2(x))
        self.add_btn(self.Frame2_2, "ceil", "#264235", 0, 1,
                    lambda x="ceil": self.result2(x))
        self.add_btn(self.Frame2_2, "floor", "#264235", 0, 2,
                    lambda x="floor": self.result2(x))
        self.add_btn(self.Frame2_2, "pow", "#264235", 0, 3,
                    lambda x="pow": self.result2(x))
        
        self.add_btn(self.Frame2_2, "exp", "#264235", 1, 0,
                    lambda x="exp": self.result2(x))
        self.add_btn(self.Frame2_2, "log", "#264235", 1, 1,
                    lambda x="log": self.result2(x))
        self.add_btn(self.Frame2_2, "sin", "#264235", 1, 2,
                    lambda x="sin": self.result2(x))
        self.add_btn(self.Frame2_2, "cos", "#264235", 1, 3,
                    lambda x="cos": self.result2(x))
        
        self.add_btn(self.Frame2_2, "tan", "#264235", 2, 0,
                    lambda x="tan": self.result2(x))
        self.add_btn(self.Frame2_2, "radians", "#264235", 2, 1,
                    lambda x="radians": self.result2(x))
        self.add_btn(self.Frame2_2, "degrees", "#264235", 2, 2,
                    lambda x="degrees": self.result2(x))
        self.add_btn(self.Frame2_2, "factorial", "#264235", 2, 3,
                    lambda x="factorial": self.result2(x))
        
        self.add_btn(self.Frame2_2, "gcd", "#264235", 3, 0,
                    lambda x="gcd": self.result2(x))
        self.add_btn(self.Frame2_2, "isqrt", "#264235", 3, 1,
                    lambda x="isqrt": self.result2(x))
        self.add_btn(self.Frame2_2, "pi", "#264235", 3, 2,
                    lambda x="pi": self.result2(x))
        self.add_btn(self.Frame2_2, "e", "#264235", 3, 3,
                    lambda x="e": self.result2(x))

        # frame2_3 --------------------------------------------------------------
        self.Frame2_3 = ctk.CTkFrame(self.Frame2, width=440, height=50, fg_color="black")
        self.Frame2_3.grid(row=2, column=0, padx=5, pady=5)
        
        self.btn_close = ctk.CTkButton(self.Frame2_3, text="Close Page",
                    font=("Arial", 30, "bold"), width=430, height=60,
                    fg_color="#700725", command=self.close)
        self.btn_close.pack(padx=5, pady=5)
        # frame2_3 --------------------------------------------------------------
        self.Frame3 = ctk.CTkFrame(self, width=50, height=480, fg_color="black")
        self.Frame3.grid(row=0, column=2, padx=2, pady=2)
        
        self.btn_help = ctk.CTkButton(self.Frame3, text="H\nE\nL\nP",
                    font=("Arial", 30, "bold"), width=45, height=475,
                    fg_color="#306785", command=self.help_)
        self.btn_help.pack(padx=5, pady=5)
        
    def help_(self):
        self.Frame2.grid_forget()
        self.Frame3.grid_forget()
        self.Frame4 = ctk.CTkFrame(self, width=450, height=480, fg_color="black")
        self.Frame4.grid(row=0, column=1, padx=2, pady=2)
        
        self.lbl = ctk.CTkLabel(self.Frame4, text="Scientific Help", text_color="white", font=("B nazanin", 30, "bold"))
        self.lbl.place(x=120, y=5)
        
        self.lbl = ctk.CTkLabel(self.Frame4, text="(tan and sqrt)=> input: enter a number select button",
                                text_color="white", font=("Arial", 19))
        self.lbl.place(x=5, y=55)
        
        self.lbl = ctk.CTkLabel(self.Frame4, text="(ceil)=> input: enter a float number select button",
                                text_color="white", font=("Arial", 19))
        self.lbl.place(x=5, y=85)
        
        self.lbl = ctk.CTkLabel(self.Frame4, text="(floor)=> input: enter a float number select button",
                                text_color="white", font=("Arial", 19))
        self.lbl.place(x=5, y=115)
        
        self.lbl = ctk.CTkLabel(self.Frame4, text="(pow)=> input: enter 4,6 select button",
                                text_color="white", font=("Arial", 19))
        self.lbl.place(x=5, y=145)
        
        self.lbl = ctk.CTkLabel(self.Frame4, text="(exp)=> input: enter a number select button",
                                text_color="white", font=("Arial", 19))
        self.lbl.place(x=5, y=175)
        
        self.lbl = ctk.CTkLabel(self.Frame4, text="(log)=> input: enter 2.5,5 select button",
                                text_color="white", font=("Arial", 19))
        self.lbl.place(x=5, y=205)
        
        self.lbl = ctk.CTkLabel(self.Frame4, text="(sin)=> input: enter a float number select button",
                                text_color="white", font=("Arial", 19))
        self.lbl.place(x=5, y=235)
        
        self.lbl = ctk.CTkLabel(self.Frame4, text="(cos)=> input: enter a float number select button",
                                text_color="white", font=("Arial", 19))
        self.lbl.place(x=5, y=265)
        
        self.lbl = ctk.CTkLabel(self.Frame4, text="(radians)=> input: enter a number select button",
                                text_color="white", font=("Arial", 19))
        self.lbl.place(x=5, y=295)
        
        self.lbl = ctk.CTkLabel(self.Frame4, text="(degrees)=> input: enter a float number select button",
                                text_color="white", font=("Arial", 19))
        self.lbl.place(x=5, y=325)
        
        self.lbl = ctk.CTkLabel(self.Frame4, text="(factorial)=> input: enter a number select button",
                                text_color="white", font=("Arial", 19))
        self.lbl.place(x=5, y=355)
        
        self.lbl = ctk.CTkLabel(self.Frame4, text="(gcd)=> input: enter 2,3 select button",
                                text_color="white", font=("Arial", 19))
        self.lbl.place(x=5, y=385)
        
        self.lbl = ctk.CTkLabel(self.Frame4, text="(isqrt)=> input: enter a number select button",
                                text_color="white", font=("Arial", 19))
        self.lbl.place(x=5, y=415)
        
        self.lbl = ctk.CTkLabel(self.Frame4, text="(pi and e)=> input: select button",
                                text_color="white", font=("Arial", 19))
        self.lbl.place(x=5, y=445)
        
        self.Frame5 = ctk.CTkFrame(self, width=50, height=480, fg_color="black")
        self.Frame5.grid(row=0, column=2, padx=2, pady=2)
        
        self.btn_back = ctk.CTkButton(self.Frame5, text="B\nA\nC\nK",
                    font=("Arial", 30, "bold"), width=45, height=475,
                    fg_color="#a34a12", command=self.open_calc2)
        self.btn_back.pack(padx=5, pady=5)
        
    
    def close(self):
        self.Frame2.grid_forget()
        self.geometry(f"{455}x{490}+{450}+{100}")
    
    def result2(self, x):
        number = self.text_box.get()
        self.clear()
        if x == "sqrt":
            text = math.sqrt(int(number))
            self.text_box.insert(0, text)
        elif x == "ceil":
            text = math.ceil(float(number))
            self.text_box.insert(0, text)
        elif x == "floor":
            text = math.floor(float(number))
            self.text_box.insert(0, text)
        elif x == "pow":
            if "," in number:
                number = number.split(",")
                text = math.pow(int(number[0]), int(number[1]))
                self.text_box.insert(0, text)
            else:
                messagebox.showerror("Error", "لطفا ورودی را به شکل زیر وارد کنید\n2,5")
        elif x == "exp":
            text = math.exp(int(number))
            self.text_box.insert(0, text)
        elif x == "log":
            if "," in number:
                number = number.split(",")
                text = math.log(float(number[0]), float(number[1]))
                self.text_box.insert(0, text)
            else:
                messagebox.showerror("Error", "لطفا ورودی را به شکل زیر وارد کنید\n2,5")
        elif x == "sin":
            text = math.sin(float(number))
            self.text_box.insert(0, text)
        elif x == "cos":
            text = math.cos(float(number))
            self.text_box.insert(0, text)
        elif x == "tan":
            text = math.tan(int(number))
            self.text_box.insert(0, text)
        elif x == "radians":
            text = math.radians(int(number))
            self.text_box.insert(0, text)
        elif x == "degrees":
            text = math.degrees(float(number))
            self.text_box.insert(0, text)
        elif x == "factorial":
            text = math.factorial(int(number))
            self.text_box.insert(0, text)
        elif x == "gcd":
            if "," in number:
                number = number.split(",")
                text = math.gcd(int(number[0]), int(number[1]))
                self.text_box.insert(0, text)
            else:
                messagebox.showerror("Error", "لطفا ورودی را به شکل زیر وارد کنید\n2,5")
        elif x == "isqrt":
            if number.isdigit():
                text = math.isqrt(int(number))
                self.text_box.insert(0, text)
            else:
                messagebox.showerror("Error", "لطفا عدد صحیح وارد کنید")
        elif x == "pi":
            text = math.pi
            self.text_box.insert(0, text)
        elif x == "e":
            text = math.e
            self.text_box.insert(0, text)

def main():
    obg = App()
    obg.mainloop()

if __name__ == "__main__":
    main()