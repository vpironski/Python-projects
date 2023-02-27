from re import X
import tkinter as tk
from tkinter import *
from tkinter.font import BOLD
from turtle import back
from xml.dom.pulldom import END_DOCUMENT


def logic(window,ent_credit,cost1):
    change = float(cost1-ent_credit)
    if change >= 0:
        neshto = tk.Label(window, text = f'Change: {change}')
        neshto.place(x = 950, y =300)

def latte():
    cost1 = 2
    window = tk.Tk()
    window.geometry('1920x1080')
    window.title('Coffee machine')
    lbl1= tk.Label(window, text = 'Your chosen drink is: LATTE')
    lbl1.configure(font=("Bernard MT", 13, 'bold'))
    lbl1.place(x = 950, y = 50)

    cost = tk.Label(window, text = f'Cost: {cost1:.2f} credit')
    cost.place(x = 950, y = 70)

    credit_lbl = tk.Label(window, text = 'Enter a credit:')
    credit_lbl.place(x=950, y=125)


  
  
  
    # ent_credit = float(credit.get())
    # credit.config(text=f"{ent_credit}": {})
    # credit1 = float(ent_credit.get())
    # ent_credit.config(text = f"change: {change:}")
    # ent_credit = float(tk.Entry(window))
    # ent_credit.place(x=950, y=150)

    # enter = tk.Button(window, text = 'Enter',command = logic(window,ent_credit,cost1))
    # enter.place(x=950,y = 200)


    
def espresso():
    cost1 = 0,5
    window = tk.Tk()
    window.geometry('1920x1080')
    window.title('Coffee machine')
    lbl1= tk.Label(window, text = 'Your chosen drink is: ESPRESSO')
    lbl1.configure(font=("Bernard MT", 13, 'bold'))
    lbl1.place(x = 950, y = 50)

    cost = tk.Label(window, text = f'Cost: {cost1:.2f} credit')
    cost.place(x = 950, y = 70)
    
def mochaccino():
    cost1 = 1,5
    window = tk.Tk()
    window.geometry('1920x1080')
    window.title('Coffee machine')
    lbl1= tk.Label(window, text = 'Your chosen drink is: MOCHACCINO)')
    lbl1.configure(font=("Bernard MT", 13, 'bold'))
    lbl1.place(x = 950, y = 50)

    cost = tk.Label(window, text = f'Cost: {cost1:.2f} credit')
    cost.place(x = 950, y = 70)
    cost = 20
    
def cappuccino():
    cost1 = 1
    window = tk.Tk()
    window.geometry('1920x1080')
    window.title('Coffee machine')

    lbl1= tk.Label(window, text = 'Your chosen drink is: CAPPUCCINO')
    lbl1.configure(font=("Bernard MT", 13, 'bold'))
    lbl1.place(x = 950, y = 50)

    cost = tk.Label(window, text = f'Cost: {cost1:.2f} credit')
    cost.place(x = 950, y = 70)
    
    clear_btn = tk.Button(window, text='Go back', bg="red", fg='white', command=window.destroy)
    clear_btn.place(x = 950, y = 500)

def play():
    
    window = tk.Tk()
    window.geometry('1920x1080')
    window.title('Coffee machine')

    lbl1 = tk.Label(window, text='Choose a coffee!')
    lbl1.configure(font=("Bernard MT", 30, 'bold'))
    lbl1.place(x = 250, y = 30)
    
    coffee1_btn = tk.Button(window, text='Latte', bg="#604CDE",
    fg='black', command=latte)
    coffee1_btn.place(x = 220, y = 150)
    coffee1_btn.config(height = 5, width = 15)

    coffee2_btn = tk.Button(window, text='Espresso', bg="#604CDE",
    fg='black', command=espresso)
    coffee2_btn.place(x = 470, y = 150)
    coffee2_btn.config(height = 5, width = 15)

    coffee3_btn = tk.Button(window, text='Mochaccino', bg="#604CDE",
    fg='black', command=mochaccino)
    coffee3_btn.place(x = 220, y = 270)
    coffee3_btn.config(height = 5, width = 15)

    coffee4_btn = tk.Button(window, text='Cappuccino', bg="#604CDE",
    fg='black', command=cappuccino)
    coffee4_btn.place(x =470, y = 270)
    coffee4_btn.config(height = 5, width = 15)

    window.mainloop()

play()