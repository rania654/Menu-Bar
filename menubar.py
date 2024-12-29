from tkinter import *
import tkinter as tk
from tkinter import Menu
root = Tk()

root.geometry("500x500")
root.title("A simple menu bar")
menubar=Menu(root)
root.config(menu=menubar)

filemenu = Menu(menubar)
filemenu.add_command(label= "new",command = lambda:print("New file") )
filemenu.add_command(label= "open",command = lambda:print("Open file"))
filemenu.add_command(label= "save",command = lambda:print("Save file"))
filemenu.add_separator()
filemenu.add_command(label= "exit",command = root.quit)
menubar.add_cascade(label="File",menu = filemenu)

editmenu = Menu(menubar)
editmenu.add_command(label= "cut",command = lambda:print("You have pressed cut"))
editmenu.add_command(label= "copy",command = lambda:print("You have pressed copy"))
editmenu.add_command(label= "paste",command = lambda:print("You have pressed paste"))
editmenu.add_separator()
editmenu.add_command(label= "undo",command = lambda:print("You have pressed undo"))
editmenu.add_command(label= "redo",command = lambda:print("You have pressed redo"))
menubar.add_cascade(label="Edit",menu = editmenu)

selectionmenu = Menu(menubar)
selectionmenu.add_command(label= "Select all",command = lambda:print("You have pressed select all"))
selectionmenu.add_command(label= "Expand selection",command = lambda:print("You have pressed expand selection"))
selectionmenu.add_command(label= "Shrink selection",command = lambda:print("You have pressed shrink selection"))
selectionmenu.add_separator()
selectionmenu.add_command(label= "Copy line up",command = lambda:print("You have pressed copy line up"))
selectionmenu.add_command(label= "Copy line down",command = lambda:print("You have pressed copy line down"))
menubar.add_cascade(label="Selection",menu = selectionmenu)

viewmenu = Menu(menubar)
viewmenu.add_command(label= "Command palette",command = lambda:print("You have pressed command palette"))
viewmenu.add_command(label= "Open view",command = lambda:print("You have pressed open view"))
viewmenu.add_separator()
viewmenu.add_command(label= "Appearance",command = lambda:print("You have pressed appearance"))
viewmenu.add_command(label= "Editor Layout",command = lambda:print("You have pressed editor layout"))
menubar.add_cascade(label="View",menu = viewmenu)

gomenu = Menu(menubar)
gomenu.add_command(label= "Back",command = lambda:print("You have pressed back"))
gomenu.add_command(label= "Forward",command = lambda:print("You have pressed forward"))
gomenu.add_command(label= "Last Edit Location",command = lambda:print("You have pressed last edit location"))
gomenu.add_separator()
gomenu.add_command(label= "Switch Editor",command = lambda:print("You have pressed switch editor"))
gomenu.add_command(label= "Switch Group",command = lambda:print("You have pressed switch group"))
menubar.add_cascade(label="Go",menu = gomenu)

runmenu = Menu(menubar)
runmenu.add_command(label= "Start Debugging",command = lambda:print("You have pressed start debugging"))
runmenu.add_command(label= "Run Without Debugging",command = lambda:print("You have pressed run without debugging"))
runmenu.add_command(label= "Stop Debugging",command = lambda:print("You have pressed stop debugging"))
runmenu.add_command(label= "Restart Debugging",command = lambda:print("You have pressed restart debugging"))
menubar.add_cascade(label="Run",menu = runmenu)





root.mainloop()