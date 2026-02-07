import psutil

def get_system_health():

    user_cpu_threshold = float(input("Enter CPU usage threshold percentage: "))
    user_memory_threshold = float(input("Enter Memory usage threshold percentage: "))
    user_disk_threshold = float(input("Enter Disk usage threshold percentage: "))

    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')


    if cpu_usage > user_cpu_threshold:
        print(f"Warning: CPU usage is at {cpu_usage}% which exceeds the threshold of {user_cpu_threshold}%")   
    else:
        print(f"CPU usage is at {cpu_usage}%, within the threshold.")

    if memory.percent > user_memory_threshold:
        print(f"Warning: Memory usage is at {memory.percent}% which exceeds the threshold of {user_memory_threshold}%")
    else:
        print(f"Memory usage is at {memory.percent}%, within the threshold.")

    if disk.percent > user_disk_threshold:
        print(f"Warning: Disk usage is at {disk.percent}% which exceeds the threshold of {user_disk_threshold}%")
    else:
        print(f"Disk usage is at {disk.percent}%, within the threshold.")   
    
    print("Uptime:", psutil.boot_time())  #In seconds


get_system_health()