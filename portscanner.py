import socket,colors,time,sys,threading,argparse
import concurrent.futures 
from datetime import datetime
from colorama import Fore
print_lock = threading.Lock()
parser = argparse.ArgumentParser()
parser.add_argument('-t','--target',metavar='',help='IP of the target or domain. (Ex. google.com)')
parser.add_argument('-pl','--portlimit',metavar='',help='Number limit of the port scanning,(Ex. 1000)')
args = parser.parse_args()
class PortScanner(object):
    def __init__(self,target,portl):
        self.target = target
        self.portl = portl
    def banner(self):
       now = datetime.now()
       dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
       print(f"""{colors.BGreen}
╔╦╗┬ ┬┬─┐┌─┐┌─┐┌┬┐┌─┐┌┬┐  ╔═╗┌─┐┬─┐┌┬┐  ╔═╗┌─┐┌─┐┌┐┌┌┐┌┌─┐┬─┐
 ║ ├─┤├┬┘├┤ ├─┤ ││├┤  ││  ╠═╝│ │├┬┘ │   ╚═╗│  ├─┤││││││├┤ ├┬┘
 ╩ ┴ ┴┴└─└─┘┴ ┴─┴┘└─┘─┴┘  ╩  └─┘┴└─ ┴   ╚═╝└─┘┴ ┴┘└┘┘└┘└─┘┴└─
               """) 
       print(Fore.WHITE + "─" * 38)
       print(f"{Fore.GREEN}Github: {Fore.WHITE}https://github.com/FonderElite")
       print(Fore.WHITE + "─" * 38)
       time.sleep(0.3)
       print(f"{Fore.WHITE}Scanning Target: {Fore.GREEN}{self.target}")
       time.sleep(0.5)
       print(f"{Fore.WHITE}Script started at: {Fore.GREEN}{str(dt_string)}{Fore.WHITE}")       
       if args.target == None or args.portlimit == None:
           pass
       else:
           time.sleep(0.5)
           print(f"{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}]Scanning {self.portl} ports.\n")
    def scan_ports(self,port):
        scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        scanner.settimeout(1)
        try:
            scanner.connect((self.target,port))
            scanner.close()
            with print_lock:
                print(f'{colors.BWhite}[{colors.BGreen}+{colors.BWhite}]Open Port: {port}')
                if port == 80:
                    print(f"{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}]HTTP.\n")
                elif port == 443:
                    print(f"{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}]HTTPS.\n")

        except KeyboardInterrupt:
            print(f"{Fore.WHITE}[{Fore.RED}-{Fore.WHITE}]Exiting Program.")
            sys.exit()
        except socket.gaierror:
            print(f"{WHITE}[{Fore.RED}-{Fore.WHITE}]Hostname Could Not Be Resolved.")
            sys.exit()
        except socket.error:
            pass

if __name__ == "__main__":
    call_class = PortScanner(args.target,args.portlimit)
    banner = call_class.banner()
    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=250) as executor:
            for port in range(int(args.portlimit)):

                executor.submit(call_class.scan_ports,port + 1)
    except TypeError:
        print(f"{Fore.GREEN}Usage: {Fore.CYAN}python3 {Fore.WHITE}<portscanner.py> {Fore.GREEN}-t {Fore.WHITE}<target> {Fore.GREEN}-pl {Fore.WHITE}<port-limit>")


