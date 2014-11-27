from telnetlib import Telnet


class Dlink:
    log = []
    def __init__(self, ip, username, password):
        self.ip = ip
        self.username = username
        self.password = password

    def connect(self):
        self.tn = Telnet(self.ip)
        self.tn.read_until("Login: ")
        self.tn.write(self.username + "\r")
        self.tn.read_until("Password: ")
        self.tn.write(self.password + "\r")
        if self.tn.read_until("> "):
            return self.tn
        else:
            return "Something wrong..."

    def send_command(self, command):
        for cmd in command:
            print "sending command: %s" % cmd
            self.tn.write(cmd + "\r")
            t = self.tn.read_until("> ")
            print t
            self.log.append(t)

    def disconnect(self):
        try:
            self.tn.close()
            return "Disconnected.."
        except:
            return "cannot disconnect.."

    def write_log(self, filename):
        f = open(filename, "a")
        f.write('\n'.join(self.log))


