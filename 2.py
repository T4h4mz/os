import pynvml
import time

pynvml.nvmlInit()


for i in range(int(5)):
    deviceCount = pynvml.nvmlDeviceGetCount()
    print("deviceCount : " + str(deviceCount))
    for i in range(deviceCount):
        handle = pynvml.nvmlDeviceGetHandleByIndex(i)

        name = pynvml.nvmlDeviceGetName(handle)
        print(f"GPU {i} : {name.encode('utf-8').decode()}") 

        meminfo = pynvml.nvmlDeviceGetMemoryInfo(handle)
        print(f"memory (total) : {meminfo.total/1024/1024:.2f} (MB)")
        print(f"memory (free) : {meminfo.free/1024/1024:.2f} (MB)")
        print(f"memory (used) : {meminfo.used/1024/1024:.2f} (MB)")

        utilization = pynvml.nvmlDeviceGetUtilizationRates(handle)
        print(f"GPU utilization: {utilization.gpu} %")
        print(f"memory utilization: {utilization.memory} %")

        temperature = pynvml.nvmlDeviceGetTemperature(handle, pynvml.NVML_TEMPERATURE_GPU)
        print(f"GPU temp : {temperature} (c)")

        time.sleep(1) #ijade vaqfe 


pynvml.nvmlShutdown()
