from CPUINFO import *
from MemoryINFO import *
from motherboard import *
from tk_ui import *
from tkinter import *
id = wmi.WMI()



def print_pos(event):
    x, y = event.widget.winfo_pointerxy()
    #print("鼠标位置：x=", x, " y=", y)
    mouse_sp.config(text=f"x:{x},y:{y}")

root.bind('<Motion>', print_pos)
root.mainloop()

