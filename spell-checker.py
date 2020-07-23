from textblob import TextBlob

from tkinter import * 
def check():
    ori = var1.get()
    b = TextBlob(ori)
    var2.set(b.correct())

root=Tk()
root.title('Spelling checker')
root.geometry('400x200')
Label(root,text='Spell Checker', font='Arial 20 bold').pack()
# origi = Label(root,text='')
var1 = StringVar()
Entry(root, textvariable=var1, font='arial 12').pack()
Button(root,text='check', relief=SUNKEN, command=check).pack()
var2 = StringVar()
Entry(root, textvariable=var2, font='arial 12').pack()
root.mainloop()
