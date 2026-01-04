import socket
from concurrent.futures import ThreadPoolExecutor
import argparse

def scanPort(host, port, grabBannerBool) :

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock :
        sock.settimeout(1) # Pour soc.connect <= 1s

        try :
            if sock.connect_ex((host, port)) == 0 :
                if grabBannerBool :
                    grabBanner(host, port, sock)
                else :
                    print(f"[+] Port {port}")

        except OSError :
            print(f"[!] Port {port} OSError")

    return 0

def scanPortThread(host, ports, grabBannerBool, max_threads=100) :
    with ThreadPoolExecutor(max_workers=max_threads) as executor :
        for port in ports :
            executor.submit(scanPort, host, port, grabBannerBool)

def grabBanner(host, port, sock) :
    try :
        sock.send(b'HEAD / HTTP/1.1\r\n\r\n')
        banner = sock.recv(1024).decode('utf-8', errors='ignore')

        if banner :
            print(f"[+] Port {port} : {banner.strip()}\n")
        else :
            print(f"[-] Port {port} : Pas de bannière\n")

    except OSError :
        print(f"[!] Port {port} : OSError\n")

# TEST ~~ ~~ ~~ ~~ ~~ ~~ ~~

if __name__ == "__main__" :

    parser = argparse.ArgumentParser(description="Scanner de ports")

    parser.add_argument('host',
                        type=str,
                        help="Adresse IP ou nom de domaine à scanner"
                        )
    parser.add_argument('--ports',
                        type=int,
                        nargs=2,
                        metavar=("START", "END"),
                        default=[1, 1024],
                        help="Liste des ports à scanner"
                        )
    parser.add_argument('--banners',
                        action="store_true",
                        help="Affiche les bannières des ports ouverts"
                        )
    parser.add_argument('--max-threads',
                        type=int,
                        default=100,
                        help="Nombre de thredPool"
                        )

    args = parser.parse_args()

    start, end = args.ports
    portToScan = range(start, end+1) # List des ports

    scanPortThread(args.host, portToScan, args.banners, args.max_threads)
