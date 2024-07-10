from tkinter import *
from CPUINFO import *
from MemoryINFO import *
from motherboard import *
from test import *
import wget
import zipfile



root = Tk()
root.title("电脑检测")
root.geometry("600x450")
#root.overrideredirect(True)




mouse_sp = Label(root)
mouse_sp.pack()

Test_cpu = Button(root,text="检测cpu",command=lambda:root.after(1,lambda:testcpu(Test_frame_text)))
Test_cpu.place(x=10,y=30)
Test_memory = Button(root,text="检测内存",command=lambda:root.after(1,lambda:testmemory(Test_frame_text)))
Test_memory.place(x=80,y=30)
Test_motherboard = Button(root,text="检测主板",command=lambda:root.after(1,lambda:testmotherboard(Test_frame_text)))
Test_motherboard.place(x=150,y=30)

Test_frame_text = Text(root,height=25,width=35)
Test_frame_text.place(x=10,y=60)

def findnew():
    url = "https://codeload.github.com/YangZhun6/ComputerChecker/zip/refs/heads/main"
    wget.download(url,"new.zip")
    file_url = "new.zip"
    zipfiles = zipfile.ZipFile(file_url)
    zipfiles.extractall("/")
    zipfiles.close()
find_new = Button(root,text="检查更新",command=lambda:root.after(1000,findnew))
find_new.place(x=10,y=410)
