from textblob import TextBlob

from tkinter import * 
def check():
    ori = var1.get()
    b = TextBlob(ori)
    correct = b.correct()
    if var1.get() == correct and var1.get() != '':
        stavar.set(f'Already correct word')
    elif var1.get() == '':
        stavar.set('Enter a word to chrck')
    else: 
        stavar.set(f'Correct word')
    var2.set(correct)

root=Tk()
root.title('Spelling checker')
root.geometry('400x240')
root.configure(background='beige')
Label(root,text='Spell Checker', font='Arial 20 bold').pack(pady=8)
var1 = StringVar()
stavar = StringVar()
stavar.set('')
Entry(root, textvariable=var1, font='arial 12').pack(pady=5)
Button(root,text='check', relief=SUNKEN, command=check, bg='green yellow').pack(pady=5)
var2 = StringVar()
Entry(root, textvariable=var2, font='arial 12').pack(pady=5)
sta = Entry(root,textvariable=stavar, bg='beige')
sta.pack()
frm=Frame(root, bg='gray')
Label(frm, text='By Prabal Gupta', bg='gray').pack(anchor='e',side=RIGHT)
Label(frm, text='©bystrSC.0.2.').pack(anchor='w',side=LEFT)
frm.pack(side=BOTTOM, fill=X)
root.mainloop()
