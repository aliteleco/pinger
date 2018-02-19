
#in the name of God


import os
import sys
import datetime
import time

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


def main():
    if len(sys.argv) > 1:
        ip = sys.argv[1]                # IP
        
        log_dest = "log.txt"
        if len(sys.argv) == 3:
            log_dest = sys.argv[2]      # log file name

        os_name = os.name
        #print 'Macos'
        last_state = None
        while True:
            if os_name == 'posix':
                ping_res = os.popen('ping -c 1 {}'.format(ip)).read()
            elif os_name == 'nt':
                ping_res = os.popen('ping -n 1 {}'.format(ip)).read()
            else:
                print "your os cann't support :("
                exit()
            #print ping_res
            for any_line in ping_res:
                if "time=" in ping_res:
                    if last_state == False or last_state == None:
                        write_log(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S') + '-OK',log_dest)
                    last_state = True
                else:
                    if last_state == True:
                        write_log(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S') + '-NOK',log_dest)
                    last_state = False
            os.system('cls' if os.name == 'nt' else 'clear')
            print "Pinger!! \nLast status is:"
            
            if last_state:
                print color.GREEN
                print "OK"
            else:
                print color.RED
                print "NOK"
            print color.END
            time.sleep(1)
    else:
        print "Please type ip address :)"

def write_log(data,log_dest):
    with open(log_dest, 'a') as the_file:
        the_file.write(data+"\n")
if __name__ == "__main__":
     main()