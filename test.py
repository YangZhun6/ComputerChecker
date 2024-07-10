from tkinter import *
from CPUINFO import *
from MemoryINFO import *
from motherboard import *


def testcpu(Test_frame_text):
    
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
------------------------"
    Test_frame_text.insert('end',cpu_information)
    print(cpu_information)

def testmemory(Test_frame_text):
    
    Test_frame_text.delete('1.0',"end")
    memory_information=f"\
-------内存检测结果------\n\
memory_total:{memory_total()}\n\
memory_available:{memory_available()}\n\
memory_used:{memory_used()}\n\
memory_usage:{memory_usage()}\n\
max_memory_capacity:{get_max_memory_capacity()}\n\
memory_speeds:{memory_speeds()}\n\
memory_sizes:{memory_sizes()}\n\
memory_num:{memory_num()}\n\
-------------------------"
    Test_frame_text.insert('end',memory_information)
    print(memory_information)

def testmotherboard(Test_frame_text):
  
    Test_frame_text.delete('1.0',"end")
    motherboard_information=f"\
-------主板检测结果------\n\
motherboard_vendor:{motherboard_vendor()}\n\
baseboard_sn:{Hardware.get_baseboard_sn()}\n\
bios_sn:{Hardware.get_bios_sn()}\n\
-------------------------"
    Test_frame_text.insert('end',motherboard_information)
    print(motherboard_information)