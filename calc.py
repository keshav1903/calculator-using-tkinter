from tkinter import *
import tkinter.messagebox as tmsg

def click(event):
    global scvalue
    txt = event.widget.cget('text')
    if txt == '=':
        if scvalue.get().isdigit():
            val = int(scvalue.get())
        else:
            try:
                val = eval(screen.get())
            except Exception as e:
                tmsg.showinfo('ERROR', 'Please Enter Valid Values')
                val = ''
        scvalue.set(val)
        screen.update()
    elif txt == 'C':
        scvalue.set('')
        screen.update()
    else:
        scvalue.set(scvalue.get()+txt)
        screen.update()

        
root = Tk()
root.geometry('270x500')
root.maxsize(270, 500)
root.minsize(270, 500)
root.title('CALCULATOR')
root.wm_iconbitmap('C:/Users/hp/PycharmProjects/GUI/calculator/calc.ico')
root.config(bg='#F9A200')

scvalue = StringVar()
scvalue.set('')
screen = Entry(root, textvariable=scvalue, font='lucida 40 bold', relief=SUNKEN, borderwidth=10, bg='#FCCC92')
screen.pack(fill=X, ipadx=8, pady= 10, padx=10)

f1 = Frame(root, bg='#DBFF71')
b = Button(f1, text='0', font='lucida 20 bold', relief=RIDGE, borderwidth=10, bg='#FFFF71')
b.pack(fill=X)
b.bind('<Button-1>', click)
f1.pack(side=BOTTOM, fill=X)

f1 = Frame(root, bg='#DBFF71')
b = Button(f1, text='7',  font='lucida 20 bold', relief=SUNKEN, borderwidth=10, bg='#FFFF71')
b.pack(side=LEFT, padx=5, pady=5)
b.bind('<Button-1>', click)
b = Button(f1, text='8',  font='lucida 20 bold', relief=SUNKEN, borderwidth=10, bg='#FFFF71')
b.pack(side=LEFT, padx=5, pady=5)
b.bind('<Button-1>', click)
b = Button(f1, text='9',  font='lucida 20 bold', relief=SUNKEN, borderwidth=10, bg='#FFFF71')
b.pack(side=LEFT, padx=5, pady=5)
b.bind('<Button-1>', click)
b = Button(f1, text='*',  font='lucida 20 bold', relief=SUNKEN, borderwidth=10, bg='#00D5EC')
b.pack(side=TOP, padx=7, pady=5)
b.bind('<Button-1>', click)
f1.pack(side=BOTTOM)

f1 = Frame(root, bg='#DBFF71')
b = Button(f1, text='4',  font='lucida 20 bold', relief=SUNKEN, borderwidth=10, bg='#FFFF71')
b.pack(side=LEFT, padx=5, pady=5)
b.bind('<Button-1>', click)
b = Button(f1, text='5',  font='lucida 20 bold', relief=SUNKEN, borderwidth=10, bg='#FFFF71')
b.pack(side=LEFT, padx=5, pady=5)
b.bind('<Button-1>', click)
b = Button(f1, text='6',  font='lucida 20 bold', relief=SUNKEN, borderwidth=10, bg='#FFFF71')
b.pack(side=LEFT, padx=5, pady=5)
b.bind('<Button-1>', click)
b = Button(f1, text='-',  font='lucida 20 bold', relief=SUNKEN, borderwidth=10, bg='#00D5EC')
b.pack(side=TOP, padx=8, pady=5)
b.bind('<Button-1>', click)
f1.pack(side=BOTTOM)

f1 = Frame(root, bg='#DBFF71')
b = Button(f1, text='1',  font='lucida 20 bold', relief=SUNKEN, borderwidth=10, bg='#FFFF71')
b.pack(side=LEFT, padx=5, pady=5)
b.bind('<Button-1>', click)
b = Button(f1, text='2',  font='lucida 20 bold', relief=SUNKEN, borderwidth=10, bg='#FFFF71')
b.pack(side=LEFT, padx=5, pady=5)
b.bind('<Button-1>', click)
b = Button(f1, text='3',  font='lucida 20 bold', relief=SUNKEN, borderwidth=10, bg='#FFFF71')
b.pack(side=LEFT, padx=5, pady=5)
b.bind('<Button-1>', click)
b = Button(f1, text='+',  font='lucida 20 bold', relief=SUNKEN, borderwidth=10, bg='#00D5EC')
b.pack(side=LEFT, padx=5, pady=5)
b.bind('<Button-1>', click)
f1.pack(side=BOTTOM)



f1 = Frame(root, bg='#DBFF71')
b = Button(f1, text='C',  font='lucida 20 bold', relief=SUNKEN, borderwidth=10, bg='#EC0000')
b.pack(side=LEFT, padx=5, pady=5)
b.bind('<Button-1>', click)
b = Button(f1, text='/',  font='lucida 20 bold', relief=SUNKEN, borderwidth=10, bg='#00D5EC')
b.pack(side=LEFT, padx=5, pady=5)
b.bind('<Button-1>', click)
b = Button(f1, text='%',  font='lucida 20 bold', relief=SUNKEN, borderwidth=10, bg='#00D5EC')
b.pack(side=LEFT, padx=5, pady=5)
b.bind('<Button-1>', click)
b = Button(f1, text='=',  font='lucida 20 bold', relief=SUNKEN, borderwidth=10, bg='#00D5EC')
b.pack(side=LEFT, padx=1, pady=5)
b.bind('<Button-1>', click)
f1.pack(side=BOTTOM)



root.mainloop()