import subprocess 
import wmi 
'''
创建日期：2024 7 9 19：00
创建者：YZ(github:YangZhun6)
描述：检测内存信息的模块，仅在Windows系统有效
版本：V1.1
转载代码请标明原出处,请勿对代码进行商业盈利活动
'''
id = wmi.WMI()
def motherboard_vendor():  
    # 使用wmic命令获取主板的厂商信息  
    command = "wmic baseboard get Manufacturer /format:list"  
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, text=True)  
    if result.returncode != 0:  
        return "Failed to retrieve motherboard information"  
    # 解析输出以获取厂商信息   
    for line in result.stdout.strip().split('\n'):  
        if line.startswith('Manufacturer='):  
            return line.split('=')[-1].strip()  
      
    return "Motherboard vendor information not found" 
class Hardware:
    @staticmethod
    def get_baseboard_sn():#部分主板无法查询,主板序列号


        for board_id in id.Win32_BaseBoard():
            # print(board_id.SerialNumber)
            return board_id.SerialNumber

    @staticmethod
    def get_bios_sn():#BIOS序列号
        for bios_id in id.Win32_BIOS():
            return bios_id.SerialNumber.strip()

'''
print(motherboard_vendor())
print(Hardware.get_baseboard_sn())
print(Hardware.get_bios_sn())
'''