import tkinter as tk
import random

def generate_number():
    num = random.randint(100, 999)
    label_num.config(text=str(num))

root = tk.Tk()
root.title("Lucky Draw")
root.geometry("250x150")

label_title = tk.Label(root, text="เลขที่ออก", font=("Tahoma", 10))
label_title.grid(row=0, column=0, padx=50, pady=10)

label_num = tk.Label(root, text="???", font=("Arial", 30, "bold"), fg="red")
label_num.grid(row=1, column=0)

btn = tk.Button(root, text="สุ่มเลข", command=generate_number)
btn.grid(row=2, column=0, pady=10)
root.mainloop()
