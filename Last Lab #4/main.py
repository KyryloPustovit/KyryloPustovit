#Import
from tkinter import *
from func import graphic,Tablitsa,save_Exel,save_txt

#Вікно з кнопками
root = Tk()
root.geometry("210x160")
root.resizable(False, False)
root.configure(bg = "#7F7E7E")


#Кнопка "Графік"
btn1 = Button(root)
btn1.configure(bg = '#5A5959', fg = 'white', text = 'Графік', command=graphic)
btn1.place(x = 35, y = 20, width=150, height=30)

#Кнопка "Таблиця"
btn2 = Button(root)
btn2.configure(bg='#5A5959', fg='white', text='Таблиця', command=Tablitsa)
btn2.place(x = 35, y = 50, width=150, height=30)

#Кнобка "Зберегти таблицю в Exel"
btn3 = Button(root)
btn3.configure(bg = '#5A5959', fg = 'white', text = 'Зберегти таблицю в Exel', command = save_Exel)
btn3.place(x = 35, y = 80, width = 150, height = 30)

#Кнопка "Зберегти в .txt"
btn4 = Button(root)
btn4.configure(bg = '#5A5959', fg = 'white', text = 'Зберегти таблицю в .txt', command = save_txt)
btn4.place(x = 35, y = 110, width = 150, height = 30)

root.mainloop()