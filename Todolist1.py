import tkinter 
import random

from tkinter import *
from tkinter import messagebox

root=  tkinter.Tk()

root.configure(bg= "white")
root.title("My own App")
root.geometry("325x275")

tasks = []
tasks =["dsa roadmap", "proper plan", "reminder for dec test series", "b", "c"]

def update_task():
    clr_listbox()
    for task in tasks:
        lb_tasks.insert("end",task)

def clr_listbox():
    lb_tasks.delete(0,"end")
def add_task():
    task = txt_input.get()
    if tasks!="":
        tasks.append(task)
        update_task()
    else:
        messagebox.showwarning("Warning", "You need to enter a task first")
        lbl_display["text"] = "please enter a task."
    txt_input.delete(0,"end")    
    pass

def del_all():
    confirmed  = messagebox.askyesno("please Confirm","Do you really want to delete all tasks?")
    if confirmed == True:
        global tasks
        tasks = []
        update_task()
    pass

def del_one():
    task = lb_tasks.get("active")
    if task in tasks:
        tasks.remove(task)
    update_task()
    
    pass

def sort_asc():
    tasks.sort()
    update_task()
    pass

def sort_desc():
    tasks.sort()
    tasks.reverse()
    update_task()
    pass

def choose_random():
    task = random.choice(tasks)
    lbl_display["text"] = task
    lbl_display["task"] = task
    pass

def no_of_tasks():
    number_of_tasks = len(tasks)
    msg  ="Numebr of taks: %s" %number_of_tasks
    lbl_display["text"] = msg
    
    pass


lbl_title = tkinter.Label(root, text = "To-Do-List", bg = "white")
lbl_title.grid(row=0,column=0)


lbl_display = tkinter.Label(root, text = "", bg = "white")
lbl_display.grid(row=0,column=1)


txt_input = tkinter.Entry(root, width = 30)
txt_input.grid(row=1,column=1)

btn_add_task = tkinter.Button(root,text = "Add task", fg = "#464646", bg = "white", command= add_task)

btn_add_task.grid(row=1,column=0)



btn_del_all = tkinter.Button(root,text = "Delete All", fg = "#464646", bg = "white", command= del_all)

btn_del_all.grid(row=2,column=0)


btn_del_one = tkinter.Button(root,text = "Delete ", fg = "#464646", bg = "white", command= del_one)

btn_del_one.grid(row=3,column=0)
5
btn_sort_asc = tkinter.Button(root,text = "Sort-Asc", fg = "#464646", bg = "white", command= sort_asc)

btn_sort_asc.grid(row=4,column=0)


btn_sort_desc = tkinter.Button(root,text = "Sort Desc", fg ="#464646", bg = "white", command= sort_desc)

btn_sort_desc.grid(row=5,column=0)


btn_choose_random = tkinter.Button(root,text = "Choose Random", fg = "#464646", bg = "white", command= choose_random)

btn_choose_random.grid(row=6,column=0)


btn_no_of_tasks = tkinter.Button(root,text = "Number of Task", fg = "#464646", bg = "white", command= no_of_tasks)

btn_no_of_tasks.grid(row=7,column=0)

btn_exit = tkinter.Button(root,text = "Exit", fg = "red", bg = "#464646", command= exit)

btn_exit.grid(row=8,column=0)

lb_tasks = tkinter.Listbox(root)
lb_tasks.grid(row=2,column=1,rowspan  =7)

