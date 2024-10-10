import tkinter as tk

# list1 = []
#
#
# def addcoffee():
#     list1.append("coffee")
#     print(list1.count("coffee"))
#     addText()
#
#
# def addText():
#     txt.delete("1.0", tk.END)
#
#     txt.insert(tk.END, list1.count("coffee"))
#
#
# window = tk.Tk()
# window.columnconfigure((0,1), weight=1, minsize=75)
# window.rowconfigure((0,1), weight=1, minsize=50)
#
# frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=5)
#
# frame.grid(row=0, column=1)
# btn1 = tk.Button(master=frame,text="Coffee", command=addcoffee)
# btn1.pack()
#
# frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=5)
# frame.grid(row=1, column=1)
# btn2 = tk.Button(master=frame, text="Tea")
# btn2.pack()
#
# frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=5)
# frame.grid(row=0, column=0, rowspan=2)
# txt = tk.Text(master=frame)
# txt.pack()


# ***************************************************************************************************************

window = tk.Tk()

window.geometry("500x500")

frame = tk.Frame(master=window, width=250, height=250, bg="red", borderwidth=2)
label = tk.Label(master=frame, text="h"*10, bg="blue")

frame.place(x=125, y=125)
label.pack()

tk.mainloop()
