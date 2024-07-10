import psutil
import subprocess
import re
'''
创建日期：2024 7 9 19：00
创建者：YZ(github:YangZhun6)
描述：检测内存信息的模块，仅在Windows系统有效
版本：V1.0
转载代码请标明原出处,请勿对代码进行商业盈利活动
'''
def remove_elements(arr, n):#必要代码
    return arr[n:]
# 获取内存总数
def memory_total():   
    total_memory = psutil.virtual_memory().total    
    total_memory_gb = total_memory / (1024 ** 3)  
    return round(total_memory_gb, 2)
# 获取可用内存
def memory_available():
    available_memory = psutil.virtual_memory().available
    available_memory_GB=available_memory / (1024 ** 3)
    return round(available_memory_GB, 2)
#获取已用内存（虽然没有必要）
def memory_used():
    memory_used = memory_total()-memory_available()
    return round(memory_used, 2)
# 获取内存使用率
def memory_usage():
    memory_usage = psutil.virtual_memory().percent
    return memory_usage
def get_max_memory_capacity():
    try:
        result = subprocess.run('Wmic memphysical get maxcapacity', shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            output = result.stdout.strip()
        else:
            output = result.stderr.strip()
    except Exception as e:
        output = str(e)
        
    n = 15
    result = remove_elements(output, n)#清除不用的内容

    return int(result) / 1048576

def memory_speeds():
    try:
        # 执行wmic命令
        result = subprocess.run(['wmic', 'memorychip', 'get', 'speed'], capture_output=True, text=True)
        output = result.stdout
        speeds = [line.strip() for line in output.split('\n') if line.strip() and line.strip() != 'Speed']
        # 返回内存频率列表
        return speeds
    except Exception as e:
        # 如果发生异常，返回错误信息
        return str(e)
def memory_num():
    temp = len(memory_speeds())#查看列表数量即内存数量
    return temp
def memory_sizes():#单位：GB，查看每根内存大小
    try:
        # 执行wmic命令
        result = subprocess.run(['wmic', 'memorychip', 'get', 'Capacity'], capture_output=True, text=True)
        output = result.stdout
        lines = [line for line in output.split('\n') if line.strip() and line.strip() != 'Capacity']
        memory_sizes_mb = [int(line.split()[0]) / 1073741824 for line in lines if line.split()[0].isdigit()]
        return memory_sizes_mb
    except Exception as e:
        # 如果发生异常，返回错误信息
        return [str(e)]

def memory_MaxVoltage():
    # 命令用于获取内存电压信息
    command = 'wmic path Win32_PhysicalMemory get DeviceLocator, MaxVoltage'
    
    # 执行命令并捕获输出
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while executing the command: {e.output.decode()}")
        return []
    
    # 将输出结果转换为字符串
    output = result.decode()
    
    # 使用正则表达式匹配内存电压
    memory_types = re.findall(r'(DIMM\d+)\s+(\d+)', output)
    
    # 提取内存电压并存储到列表中
    memory_types_list = [type_num for _, type_num in memory_types]
    
    return memory_types_list

'''
各个数字代表的内存类型适用于memory_types()函数，此规则暂时没有DDR5的准确数据，以后有人愿意提供数据请联系作者：yzbox_2023@qq.com只要在CMD运行wmic path Win32_PhysicalMemory get DeviceLocator, SMBIOSMemoryType就好了，请确保你的内存是DDR5,原网址：https://learn.microsoft.com/en-us/windows/win32/cimwin32prov/win32-physicalmemory
        0: "Unknown",
        1: "Other",
        2: "DRAM",
        3: "Synchronous DRAM",
        4: "Cache DRAM",
        5: "EDO",
        6: "EDRAM",
        7: "VRAM",
        8:  "SRAM",
        9: "RAM",
        10: "ROM",
        11: "Flash",
        12: "EEPROM",
        13: "FEPROM",
        14: "EPROM",
        15: "CDRAM",
        16: "3DRAM",
        17: "SDRAM",
        18: "SGRAM",
        19: "RDRAM",
        20: "DDR",
        21: "DDR2",
        22: "DDR2 FB-DIMM",  可能不可用，微软说的
        24: "DDR3",   可能不可用，微软说的
        25: "FBD2",
        26: "DDR4",
        27: "DDR5"DDR5是猜的，不一定是这个
'''
def memory_types():
    # 命令用于获取内存代数信息
    command = 'wmic path Win32_PhysicalMemory get DeviceLocator, SMBIOSMemoryType'
    
    # 执行命令并捕获输出
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while executing the command: {e.output.decode()}")
        return []
    
    # 将输出结果转换为字符串
    output = result.decode()
    
    # 使用正则表达式匹配内存代数
    memory_types = re.findall(r'(DIMM\d+)\s+(\d+)', output)
    
    # 提取内存代数并存储到列表中
    memory_types_list = [type_num for _, type_num in memory_types]
    
    return memory_types_list
def memory_Manufacturers():
    # 命令用于获取内存厂商信息
    command = 'wmic path Win32_PhysicalMemory get DeviceLocator, Manufacturer'
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while executing the command: {e.output.decode()}")
        return []
    
    # 将输出结果转换为字符串
    output = result.decode()
    
    # 切分输出为行
    lines = output.strip().split('\n')
    
    # 跳过标题行
    lines = lines[1:]
    
    # 使用正则表达式匹配每行的内存厂商
    manufacturers_list = []
    for line in lines:
        match = re.match(r'(.+?)\s+(.+)', line)
        if match:
            device_locator, manufacturer = match.groups()
            manufacturers_list.append(manufacturer.strip())
    
    return manufacturers_list
'''
print(memory_total())
print(memory_available())
print(memory_used())
print(memory_usage())
print(get_max_memory_capacity())
print(memory_speeds())
print(memory_sizes())
print(memory_num())
print(memory_types())
print(memory_MaxVoltage())
print(memory_Manufacturers())
'''
