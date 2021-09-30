from tkinter import *
from os import system

root = Tk()
root.title('Apt interface')

update = Button(root, text="update", command=lambda: system('sudo apt update && exit'))
update.pack()
upgrade = Button(root, text="upgrade", command=lambda: system('sudo apt upgrade && exit'))
upgrade.pack()
list = Button(root, text="list upgradable", command=lambda: system('apt list --upgradable && exit'))
list.pack()
autoremove = Button(root, text="autoremove", command=lambda: system('sudo apt autoremove && exit'))
autoremove.pack()
autoclean = Button(root, text="autoclean", command=lambda: system('sudo apt autoclean && exit'))
autoclean.pack()

root.mainloop()