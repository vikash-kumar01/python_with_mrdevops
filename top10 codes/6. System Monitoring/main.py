import psutil

def system_stats():
    cpu_util = psutil.cpu_percent(interval=1)
    mem_util = psutil.virtual_memory().percent
    print(f"CPU Usage: {cpu_util}%")
    print(f"Memory Usage: {mem_util}%")   
    
    
system_stats()