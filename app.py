from dlink.dlink import Dlink
from dlink.base_command import ip_info
from dlink.packed_command import Packed
from settings import HOST, USERNAME, PASSWORD, LOG_FILE_NAME

def main():

    d = Dlink(HOST, USERNAME,PASSWORD)
    d.connect()
    t = Packed()
    cmd = t.sys_info()
    d.send_command(cmd)
    d.send_command(ip_info())
    d.disconnect()
    d.write_log(LOG_FILE_NAME)


if __name__ == "__main__":
    main()
