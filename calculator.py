import tkinter as tk

root=tk.Tk()

root.title("Calculator")
root.geometry("320x420")
root.configure(bg="#121314")
root.resizable(False,False)

entry=tk.Entry(root,font=("Segoe UI",24),bd=0,bg="#2d2d2d",fg="white",justify="right")
entry.place(x=10,y=10,width=300,height=60)

btn_style={
    "font":("Segoe UI",12),
    "bd":0,
    "fg":"white",
    "activeforeground":"white"
}
BTN_W=70
BTN_H=50
def create_btn(text,x,y,cmd,bg):
    tk.Button(
        root,
        text=text,
        command=cmd,
        bg=bg,
        activebackground=bg,
        **btn_style
    ).place(x=x,y=y,width=BTN_W,height=BTN_H)

def click(x):
    entry.insert(tk.END,x)

def equal():
    result=eval(entry.get())
    entry.delete(0,tk.END)
    entry.insert(tk.END,result)

def clear():
    entry.delete(0,tk.END)

def backspace():
    entry.delete(len(entry.get())-1)

button=[("C",0,0,clear,"#ff5c5c"),
        ("<-",1,0,backspace,"#ff5c5c"),
        ("/",2,0,lambda:click("/"),"#3a3a3a"),
        ("*",3,0,lambda:click("*"),"#3a3a3a"),

        ("7",0,1,lambda:click("7"),"#2d2d2d"),
        ("8",1,1,lambda:click("8"),"#2d2d2d"),
        ("9",2,1,lambda:click("9"),"#2d2d2d"),           
        ("-",3,1,lambda:click("-"),"#2d2d2d"),
         
        ("4",0,2,lambda:click("4"),"#2d2d2d"),
        ("5",1,2,lambda:click("5"),"#2d2d2d"),
        ("6",2,2,lambda:click("6"),"#2d2d2d"),
        ("+",3,2,lambda:click("+"),"#2d2d2d"),
       
        ("1",0,3,lambda:click("1"),"#2d2d2d"),
        ("2",1,3,lambda:click("2"),"#2d2d2d"),
        ("3",2,3,lambda:click("3"),"#2d2d2d"),
        ("=",3,3,equal,"#2d2d2d"),
        
        ("0",0,4,lambda:click("0"),"#2d2d2d"),
        (".",1,4,lambda:click("."),"#2d2d2d")
        
        ]

start_x=10
start_y=80

gap_x=75
gap_y=60

for(text,column,row,command,color) in button:
    x=start_x+column*gap_x
    y=start_y+row*gap_y
    create_btn(text,x,y,command,color)

root.mainloop()