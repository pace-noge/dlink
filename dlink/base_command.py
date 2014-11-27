

def mem_info():
    return ["meminfo"]

def cpu_info():
    return ["cat proc/cpuinfo"]

def free_mem():
    return ["cat /proc/meminfo"]

def os_version():

    return ["cat /proc/version"]

def running_process():

    return ["ps"]

def kernel_module():
    return ["lsmod"]

def if_config():
    return ["ifconfig"]

def ip_info():
    return ["ifconfig ppp0"]

def route():
    return ["route"]

def get_speed():
    return ["cat /proc/avalanche/eth0_rfc2665_stats"]

def modem_stats():
    return ["cat /proc/avalanche/avsar_modem_stats"]

def reboot():
    return ["reboot"]
