from tkinter import *
from CPUINFO import *
from MemoryINFO import *
from motherboard import *

def testcpu():
    global Test_frame_text
    Test_frame_text.delete('1.0',"end")
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
    Test_frame_text.insert('end',cpu_information)
    print(cpu_information)

def testmemory():
    global Test_frame_text
    Test_frame_text.delete('1.0',"end")
    memory_information=f"\
-------内存检测结果------\n\
memory_total:{memory_total()}\
memory_available:{memory_available()}\
memory_used:{memory_used()}\
memory_usage:{memory_usage()}\
max_memory_capacity:{get_max_memory_capacity()}\
memory_speeds:{memory_speeds()}\
memory_sizes:{memory_sizes()}\
memory_num:{memory_num()}\
-----------------------"
    Test_frame_text.insert('end',memory_information)
    print(memory_information)

def testmotherboard():
    global Test_frame_text
    Test_frame_text.delete('1.0',"end")
    motherboard_information=f"\
-------主板检测结果------\n\
:{motherboard_vendor()}\n\
:{Hardware.get_baseboard_sn()}\n\
:{Hardware.get_bios_sn()}\n\
-----------------------"
    Test_frame_text.insert('end',motherboard_information)
    print(motherboard_information)



root = Tk()
root.title("电脑检测")
root.geometry("600x450")
root.overrideredirect(True)




mouse_sp = Label(root)
mouse_sp.pack()

Test_cpu = Button(root,text="检测cpu",command=lambda:root.after(1,testcpu))
Test_cpu.place(x=10,y=30)
Test_memory = Button(root,text="检测内存",command=lambda:root.after(1,testmemory))
Test_memory.place(x=80,y=30)
Test_motherboard = Button(root,text="检测主板",command=lambda:root.after(1,testmotherboard))
Test_motherboard.place(x=150,y=30)

Test_frame_text = Text(root,height=25,width=35)
Test_frame_text.place(x=10,y=60)
