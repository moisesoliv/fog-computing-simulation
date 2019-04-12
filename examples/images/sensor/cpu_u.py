import psutil

def cpu_u():
    t = [proc.cpu_percent(interval=0.1) for proc in psutil.process_iter()]
    return sum(t)/psutil.cpu_count()

print(cpu_u())
