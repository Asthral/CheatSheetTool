import configparser
import argparse
import subprocess
import base64
import socket
import re
import time
from os import path, chdir
import readline
import platform
import subprocess
import sys

# ============== PAYLOAD ============== #
Main_payload = r"""
_____/\\\\\\\\\_____________________________________________________________/\\\\\\____        
 ___/\\\\\\\\\\\\\__________________________________________________________\////\\\____       
  __/\\\/////////\\\__________________/\\\______________________________________\/\\\____      
   _\/\\\_______\/\\\__/\\\\\\\\\\__/\\\\\\\\\\\__/\\/\\\\\\\___/\\\\\\\\\_______\/\\\____     
    _\/\\\\\\\\\\\\\\\_\/\\\//////__\////\\\////__\/\\\/////\\\_\////////\\\______\/\\\____    
     _\/\\\/////////\\\_\/\\\\\\\\\\____\/\\\______\/\\\___\///____/\\\\\\\\\\_____\/\\\____   
      _\/\\\_______\/\\\_\////////\\\____\/\\\_/\\__\/\\\__________/\\\/////\\\_____\/\\\____  
       _\/\\\_______\/\\\__/\\\\\\\\\\____\//\\\\\___\/\\\_________\//\\\\\\\\/\\__/\\\\\\\\\_ 
        _\///________\///__\//////////______\/////____\///___________\////////\//__\/////////__"""
Exit_payload = r"""
_____/\\\\\\\\\\\\_____________________________________/\\\_____________/\\\_____________________________________        
 ___/\\\//////////_____________________________________\/\\\____________\/\\\_____________________________________       
  __/\\\________________________________________________\/\\\____________\/\\\___________/\\\__/\\\________________      
   _\/\\\____/\\\\\\\_____/\\\\\________/\\\\\___________\/\\\____________\/\\\__________\//\\\/\\\______/\\\\\\\\__     
    _\/\\\___\/////\\\___/\\\///\\\____/\\\///\\\____/\\\\\\\\\____________\/\\\\\\\\\_____\//\\\\\_____/\\\/////\\\_    
     _\/\\\_______\/\\\__/\\\__\//\\\__/\\\__\//\\\__/\\\////\\\____________\/\\\////\\\_____\//\\\_____/\\\\\\\\\\\__   
      _\/\\\_______\/\\\_\//\\\__/\\\__\//\\\__/\\\__\/\\\__\/\\\____________\/\\\__\/\\\__/\\_/\\\_____\//\\///////___  
       _\//\\\\\\\\\\\\/___\///\\\\\/____\///\\\\\/___\//\\\\\\\/\\___________\/\\\\\\\\\__\//\\\\/_______\//\\\\\\\\\\_ 
        __\////////////_______\/////________\/////______\///////\//____________\/////////____\////__________\//////////__"""
# ============== PAYLOAD ============== #

# ========================= LIST ========================= #
categorie = ["Crypto",
        "Forensic",
        "Network",
        "Osint",
        "Pwn",
        "Reverse",
        "Stegano",
        "Web"]
# ========================= LIST ========================= #

# ================================= FUNCTION ================================= #
# ================================= FUNCTION ================================= #
# ================================= FUNCTION ================================= #
def detect_os():
    system = platform.system()
    if system == "Linux":
        print(f"[+] vérifiction de l'OS :  {system}")
    elif system == "Windows":
        print(f"[-] le tool ne fonctionne pas sur {system}")
        print(Exit_payload)
        exit()
    elif system == "Darwin":
        print(f"[-] le tool ne fonctionne pas sur {system}")
        print(Exit_payload)
        exit()
    else:
        print("[!] Votre OS n'est pas reconnu")
        print(Exit_payload)
        exit()
    return system

def absolut_path(file):
    global repo_path
    repo_path = path.dirname(path.abspath(__file__))
    return path.join(repo_path, file)

def data(tool):
    global tool_found, tool_install, tool_name, tool_categorie, tool_description, tool_path, tool_exec, section, sect # tool_tag
    tool_found = False
    for section in sect:
        if tool.lower() == section.lower():
            tool_found = True
            tool_name = Config.get(section, "name")
            tool_path = Config.get(section, "path", fallback=None)
            exec_cmd = Config.get(section, "exec")
#           tool_tag = Config.get(section, "tag")
            tool_install = Config.get(section, "install")
            tool_categorie = Config.get(section, "categorie")
            tool_description = Config.get(section, "description")
            if tool_path:
                tool_path = absolut_path(tool_path)
                tool_exec = tool_path + exec_cmd
            else:
                tool_exec = exec_cmd
            return

def exec_tool():
    print(f"[+] Tool {tool_name} selectionné")
    if tool_path != "":
        print(f"[+] Chemin du tool : {tool_path}")
    else:
        print(f"[+] Chemin du tool : {tool_exec}")
    print(f"[+] Exec de {tool_name}...")
    back = 0
    while back == 0:
        using_tool = input(f"({args.use}) > {tool_exec}")
        if using_tool in ["back", "exit"]:
            back = 1
            print(Exit_payload)
        else:
            subprocess.run((tool_exec + using_tool), shell=True)

def install_tool():
    print(f"[+] Installation de {tool_name}...")
    print(f"[+] Execution de {tool_install}...")
    subprocess.run(f"cd {repo_path}/tools/{tool_categorie} && {tool_install}", shell=True)
    if not path.exists(bin_path):
        replace = input(f"[-] Veux-tu ajouter {bin_path} ? (y/N) ")
        if replace.lower() in ["o", "y"]:
            print(f"[+] ajout de {bin_path}...")
            replace_bin = f"ln -sfv {tool_exec} $HOME/.local/bin/{tool_name}"
            subprocess.run(replace_bin, shell=True)
            print(f"[+] Fin de l'installation de {tool_name}")
# ================================= FUNCTION ================================= #
# ================================= FUNCTION ================================= #
# ================================= FUNCTION ================================= #


# ========= MAIN ========= #
print(Main_payload)
# ========= MAIN ========= #


# =================== ARGS CONF =================== #
parser = argparse.ArgumentParser()
parser.add_argument('-s', '--search', dest='search', default=None, help="Search tool by name")
#parser.add_argument('-t', '--tag', dest='tag', default=None, help="Search tool by tag")
parser.add_argument('-i', '--install', dest='install', default=None, help='Install the tool')
parser.add_argument('-l', '--list', dest='list', default=None, help='List all tools')
parser.add_argument('-u', '--use', dest='use', default=None, help='Use the selected tool')
parser.add_argument('-c', '--categorie', dest='categorie', default=None, help='Option used for list tool by categorie')
parser.add_argument('-p', '--personalize', dest='personnalize', required=False, help='create and personnalize a tool, or modify a tool existing in lists.ini')
args = parser.parse_args()
# =================== ARGS CONF =================== #

# =================== DATA CONF =================== #
config_file = absolut_path("lists.ini")
Config = configparser.ConfigParser()
Config.read(config_file)
sect = Config.sections()
rawconfig = configparser.RawConfigParser()
# =================== DATA CONF =================== #

# ================== INIT VARIABLE ================== #
tool_found = False
# ================== INIT VARIABLE ================== #

print(f"[+] Initialisation du path {repo_path}...")
if path.exists(f"{repo_path}/lists.ini"):
    print(f"[+] Chargement du fichier d'initialisation des tools {repo_path}/lists.ini...")
else:
    print(f"[!] Erreur du chargement du fichier d'initialisation des tools {repo_path}/lists.ini...")

os = detect_os()

if not args.list and not args.install and not args.search and not args.use and not args.categorie and not args.personnalize: #and not args.tag
    print(f"[!] Merci de bien vouloir utiliser une option")
    print("""
usage: main.py [-h] [-s SEARCH] [-i INSTALL] [-l LIST] [-u USE] [-c CATEGORIE]
               [-p PERSONNALIZE]

optional arguments:
  -h, --help            show this help message and exit
  -s SEARCH, --search SEARCH
                        Search tool by name
  -i INSTALL, --install INSTALL
                        Install the tool
  -l LIST, --list LIST  List all tools
  -u USE, --use USE     Use the selected tool
  -c CATEGORIE, --categorie CATEGORIE
                        Option used for list tool by categorie
  -p PERSONNALIZE, --personalize PERSONNALIZE
                        create and personnalize a tool, or modify a tool
                        existing in lists.ini
""")
# ================================================ OPTIONS ================================================ #
# ================================================ OPTIONS ================================================ #
# ================================================ OPTIONS ================================================ #

# ================ PERSONNALIZE ================ #

if args.personnalize:
        print(f"[+] personnalisation de {repo_path}/lists.ini")
        data(args.personnalize)
        if tool_found:
            print(f"[+] {section}\n\t description : {tool_description}")
            print(f"[+] edite du tool {args.personnalize}")
            modif = input(f" ({args.personnalize}) > ")
            rawconfig.set(section, "name", modif)
        else:
            print(f"[!] tool {args.personnalize} non trouvé")
            create_tool = input("voulez vous creer un nouveau tool ? (y/N)")
            if create_tool.lower() in ["o", "y"]:
                print(f"[+] creation du tool {args.personnalize}")
                #rawconfig.add_section(args.personnalize)
                #finish that
            else:
                print(f"[!] Exit de la personalisation")
                        
# ================ PERSONNALIZE ================ #


# ================ CATEGORIE ================ #
if args.categorie:
        print(f"[+] List de la categorie : {args.categorie}\n")
        categorie_found = False
        for section in sect:
            data(section)
            if args.categorie.lower() == tool_categorie.lower():
                print(f"[+] {section}\n {tool_description}")
                categorie_found = True
        if not categorie_found:
                print("[-] Aucune catégorie trouvée")
                for i in range (len(categorie)): print(f"[{i}] {categorie[i]}")
# ================ CATEGORIE ================ #


# ================ SEARCH ================ #
if args.search:
    print(f"[+] Recherche de : {args.search}\n")
    for section in sect:
        if args.search.lower() in section.lower():
            data(section)
            print(f"[+] {section}\n {tool_description}")
            tool_found = True
    if not tool_found:
        print("[-] Aucun tool trouvé")
# ================ SEARCH ================ #


# ================ USE ================ #
if args.use:
    data(args.use)

    if tool_found:
        if tool_path:
            if path.exists(tool_path):
                chdir(tool_path)
                exec_tool()
            else:
                print(f"[-] Chemin introuvable")
                install = input(f"[-] Veux-tu installer {tool_name} ? (y/N) ")
                if install.lower() in ["o", "y"]:
                    args.install = args.use
        else:
            exec_tool()
    else:
        print(f"[-] Tool {args.use} non trouvé")
        print(f"[-] Suggestion possible :")
        for section in sect:
            if args.use.lower() in section.lower():
                data(section)
                print(f"[+] {section}\n\tdescription : {tool_description}")
        if not tool_found:
            print(f"[-] Pas de suggestion")
# ================ USE ================ #


# ================ INSTALL ================ #
if args.install:
    data(args.install)

    if tool_found:
        bin_path = f"/usr/bin/{tool_name}"
        
        if path.exists(bin_path):
            print(f"[!] {tool_name} est déjà installé à {bin_path}")
            install = input("[?] Voulez-vous vraiment l'installer ? (y/N) ")
            if install.lower() in ["o", "y"]:
                install_tool()
            else:
                print(f"[+] Annulation de l'installation de {tool_name}")
                print(f"[+] Tool déjà existant à {bin_path}")
                #subprocess.run(tool_name, shell=True)
        else:
            install_tool()
        
    else:
        print(f"[-] Tool {args.install} pas trouvé")
# ================ INSTALL ================ #

# ================ LIST ================ #
if args.list:
    print(f"[+] Liste de {args.list} :")
    for section in sect:
        data(section)
        print(f"[+] {section}\n\tdescription : {tool_description}")
# ================ LIST FUNCTION ================ #

# ================ TAG FUNCTION ================ #
#if args.tag:
#    print("[+] Recherche tag des tools :")
#    for section in sect:
#        if tool_tag == args.tag:
#            print(f"[+] {section}\ndescription : {tool_description}")
# ================ TAG FUNCTION ================ #

# ================================================ OPTIONS ================================================ #
# ================================================ OPTIONS ================================================ #
# ================================================ OPTIONS ================================================ #