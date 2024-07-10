import psutil
import subprocess



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
'''
def get_memory_voltages():
    try:
        # 执行wmic命令
        result = subprocess.run(['wmic', 'memorychip', 'get', 'BankLabel, Voltage'], capture_output=True, text=True)
        # 获取输出结果
        output = result.stdout
        # 去除标题行和空行
        lines = [line for line in output.split('\n') if line.strip() and 'wmic' not in line and 'Voltage' in line]
        # 提取电压值
        voltages = []
        for line in lines:
            voltage_value = line.split('Voltage')[-1].strip()
            try:
                voltages.append(float(voltage_value))
            except ValueError:
                continue
        return voltages
    except Exception as e:
        # 如果发生异常，返回错误信息
        return [str(e)]

print(memory_total())
print(memory_available())
print(memory_used())
print(memory_usage())
print(get_max_memory_capacity())
print(memory_speeds())
print(memory_sizes())
print(memory_num())
'''