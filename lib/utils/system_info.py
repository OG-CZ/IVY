import psutil
import math


def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return f"{s} {size_name[i]}"


def get_cpu_usage():
    cpu_percent = psutil.cpu_percent(interval=1)
    return f"CPU usage is at {cpu_percent}%"


def get_memory_usage():
    mem = psutil.virtual_memory()
    used = convert_size(mem.used)
    total = convert_size(mem.total)
    percent = mem.percent
    return f"Memory usage is {used} out of {total} ({percent}% used)"


def get_battery_level():
    battery = psutil.sensors_battery()
    if not battery:
        return "This device does not have a battery"
    percent = battery.percent
    plugged = "charging" if battery.power_plugged else "not charging"
    return f"Battery is at {percent}% and is currently {plugged}"


def get_disk_usage():
    disk = psutil.disk_usage("/")
    used = convert_size(disk.used)
    total = convert_size(disk.total)
    percent = disk.percent
    return f"Disk usage is {used} out of {total} ({percent}% used)"


def get_system_summary():
    cpu = get_cpu_usage()
    mem = get_memory_usage()
    battery = get_battery_level()
    disk = get_disk_usage()
    return f"{cpu}, {mem}, {battery} and the {disk}"
