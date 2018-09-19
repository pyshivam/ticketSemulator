from tkinter import *
from tkinter import Button


class project():
    Button=0
    def __init__(self, master, a):
        self.root = master
        self.e = a
        root.title("Ticket Simulator")
        root.geometry('300x300')
        films = {"Race": [12, 25, 200],
                 "Ant-Man": [16, 25, 300],
                 "Deadpool": [18, 18, 180],
                 "Infinity-War": [12, 29, 400],
                 "Stranger Things 3": [3, 10, 350],
                 "Game of thorns": [18, 10, 350],
                 }

        label = Label(root, text="MOVIES AVAILABEL")
        label.pack()
        # spinbox1=Spinbox(root,from_=5,to=10,state=NORMAL).pack()

        check1 =Button(root, text="Race 3").grid(row=0,column=0)
        check2 =Button(root, text="Antman the worse").grid(row=1,column=0)

        check3 =Button(root, text="Deadpool 2").grid(row=2,column=0)

        check4 =Button(root, text="Infinity-War").grid(row=3,column=0)
        check5 =Button(root, text="Stranger things").grid(row=4,column=0)
        check6 =Button(root, text="Game of thorns").grid(row=5,column=0)


root = Tk()
project(root, 0)
root.mainloop()
