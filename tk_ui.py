from tkinter import *
from CPUINFO import *
from MemoryINFO import *
from motherboard import *
from test import *
import wget
import zipfile
import os


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

def findnew(Test_frame_text):
    Test_frame_text.delete('1.0',"end")
    url = "https://codeload.github.com/YangZhun6/ComputerChecker/zip/refs/heads/main"
    wget.download(url,"new.zip")
    file_url = "new.zip"
    with zipfile.ZipFile("new.zip","r") as z:
        z.extractall("./")
        z.close()
    with open("ComputerChecker-main/version.txt","r") as f:
        new_ver = f.read()
    with open("version.txt","r") as f:
        now_ver = f.read()
    if float(now_ver) < float(new_ver):
        Test_frame_text.insert('end',"有新的版本,自动更新")
    else:
        Test_frame_text.insert('end',"现在这个版本已经很新了")
    os.remove("new.zip")
find_new = Button(root,text="检查更新",command=lambda:root.after(1000,lambda:findnew(Test_frame_text)))
find_new.place(x=10,y=410)
