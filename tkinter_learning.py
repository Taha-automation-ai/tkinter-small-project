# imports 
import tkinter as tk

root = tk.Tk()
root.title("Click Counter")
root.geometry("300x200")

count = 0

def click_count():
    global count
    count = count + 1
    lbl_result.config(text=f"Button was clicked {count} times!")


lbl_result = tk.Label(root, text="Button was clicked 0 times!", font=("Arial", 11))
lbl_result.pack(pady=15)


btn = tk.Button(root, text="Click Me!", command=click_count)
btn.pack(pady=10)


root.mainloop()
