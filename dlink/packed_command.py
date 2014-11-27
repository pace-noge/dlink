from base_command import *

class Packed:

    def sys_info(self):
        return mem_info() + cpu_info() + free_mem()

    def network_info(self):
        return if_config() + route()