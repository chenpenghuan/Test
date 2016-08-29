from tkinter import *
master=Tk()
text=Text(master,width=30,height=10)
text.insert(INSERT,"你是傻逼\n")
text.pack()
def say():
    text.insert(INSERT,"你是傻逼\n")
    pass
lb=Button(text,text='我想说',command=say)
text.window_create(INSERT,window=lb)
'''
sb=Scrollbar(master)
sb.pack(side=RIGHT,fill=Y)
lb=Listbox(master,selectmod=EXTENDED,height=5,yscrollcommand=sb.set)
lb.pack()
list1=['驴','马','骡子','猪','牛','羊']
def delet():
    lb.delete(ACTIVE)
for anim in list1:
    lb.insert(END,anim)
sb.config(command=lb.yview)
bt=Button(master ,text='删除它',command=delet)
bt.pack()
'''
mainloop()
