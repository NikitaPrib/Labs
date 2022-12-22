# import tkinter
'''1 задание'''
# # Вызывается в момент нажатия на кнопку:
# def click():
# # Получаем строковое содержимое поля ввода с помощью метода get()
# # C помощью config() можем изменить отображаемый текст
#     converter.set('{:.2f}'.format((5/9*(float(entry.get())-32))))
# window = tkinter.Tk()
# frame = tkinter.Frame(window)
# frame.pack()
# # Модель: создаем объект класса IntVar
# converter = tkinter.IntVar()
# # Обнуляем созданный объект с помощью метода set()
# #converter.set(0)
# entry = tkinter.Entry(frame)
# entry.pack()
# label = tkinter.Label(frame, textvariable=converter)
# label.pack()
# # Привязываем обработчик нажатия на кнопку к функции click()
# button = tkinter.Button(frame, text='CONVERT', command=click)
# button.pack()
# window.mainloop()
'''2 задание'''
# import tkinter
# import random
# from tkinter import messagebox
# import os
# import sys
#
# d = {'машина': 'car', 'вертолет': 'helicopter', 'самолет': 'plane', 'автобус': 'bus', 'поезд': 'train'}
# window = tkinter.Tk()
# window.geometry('300x200')
# window.title('Dictionary')
# lbl1 = tkinter.Label(window, text='Write the English word for:', font=("Arial Bold", 15))
# lbl2 = tkinter.Label(window)
# lbl3 = tkinter.Label(window)
# lbl4 = tkinter.Label(window)
#
#
# # функция выбора случайного слова из словаря
# def random_word():
#     word = random.choice(list(d.keys()))
#     lbl2.configure(text=word)
#     lbl3.configure(text='')
#     return word
#
#
# random_word()
#
# lbl1.pack()
# lbl2.pack()
# txt = tkinter.Entry(window, width=10)
# txt.focus()
# txt.pack()
# lbl3.pack()
# lbl4.pack()
#
#
# # функция рестарта программы
# def restart_program():
#     python = sys.executable
#     os.execl(python, python, *sys.argv)
#
#
# # функция проверки ввода
# def click():
#     a = txt.get()
#     if d[lbl2.cget('text')] == a:
#         result = 'You are right.'
#     else:
#         result = 'You are wrong.'
#         click.invocations -= 1
#         lbl4.configure(text=f'Attempts left: {click.invocations}.')
#         if click.invocations == 0:
#             result = 'You lost.'
#             msg = messagebox.showinfo(title="You lost!", message="The game will restart.")
#             if msg == 'ok':
#                 restart_program()  # при трех ошибках возникает сообщение о том, Вы проиграли и что игра начнется заново.
#     lbl3.configure(text=result)
#
#
# click.invocations = 3  # обратный счетчик ошибок
#
# btn1 = tkinter.Button(window, text="Check", command=click)
# btn1.pack()
# btn2 = tkinter.Button(window, text="Next", command=random_word)
# btn2.pack()
# window.mainloop()
'''3 задание'''
# import tkinter as tk
# from tkinter.filedialog import asksaveasfilename
#
#
# def save_file():
#     filepath = asksaveasfilename(
#         defaultextension="txt",
#         filetypes=[("Текстовые файлы", "*.txt"), ("HTML файлы", "*.html")]
#     )
#     if not filepath:
#         return
#     with open(filepath, "w", encoding="UTF-8") as output_file:
#         text = txt_edit.get("1.0", tk.END)
#         output_file.write(text)
#     window.title(f"Work with - {filepath}")
#
#
# window = tk.Tk()
# window.title("Save text")
#
# window.rowconfigure(0, minsize=50, weight=1)
# window.columnconfigure(1, minsize=50, weight=1)
#
# txt_edit = tk.Text(window)
# fr_buttons = tk.Frame(window)
# btn_save = tk.Button(fr_buttons, text="Save file", command=save_file)
#
# btn_save.grid(row=0, column=0, padx=5, pady=5)
#
# fr_buttons.grid(row=0, column=0, sticky="ne")
# txt_edit.grid(row=0, column=1)
#
# window.mainloop()
'''5 задание'''
# from tkinter import *
# from tkinter import messagebox
#
# from math import pi
#
# result = .0
#
#
# def clear():
#     edit.delete(0, last=END)
#
#
# def calc():
#     global result
#     try:
#         r = float(radius.get())
#         result = 4 / 3 * pi * r ** 3
#         messagebox.showinfo("Объем сферы", "{:.4f}".format(result))
#     except ValueError:
#         messagebox.showerror("Косяк, батенька!", "Некорректный ввод!")
#
#
# def save_txt():
#     if result:
#         with open("out.txt", 'w') as f:
#             f.write('Объем сферы с радиусом {} равен {}'.format(radius.get(), str(result)))
#         messagebox.showinfo("Объем сферы", "Сохранено в файл 'out.txt'")
#     else:
#         messagebox.showwarning("Косяк, батенька!", "Нечего сохранять!")
#
#
# def save_html():
#     if result:
#         s = """ <!DOCTYPE html> <html lang="en"> <head> <meta charset="UTF-8"> <title>Tkinter</title>
#         </head> <body> <h2> Объем сферы с радиусом {} равен {}
#          </h2> </body> </html> """.format(radius.get(), str(result))
#
#         with open("output.html", 'w') as f:
#             f.write(s)
#         messagebox.showinfo("Объем сферы", "Сохранено в файл 'output.html'")
#     else:
#         messagebox.showwarning("Косяк, батенька!", "Нечего сохранять!")
#
#
# root = Tk()
# root.title('Sphere')
# root.resizable(False, False)
# radius = StringVar()
#
# Label(root, text='Radius:').grid(row=0, column=0, sticky=E, padx=10, pady=10)
#
# edit = Entry(root, width=10, text='0', textvariable=radius)
# edit.grid(row=0, column=1, padx=10, pady=10)
#
# btn_calc = Button(root, text='Calculate', command=calc)
# btn_calc.grid(row=0, column=2, padx=10, pady=10)
#
# btn_save_txt = Button(root, text='Save to txt', command=save_txt)
# btn_clear = Button(root, text='Clear', command=clear)
# btn_save_htm = Button(root, text='Save to html', command=save_html)
#
# btn_save_txt.grid(row=2, column=0, padx=10, pady=10)
# btn_clear.grid(row=2, column=1, padx=10, pady=10)
# btn_save_htm.grid(row=2, column=2, padx=10, pady=10)
#
# root.mainloop()
