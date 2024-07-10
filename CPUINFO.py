import psutil
import wmi
import win32com.client
import platform  
import subprocess



id = wmi.WMI()
def cpu_max_freq():  
    # 使用wmic命令获取CPU信息  
    command = "wmic cpu get MaxClockSpeed, ProcessorId"  
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, text=True)  
      
    if result.returncode != 0:  
        return "Failed to retrieve CPU information"  
      
    # 解析输出以获取MaxClockSpeed  
    frequencies = []  
    previous_processor_id = None  
    current_frequency = None  
      
    for line in result.stdout.strip().split('\n'):  
        if line:  
            parts = line.split()  
            if len(parts) >= 2:  
                clock_speed = parts[0]  # MaxClockSpeed  
                processor_id = parts[1]  # ProcessorId  
                  
                # 假设具有不同ProcessorId的CPU是不同的物理CPU  
                # 注意：这个假设可能不适用于所有情况，因为有些系统可能使用不同的ID格式  
                if processor_id != previous_processor_id:  
                    if current_frequency is not None:  
                        frequencies.append(current_frequency)  
                    current_frequency = clock_speed  
                    previous_processor_id = processor_id  
                  
                # 如果这是最后一行，也需要添加最后一个频率  
                if line == result.stdout.strip().split('\n')[-1]:  
                    frequencies.append(current_frequency)  
      
    # 如果没有找到任何频率（理论上不应该发生，除非输出格式与预期不同），则返回错误消息  
    if not frequencies:  
        return "No CPU frequencies found"  
      
    return frequencies  
def cpu_names():  
    if platform.system().lower() == 'windows':  
        # 使用wmic命令获取CPU型号  
        command = "wmic cpu get name /format:list"  
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, text=True)  
        cpu_models = []  
        if result.returncode == 0:  
            # 过滤出CPU型号（假设输出格式中Name后面跟着的就是型号）  
            for line in result.stdout.strip().split('\n'):  
                if line.startswith('Name='):  
                    cpu_models.append(line.split('=')[-1].strip())  
        return cpu_models  
    else:  
        return "Unsupported operating system"  
  
def cpu_count():
# 获取CPU核心数
    cpu_count = psutil.cpu_count(logical=False)
    return cpu_count
def cpu_count_both():# 获取逻辑CPU核心数（包括超线程）
    logical_cpu_count = psutil.cpu_count(logical=True)
    return logical_cpu_count



def all_cpu_usage():  
    # 获取CPU总使用率，等待一秒钟的采样时间  
    cpu_usage = psutil.cpu_percent(interval=1)  
    # 返回CPU使用率  
    return cpu_usage
def cpu_usage(a):  
    # 确保传入的a是一个有效的核心编号  
    if not isinstance(a, int) or a < 1 or a > psutil.cpu_count(logical=True):  
        return "Invalid CPU core number"  
    # 获取CPU逻辑核心使用率 
    cpu_usages = psutil.cpu_percent(interval=1, percpu=True)  
    # 为了以后有空间升级，保留这个检查
    if a - 1 < len(cpu_usages):  
        return f"{cpu_usages[a-1]}"  
    else:  
        # 由于上面的条件检查，这行代码永远不会被执行  
        return "Requested CPU core does not exist"  
    
def cpuid():
    # CPU序列号
    cc = ""
    for cpu in id.Win32_Processor():
        # print(cpu.ProcessorId.strip())
        cc += cpu.ProcessorId.strip()
    return cc

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

