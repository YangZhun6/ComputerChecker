from tkinter import *
from CPUINFO import *
from MemoryINFO import *
from motherboard import *

def testcpu():
    global Test_cpu_frame_text
    cpu_information=f"\
-------CPU检测结果------\n\
cpu_max_freq:{cpu_max_freq()}\n\
cpu_names:{cpu_names()}\n\
cpu_count:{cpu_count()}\n\
cpu_count_both:{cpu_count_both()}\n\
all_cpu_usage:{all_cpu_usage()}\n\
cpu_usage:{cpu_usage(1)}\n\
cpuid:{cpuid()}\n\
-----------------------"
    Test_cpu_frame_text.insert('end',cpu_information)
    print(cpu_information)


root = Tk()
root.title("电脑检测")
root.geometry("600x450")
root.overrideredirect(True)




mouse_sp = Label(root)
mouse_sp.pack()

Test_cpu = Button(root,text="检测cpu",command=lambda:root.after(1,testcpu))
Test_cpu.place(x=10,y=30)

Test_cpu_frame_text = Text(root,height=25,width=35)
Test_cpu_frame_text.place(x=10,y=60)
