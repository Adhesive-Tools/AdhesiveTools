import os
import msvcrt
import ctypes
import hashlib
import uuid
import socket
from pystyle import Colorate, Colors, Center


def check_maintenance():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)
            s.connect((IP, PORT))
            s.sendall(b"GET_STATUS")
            status = s.recv(BUFFER_SIZE).decode('utf-8')
            return status.lower() == "active"
    except socket.error as e:
        print(f"Erreur de connexion au serveur de maintenance : {e}")
        return False

def get_hwid():
    hwid = hashlib.sha256(uuid.UUID(int=uuid.getnode()).bytes).hexdigest()
    return f"Adhesive-{hwid[:16]}"

def SetConsoleTitle(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)

def Title():
    ascii_art = """
                                             ▄▄  ▄▄                        ▄▄                     
                               ██           ▀███ ███                        ██                     
                              ▄██▄            ██  ██                                               
                             ▄█▀██▄      ▄█▀▀███  ███████▄   ▄▄█▀██ ▄██▀██████ ▀██▀   ▀██▀  ▄▄█▀██ 
                            ▄█  ▀██    ▄██    ██  ██    ██  ▄█▀   ████   ▀▀ ██   ██   ▄█   ▄█▀   ██
                            ████████   ███    ██  ██    ██  ██▀▀▀▀▀▀▀█████▄ ██    ██ ▄█    ██▀▀▀▀▀▀
                           █▀      ██  ▀██    ██  ██    ██  ██▄    ▄█▄   ██ ██     ███     ██▄    ▄
                         ▄███▄   ▄████▄ ▀████▀███▄███  ████▄ ▀█████▀██████▀████▄    █       ▀█████▀
    """
    print(Colorate.Vertical(Colors.blue_to_purple, Center.XCenter(ascii_art)))

def Clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def StartProgram(script_choice):
    scripts = {
        "1": "massdm.py", 
        "2": "delfriends.py",
        "3": "block.py",
        "4": "idtoken.py",
        "5": "Server_Lookup.py",
        "6": "delbook.py",
        "7": "webhookspam.py",
        "8": "discordbot.py",
        "9": "discordraid.py",
        "10": "hypesquad.py",
        "11": "nitrogen.py",
        "12": "Phishing-Attack.py",
        "13": "sqlvul.py",
        "14": "snusbase.py",
        "15": "ipinger.py",
        "16": "doxcreate.py",
        "17": "main.py",
        "19": "alldecompile.py"
    }

    pyw_scripts = {
        "18": "builder.pyw"
    }

    script_name = scripts.get(script_choice) or pyw_scripts.get(script_choice)
    if script_name:
        script_path = os.path.join('utils', 'main', 'tools', script_name)
        if os.path.exists(script_path):
            if script_path.endswith('.pyw'):
                # Use pythonw.exe to run .pyw files
                os.system(f'pythonw "{script_path}"')
            else:
                os.system(f'python "{script_path}"')
        else:
            print(f"Script {script_name} not found at {script_path}")
    else:
        print("Invalid choice. Please select a valid option.")

def format_option(option):
    return option.ljust(30)[:30].replace("-", " ")

page_1 = [
    "[1]massdm", "[2]deleteallfriends", "[3]blockallfriends", "[4]idtotoken", "[5]serverinfo", "[6]deletewebhook", "[7]webhookspam", "[8]invitebot", "[9]discordraid", "[10]hypesquad-changer", "[11]nitrogen"
]

page_2 = [
    "[12]phishing", "[13]vulnérabilitéSQL", "[14]snusbase", "[15]ip-ping", "[16]doxcreate"
]

page_3 = [
    "[17]Blankdecompile", "[18]buildgrabber", "alldecompile"
]

all_pages = [page_1, page_2, page_3]

def generate_menu(page_number):
    page_options = all_pages[page_number - 1]
    
    page_header = f"{white}[{violet}Page {page_number}{white}]"
    page_body = "\n".join([
        f"{violet}->{white} {format_option(opt)}"
        for opt in page_options
    ])
    
    if page_number > 1:
        page_body += f"\n   {white}[{violet}<{white}] {violet}-> {option_previous.ljust(30)[:30]}"
    if page_number < len(all_pages):
        page_body += f"\n   {white}[{violet}>{white}] {violet}-> {option_next.ljust(30)[:30]}"

    return f"""{page_header}
{page_body}

"""

violet = '\033[95m'
white = '\033[97m'
reset = '\033[0m'

# Menu options
option_next = "Page suivante >>"
option_previous = "<< Page précédente"

def WelcomeScreen():
    Clear()
    print(f"{violet}Adhesive{reset} Merci de votre confiance. Appuyez sur la touche espace pour continuer.")
    while True:
        if msvcrt.kbhit() and msvcrt.getch() == b' ':
            break

def Menu(page_number):
    return generate_menu(page_number)

if __name__ == "__main__":
    SetConsoleTitle("ADHESIVE - TOOLS")
    Title()
    WelcomeScreen()

    current_page = 1
    total_pages = len(all_pages)

    while True:
        try:
            Clear()
            Title()
            print(Menu(current_page))
            choice = input(f"{violet}|──({white}root@Adhesive{violet})─[{white}~/Main-{current_page}{violet}]\n└──{white}$ {reset}")

            if choice.lower() == 'q':
                print("\nExiting...")
                break
            
            # Check for page navigation
            if choice == ">":
                if current_page < total_pages:
                    current_page += 1
            elif choice == "<":
                if current_page > 1:
                    current_page -= 1
            else:
                # Extract script number from the choice
                try:
                    script_number = choice.split(']')[0].strip('[')
                    if script_number in [opt.split(']')[0].strip('[') for opt in all_pages[current_page - 1]]:
                        StartProgram(script_number)
                    else:
                        print("Invalid choice. Please select a valid option.")
                except ValueError:
                    print("Invalid input. Please enter a valid option.")
                
        except KeyboardInterrupt:
            print("\nExiting...")
            break