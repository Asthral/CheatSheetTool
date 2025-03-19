import configparser
import argparse
import subprocess
import base64
import socket
import re
import time
import os
import readline
import platform
import subprocess
import sys


#==============PAYLOAD==============#
Main_base64 = "X19fX18vXFxcXFxcXFxcX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fXy9cXFxcXFxfX19fICAgICAgICAKIF9fXy9cXFxcXFxcXFxcXFxcX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX1wvLy8vXFxcX19fXyAgICAgICAKICBfXy9cXFwvLy8vLy8vLy9cXFxfX19fX19fX19fX19fX19fX18vXFxcX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19cL1xcXF9fX18gICAgICAKICAgX1wvXFxcX19fX19fX1wvXFxcX18vXFxcXFxcXFxcXF9fL1xcXFxcXFxcXFxcX18vXFwvXFxcXFxcXF9fXy9cXFxcXFxcXFxfX19fX19fXC9cXFxfX19fICAgICAKICAgIF9cL1xcXFxcXFxcXFxcXFxcXF9cL1xcXC8vLy8vL19fXC8vLy9cXFwvLy8vX19cL1xcXC8vLy8vXFxcX1wvLy8vLy8vL1xcXF9fX19fX1wvXFxcX19fXyAgICAKICAgICBfXC9cXFwvLy8vLy8vLy9cXFxfXC9cXFxcXFxcXFxcX19fX1wvXFxcX19fX19fXC9cXFxfX19cLy8vX19fXy9cXFxcXFxcXFxcX19fX19cL1xcXF9fX18gICAKICAgICAgX1wvXFxcX19fX19fX1wvXFxcX1wvLy8vLy8vL1xcXF9fX19cL1xcXF8vXFxfX1wvXFxcX19fX19fX19fXy9cXFwvLy8vL1xcXF9fX19fXC9cXFxfX19fICAKICAgICAgIF9cL1xcXF9fX19fX19cL1xcXF9fL1xcXFxcXFxcXFxfX19fXC8vXFxcXFxfX19cL1xcXF9fX19fX19fX1wvL1xcXFxcXFxcL1xcX18vXFxcXFxcXFxcXyAKICAgICAgICBfXC8vL19fX19fX19fXC8vL19fXC8vLy8vLy8vLy9fX19fX19cLy8vLy9fX19fXC8vL19fX19fX19fX19fXC8vLy8vLy8vXC8vX19cLy8vLy8vLy8vX18="
Main_payload = base64.b64decode(Main_base64).decode()
Forensic_base64 = "X18vXFxcXFxcXFxcXFxcXFxcX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fXyAgICAgICAgCiBfXC9cXFwvLy8vLy8vLy8vL19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fICAgICAgIAogIF9cL1xcXF9fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fXy9cXFxfX19fX19fX19fX19fX18gICAgICAKICAgX1wvXFxcXFxcXFxcXFxfX19fX19fX18vXFxcXFxfX19fXy9cXC9cXFxcXFxcX19fX19fL1xcXFxcXFxcX19fL1xcL1xcXFxcXF9fX18vXFxcXFxcXFxcXF9cLy8vX19fX19fL1xcXFxcXFxcXyAgICAgCiAgICBfXC9cXFwvLy8vLy8vX19fX19fX18vXFxcLy8vXFxcX19cL1xcXC8vLy8vXFxcX19fL1xcXC8vLy8vXFxcX1wvXFxcLy8vL1xcXF9fXC9cXFwvLy8vLy9fX18vXFxcX19fL1xcXC8vLy8vL19fICAgIAogICAgIF9cL1xcXF9fX19fX19fX19fX19fL1xcXF9fXC8vXFxcX1wvXFxcX19fXC8vL19fXy9cXFxcXFxcXFxcXF9fXC9cXFxfX1wvL1xcXF9cL1xcXFxcXFxcXFxfXC9cXFxfXy9cXFxfX19fX19fX18gICAKICAgICAgX1wvXFxcX19fX19fX19fX19fX1wvL1xcXF9fL1xcXF9fXC9cXFxfX19fX19fX19cLy9cXC8vLy8vLy9fX19cL1xcXF9fX1wvXFxcX1wvLy8vLy8vL1xcXF9cL1xcXF9cLy9cXFxfX19fX19fXyAgCiAgICAgICBfXC9cXFxfX19fX19fX19fX19fX1wvLy9cXFxcXC9fX19cL1xcXF9fX19fX19fX19cLy9cXFxcXFxcXFxcX1wvXFxcX19fXC9cXFxfXy9cXFxcXFxcXFxcX1wvXFxcX19cLy8vXFxcXFxcXFxfIAogICAgICAgIF9cLy8vX19fX19fX19fX19fX19fX19cLy8vLy9fX19fX1wvLy9fX19fX19fX19fX19cLy8vLy8vLy8vL19fXC8vL19fX19cLy8vX19cLy8vLy8vLy8vL19fXC8vL19fX19fXC8vLy8vLy8vX18="
Forensic_paylaod = base64.b64decode(Forensic_base64).decode()
Web_base64 = "X18vXFxcX19fX19fX19fX19fX18vXFxcX19fX19fX19fX19fX19fX18vXFxcX19fX19fX18gICAgICAgIAogX1wvXFxcX19fX19fX19fX19fX1wvXFxcX19fX19fX19fX19fX19fX1wvXFxcX19fX19fX18gICAgICAgCiAgX1wvXFxcX19fX19fX19fX19fX1wvXFxcX19fX19fX19fX19fX19fX1wvXFxcX19fX19fX18gICAgICAKICAgX1wvL1xcXF9fX18vXFxcX19fXy9cXFxfX19fX18vXFxcXFxcXFxfX1wvXFxcX19fX19fX18gICAgIAogICAgX19cLy9cXFxfXy9cXFxcXF9fL1xcXF9fX19fL1xcXC8vLy8vXFxcX1wvXFxcXFxcXFxcX18gICAgCiAgICAgX19fXC8vXFxcL1xcXC9cXFwvXFxcX19fX18vXFxcXFxcXFxcXFxfX1wvXFxcLy8vL1xcXF8gICAKICAgICAgX19fX1wvL1xcXFxcXC8vXFxcXFxfX19fX1wvL1xcLy8vLy8vL19fX1wvXFxcX19cL1xcXF8gIAogICAgICAgX19fX19cLy9cXFxfX1wvL1xcXF9fX19fX19cLy9cXFxcXFxcXFxcX1wvXFxcXFxcXFxcX18gCiAgICAgICAgX19fX19fXC8vL19fX19cLy8vX19fX19fX19fXC8vLy8vLy8vLy9fX1wvLy8vLy8vLy9fX18="
Web_paylaod = base64.b64decode(Web_base64).decode()
Pwn_base64 = "X18vXFxcXFxcXFxcXFxcXF9fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fICAgICAgICAKIF9cL1xcXC8vLy8vLy8vL1xcXF9fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fXyAgICAgICAKICBfXC9cXFxfX19fX19fXC9cXFxfX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX18gICAgICAKICAgX1wvXFxcXFxcXFxcXFxcXC9fX18vXFxfX19fL1xcX19fL1xcX18vXFwvXFxcXFxcX19fICAgICAKICAgIF9cL1xcXC8vLy8vLy8vL19fX19cL1xcXF9fL1xcXFxfL1xcXF9cL1xcXC8vLy9cXFxfXyAgICAKICAgICBfXC9cXFxfX19fX19fX19fX19fXC8vXFxcL1xcXFxcL1xcXF9fXC9cXFxfX1wvL1xcXF8gICAKICAgICAgX1wvXFxcX19fX19fX19fX19fX19cLy9cXFxcXC9cXFxcXF9fX1wvXFxcX19fXC9cXFxfICAKICAgICAgIF9cL1xcXF9fX19fX19fX19fX19fX1wvL1xcXFwvL1xcXF9fX19cL1xcXF9fX1wvXFxcXyAKICAgICAgICBfXC8vL19fX19fX19fX19fX19fX19fXC8vL19fXC8vL19fX19fXC8vL19fX19cLy8vX18="
Pwn_paylaod = base64.b64decode(Pwn_base64).decode()
Stegano_base64 = "X19fX18vXFxcXFxcXFxcXFxfX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fICAgICAgICAKIF9fXy9cXFwvLy8vLy8vLy9cXFxfX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fXyAgICAgICAKICBfX1wvL1xcXF9fX19fX1wvLy9fX19fX18vXFxcX19fX19fX19fX19fX19fX19fX19fX18vXFxcXFxcXFxfX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX18gICAgICAKICAgX19fXC8vLy9cXFxfX19fX19fX19fL1xcXFxcXFxcXFxcX19fX18vXFxcXFxcXFxfX18vXFxcLy8vL1xcXF9fL1xcXFxcXFxcXF9fX19fL1xcL1xcXFxcXF9fX19fX18vXFxcXFxfX19fICAgICAKICAgIF9fX19fX1wvLy8vXFxcX19fX19fXC8vLy9cXFwvLy8vX19fXy9cXFwvLy8vL1xcXF9cLy9cXFxcXFxcXFxfXC8vLy8vLy8vXFxcX19fXC9cXFwvLy8vXFxcX19fXy9cXFwvLy9cXFxfXyAgICAKICAgICBfX19fX19fX19cLy8vL1xcXF9fX19fX1wvXFxcX19fX19fXy9cXFxcXFxcXFxcXF9fX1wvLy8vLy8vXFxcX19fL1xcXFxcXFxcXFxfX1wvXFxcX19cLy9cXFxfXy9cXFxfX1wvL1xcXF8gICAKICAgICAgX18vXFxcX19fX19fXC8vXFxcX19fX19cL1xcXF8vXFxfX1wvL1xcLy8vLy8vL19fX18vXFxfX19fX1xcXF9fL1xcXC8vLy8vXFxcX19cL1xcXF9fX1wvXFxcX1wvL1xcXF9fL1xcXF9fICAKICAgICAgIF9cLy8vXFxcXFxcXFxcXFwvX19fX19fXC8vXFxcXFxfX19fXC8vXFxcXFxcXFxcXF9cLy9cXFxcXFxcXF9fXC8vXFxcXFxcXFwvXFxfXC9cXFxfX19cL1xcXF9fXC8vL1xcXFxcL19fXyAKICAgICAgICBfX19cLy8vLy8vLy8vLy9fX19fX19fX19cLy8vLy9fX19fX19cLy8vLy8vLy8vL19fX1wvLy8vLy8vL19fX19cLy8vLy8vLy9cLy9fX1wvLy9fX19fXC8vL19fX19fXC8vLy8vX19fX18="
Stegano_paylaod = base64.b64decode(Stegano_base64).decode()
Reverse_base64 = "X19fXy9cXFxcXFxcXFxfX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fICAgICAgICAKIF9fL1xcXC8vLy8vLy9cXFxfX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fXyAgICAgICAKICBfXC9cXFxfX19fX1wvXFxcX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX18gICAgICAKICAgX1wvXFxcXFxcXFxcXFwvX19fX19fX18vXFxcXFxcXFxfX18vXFxcX19fXy9cXFxfX19fXy9cXFxcXFxcXF9fXy9cXC9cXFxcXFxcX19fL1xcXFxcXFxcXFxfX19fXy9cXFxcXFxcXF9fICAgICAKICAgIF9cL1xcXC8vLy8vL1xcXF9fX19fXy9cXFwvLy8vL1xcXF9cLy9cXFxfXy9cXFxfX19fL1xcXC8vLy8vXFxcX1wvXFxcLy8vLy9cXFxfXC9cXFwvLy8vLy9fX19fL1xcXC8vLy8vXFxcXyAgICAKICAgICBfXC9cXFxfX19fXC8vXFxcX19fXy9cXFxcXFxcXFxcXF9fX1wvL1xcXC9cXFxfX19fL1xcXFxcXFxcXFxcX19cL1xcXF9fX1wvLy9fX1wvXFxcXFxcXFxcXF9fL1xcXFxcXFxcXFxcX18gICAKICAgICAgX1wvXFxcX19fX19cLy9cXFxfX1wvL1xcLy8vLy8vL19fX19fXC8vXFxcXFxfX19fXC8vXFwvLy8vLy8vX19fXC9cXFxfX19fX19fX19cLy8vLy8vLy9cXFxfXC8vXFwvLy8vLy8vX19fICAKICAgICAgIF9cL1xcXF9fX19fX1wvL1xcXF9fXC8vXFxcXFxcXFxcXF9fX19cLy9cXFxfX19fX19cLy9cXFxcXFxcXFxcX1wvXFxcX19fX19fX19fXy9cXFxcXFxcXFxcX19cLy9cXFxcXFxcXFxcXyAKICAgICAgICBfXC8vL19fX19fX19fXC8vL19fX19cLy8vLy8vLy8vL19fX19fX1wvLy9fX19fX19fX1wvLy8vLy8vLy8vX19cLy8vX19fX19fX19fX1wvLy8vLy8vLy8vX19fX1wvLy8vLy8vLy8vX18="
Reverse_paylaod = base64.b64decode(Reverse_base64).decode()
Network_base64 = "X18vXFxcXFxfX19fXy9cXFxfX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX18gICAgICAgIAogX1wvXFxcXFxcX19fXC9cXFxfX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fXy9cXFxfX19fX19fX18gICAgICAgCiAgX1wvXFxcL1xcXF9fXC9cXFxfX19fX19fX19fX19fX19fX19fXy9cXFxfX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fXC9cXFxfX19fX19fX18gICAgICAKICAgX1wvXFxcLy9cXFxfXC9cXFxfX19fXy9cXFxcXFxcXF9fXy9cXFxcXFxcXFxcXF9fL1xcX19fXy9cXF9fXy9cXF9fX19fL1xcXFxcX19fX18vXFwvXFxcXFxcXF9fXC9cXFxcXFxcXF9fX18gICAgIAogICAgX1wvXFxcXC8vXFxcXC9cXFxfX18vXFxcLy8vLy9cXFxfXC8vLy9cXFwvLy8vX19cL1xcXF9fL1xcXFxfL1xcXF9fXy9cXFwvLy9cXFxfX1wvXFxcLy8vLy9cXFxfXC9cXFwvLy8vXFxcX18gICAgCiAgICAgX1wvXFxcX1wvL1xcXC9cXFxfXy9cXFxcXFxcXFxcXF9fX19fXC9cXFxfX19fX19cLy9cXFwvXFxcXFwvXFxcX19fL1xcXF9fXC8vXFxcX1wvXFxcX19fXC8vL19fXC9cXFxcXFxcXC9fX18gICAKICAgICAgX1wvXFxcX19cLy9cXFxcXFxfXC8vXFwvLy8vLy8vX19fX19fXC9cXFxfL1xcX19fXC8vXFxcXFwvXFxcXFxfX19cLy9cXFxfXy9cXFxfX1wvXFxcX19fX19fX19fXC9cXFwvLy9cXFxfX18gIAogICAgICAgX1wvXFxcX19fXC8vXFxcXFxfX1wvL1xcXFxcXFxcXFxfX19fXC8vXFxcXFxfX19fX1wvL1xcXFwvL1xcXF9fX19fXC8vL1xcXFxcL19fX1wvXFxcX19fX19fX19fXC9cXFxfXC8vL1xcXF8gCiAgICAgICAgX1wvLy9fX19fX1wvLy8vL19fX19cLy8vLy8vLy8vL19fX19fX1wvLy8vL19fX19fX19cLy8vX19cLy8vX19fX19fX19cLy8vLy9fX19fX1wvLy9fX19fX19fX19fXC8vL19fX19cLy8vX18="
Network_paylaod = base64.b64decode(Network_base64).decode()
Crypto_base64 = "X19fX19fX18vXFxcXFxcXFxcX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX18gICAgICAgIAogX19fX18vXFxcLy8vLy8vLy9fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX18gICAgICAgCiAgX19fL1xcXC9fX19fX19fX19fX19fX19fX19fX19fX19fX19fL1xcXF9fL1xcXF9fXy9cXFxcXFxcXFxfX19fX18vXFxcX19fX19fX19fX19fX19fX19fX18gICAgICAKICAgX18vXFxcX19fX19fX19fX19fX18vXFwvXFxcXFxcXF9fX19cLy9cXFwvXFxcX19fL1xcXC8vLy8vXFxcX18vXFxcXFxcXFxcXFxfX19fXy9cXFxcXF9fX18gICAgIAogICAgX1wvXFxcX19fX19fX19fX19fX1wvXFxcLy8vLy9cXFxfX19fXC8vXFxcXFxfX19cL1xcXFxcXFxcXFxfX1wvLy8vXFxcLy8vL19fX18vXFxcLy8vXFxcX18gICAgCiAgICAgX1wvL1xcXF9fX19fX19fX19fX1wvXFxcX19fXC8vL19fX19fX1wvL1xcXF9fX19cL1xcXC8vLy8vL19fX19fX1wvXFxcX19fX19fXy9cXFxfX1wvL1xcXF8gICAKICAgICAgX19cLy8vXFxcX19fX19fX19fX1wvXFxcX19fX19fX19fXy9cXF8vXFxcX19fX19cL1xcXF9fX19fX19fX19fX1wvXFxcXy9cXF9fXC8vXFxcX18vXFxcX18gIAogICAgICAgX19fX1wvLy8vXFxcXFxcXFxcX1wvXFxcX19fX19fX19fXC8vXFxcXC9fX19fX19cL1xcXF9fX19fX19fX19fX1wvL1xcXFxcX19fX1wvLy9cXFxcXC9fX18gCiAgICAgICAgX19fX19fX1wvLy8vLy8vLy9fX1wvLy9fX19fX19fX19fX1wvLy8vX19fX19fX19cLy8vX19fX19fX19fX19fX19cLy8vLy9fX19fX19fXC8vLy8vX19fX18="
Crypto_paylaod = base64.b64decode(Crypto_base64).decode()
Osint_base64 = "X19fX19fXy9cXFxcXF9fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fICAgICAgICAKIF9fX19fL1xcXC8vL1xcXF9fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fXyAgICAgICAKICBfX18vXFxcL19fXC8vL1xcXF9fX19fX19fX19fX19fX18vXFxcX19fX19fX19fX19fX19fX19fXy9cXFxfX19fX18gICAgICAKICAgX18vXFxcX19fX19fXC8vXFxcX18vXFxcXFxcXFxcXF9cLy8vX19fL1xcL1xcXFxcXF9fX18vXFxcXFxcXFxcXFxfICAgICAKICAgIF9cL1xcXF9fX19fX19cL1xcXF9cL1xcXC8vLy8vL19fXy9cXFxfXC9cXFwvLy8vXFxcX19cLy8vL1xcXC8vLy9fXyAgICAKICAgICBfXC8vXFxcX19fX19fL1xcXF9fXC9cXFxcXFxcXFxcX1wvXFxcX1wvXFxcX19cLy9cXFxfX19fXC9cXFxfX19fX18gICAKICAgICAgX19cLy8vXFxcX18vXFxcX19fX1wvLy8vLy8vL1xcXF9cL1xcXF9cL1xcXF9fX1wvXFxcX19fX1wvXFxcXy9cXF9fICAKICAgICAgIF9fX19cLy8vXFxcXFwvX19fX19fL1xcXFxcXFxcXFxfXC9cXFxfXC9cXFxfX19cL1xcXF9fX19cLy9cXFxcXF9fXyAKICAgICAgICBfX19fX19cLy8vLy9fX19fX19fXC8vLy8vLy8vLy9fX1wvLy9fX1wvLy9fX19fXC8vL19fX19fX1wvLy8vL19fX18="
Osint_paylaod = base64.b64decode(Osint_base64).decode()
Other_base64 = "X19fX19fXy9cXFxcXF9fX19fX19fX19fX19fX19fX19fXy9cXFxfX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fXyAgICAgICAgCiBfX19fXy9cXFwvLy9cXFxfX19fX19fX19fX19fX19fX19cL1xcXF9fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fICAgICAgIAogIF9fXy9cXFwvX19cLy8vXFxcX19fX19fL1xcXF9fX19fX1wvXFxcX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX18gICAgICAKICAgX18vXFxcX19fX19fXC8vXFxcX18vXFxcXFxcXFxcXFxfXC9cXFxfX19fX19fX19fX19fL1xcXFxcXFxcX19fL1xcL1xcXFxcXFxfXyAgICAgCiAgICBfXC9cXFxfX19fX19fXC9cXFxfXC8vLy9cXFwvLy8vX19cL1xcXFxcXFxcXFxfX19fL1xcXC8vLy8vXFxcX1wvXFxcLy8vLy9cXFxfICAgIAogICAgIF9cLy9cXFxfX19fX18vXFxcX19fX19cL1xcXF9fX19fX1wvXFxcLy8vLy9cXFxfXy9cXFxcXFxcXFxcXF9fXC9cXFxfX19cLy8vX18gICAKICAgICAgX19cLy8vXFxcX18vXFxcX19fX19fX1wvXFxcXy9cXF9fXC9cXFxfX19cL1xcXF9cLy9cXC8vLy8vLy9fX19cL1xcXF9fX19fX19fXyAgCiAgICAgICBfX19fXC8vL1xcXFxcL19fX19fX19fXC8vXFxcXFxfX19cL1xcXF9fX1wvXFxcX19cLy9cXFxcXFxcXFxcX1wvXFxcX19fX19fX19fIAogICAgICAgIF9fX19fX1wvLy8vL19fX19fX19fX19fXC8vLy8vX19fX1wvLy9fX19fXC8vL19fX19cLy8vLy8vLy8vL19fXC8vL19fX19fX19fX18="
Other_paylaod = base64.b64decode(Other_base64).decode()
Exit_base64 = "X19fX18vXFxcXFxcXFxcXFxcX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fXy9cXFxfX19fX19fX19fX19fL1xcXF9fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX18gICAgICAgIAogX19fL1xcXC8vLy8vLy8vLy9fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fXC9cXFxfX19fX19fX19fX19cL1xcXF9fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX18gICAgICAgCiAgX18vXFxcX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fXC9cXFxfX19fX19fX19fX19cL1xcXF9fX19fX19fX19fL1xcXF9fL1xcXF9fX19fX19fX19fX19fX18gICAgICAKICAgX1wvXFxcX19fXy9cXFxcXFxcX19fX18vXFxcXFxfX19fX19fXy9cXFxcXF9fX19fX19fX19fXC9cXFxfX19fX19fX19fX19cL1xcXF9fX19fX19fX19cLy9cXFwvXFxcX19fX19fL1xcXFxcXFxcX18gICAgIAogICAgX1wvXFxcX19fXC8vLy8vXFxcX19fL1xcXC8vL1xcXF9fX18vXFxcLy8vXFxcX19fXy9cXFxcXFxcXFxfX19fX19fX19fX19cL1xcXFxcXFxcXF9fX19fXC8vXFxcXFxfX19fXy9cXFwvLy8vL1xcXF8gICAgCiAgICAgX1wvXFxcX19fX19fX1wvXFxcX18vXFxcX19cLy9cXFxfXy9cXFxfX1wvL1xcXF9fL1xcXC8vLy9cXFxfX19fX19fX19fX19cL1xcXC8vLy9cXFxfX19fX1wvL1xcXF9fX19fL1xcXFxcXFxcXFxcX18gICAKICAgICAgX1wvXFxcX19fX19fX1wvXFxcX1wvL1xcXF9fL1xcXF9fXC8vXFxcX18vXFxcX19cL1xcXF9fXC9cXFxfX19fX19fX19fX19cL1xcXF9fXC9cXFxfXy9cXF8vXFxcX19fX19cLy9cXC8vLy8vLy9fX18gIAogICAgICAgX1wvL1xcXFxcXFxcXFxcXC9fX19cLy8vXFxcXFwvX19fX1wvLy9cXFxcXC9fX19cLy9cXFxcXFxcL1xcX19fX19fX19fX19cL1xcXFxcXFxcXF9fXC8vXFxcXC9fX19fX19fXC8vXFxcXFxcXFxcXF8gCiAgICAgICAgX19cLy8vLy8vLy8vLy8vX19fX19fX1wvLy8vL19fX19fX19fXC8vLy8vX19fX19fXC8vLy8vLy9cLy9fX19fX19fX19fX19cLy8vLy8vLy8vX19fX1wvLy8vX19fX19fX19fX1wvLy8vLy8vLy8vX18="
Exit_paylaod = base64.b64decode(Exit_base64).decode()
#==============PAYLOAD==============#

#=========================LIST=========================#

        
# =================== FUNCTION =================== #
#fonction by chatgpt
def detect_and_install(package):
    system = platform.system()
    
    if system == "Linux":
        try:
            cmd = "sudo apt install -y" + package
            subprocess.run(cmd, check=True)
        except Exception as e:
            print(f"[!] Erreur lors de l'installation : {e}")
            sys.exit(1)
    
    elif system == "Windows":
        print("[!] Ce programme ne supporte pas Windows. Fermeture.")
        sys.exit(1)
    
    elif system == "Darwin":
        print("[!] Ce programme ne supporte pas macOS. Fermeture.")
        sys.exit(1)
    
    else:
        print("Système d'exploitation non reconnu.")
        sys.exit(1)

def path(file):
    global repo_path
    repo_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(repo_path, file)

def data(tool):
    global tool_found, tool_install, tool_name, tool_categorie, tool_description, tool_path, tool_exec, tool_tag
    tool_found = False
    for section in sect:
        if tool == section:
            tool_found = True
            tool_name = Config.get(section, "name")
            tool_path = Config.get(section, "path", fallback=None)
            exec_cmd = Config.get(section, "exec")
#            tool_tag = Config.get(section, "tag")
            tool_install = Config.get(section, "install")
            tool_categorie = Config.get(section, "categorie")
            tool_description = Config.get(section, "description")
            if tool_path:
                tool_path = path(tool_path)
                tool_exec = tool_path + '/' + exec_cmd
            else:
                tool_exec = exec_cmd
            return
# =================== FUNCTION =================== #


# ========= MAIN ========= #
print(f"{Main_payload}\n")
# ========= MAIN ========= #


# =================== ARGS CONF =================== #
parser = argparse.ArgumentParser()
parser.add_argument('-s', '--search', dest='search', default=None, help="Search tool by name")
#parser.add_argument('-t', '--tag', dest='tag', default=None, help="Search tool by tag")
parser.add_argument('-i', '--install', dest='install', default=None, help='Install the tool')
parser.add_argument('-l', '--list', dest='list', default=None, help='List all tools')
parser.add_argument('-u', '--use', dest='use', default=None, help='Use the selected tool')
args = parser.parse_args()
# =================== ARGS CONF =================== #

# =================== DATA CONF =================== #
config_file = path("lists.ini")
Config = configparser.ConfigParser()
Config.read(config_file)
sect = Config.sections()
# =================== DATA CONF =================== #

# ================== INIT VARIABLE ================== #
tool_found = False
# ================== INIT VARIABLE ================== #

print(f"[+] Initialisation du path {repo_path}...")
if os.path.exists(f"{repo_path}/lists.ini"):
    print(f"[+] Chargement du fichier d'initialisation des tools {repo_path}/lists.ini...")
else:
    print(f"[!] Erreur du chargement du fichier d'initialisation des tools {repo_path}/lists.ini...")

if not args.list and not args.install and not args.tag and not args.search and not args.use:
    print(f"[!] Merci de bien vouloir utiliser une option")
    print("""
usage: main.py [-h] [-s SEARCH] [-t TAG] [-i INSTALL] [-l LIST] [-u USE]

optional arguments:
  -h, --help            show this help message and exit
  -s SEARCH, --search SEARCH
                        Search tool by name
  -i INSTALL, --install INSTALL
                        Install the tool
  -l LIST, --list LIST  List all tools
  -u USE, --use USE     Use the selected tool
""")


# ================================================ OPTIONS ================================================ #
# ================================================ OPTIONS ================================================ #
# ================================================ OPTIONS ================================================ #

# ================ SEARCH ================ #
if args.search:
    print(f"[+] Recherche de : {args.search}\n")
    tool_found = False
    for section in sect:
        if args.search.lower() in section.lower():
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
            print(f"[+] Tool {tool_name} selectionné")
            print(f"[+] Chemin du tool : {tool_path}")        
            if os.path.exists(tool_path):
                print(f"[+] Exec de {tool_name}...")
                os.chdir(tool_path)
                print(tool_exec)
                subprocess.run(tool_exec, shell=True)
            else:
                print(f"[-] Chemin introuvable")
                install = input(f"[-] Veux-tu installer {tool_name} ? (y/N) ")
                if install.lower() in ["o", "y"]:
                    args.install = args.use
        else:
            print(f"[+] Tool {tool_name} selectionné")
            print(f"[+] Exec de {tool_name}...")
            print(tool_exec)
            subprocess.run(tool_exec, shell=True)
    else:
        print(f"[-] Tool {args.use} non trouvé")
        print(f"[-] Suggestion :")
        tool_found = False
        for section in sect:
            if args.use.lower() in section.lower():
                print(f"[+] {section}\ndescription : {tool_description}")
                tool_found = True
# ================ USE ================ #

# ================ INSTALL ================ #
if args.install:
    data(args.install)

    if tool_found:
        bin_path = f"/usr/bin/{tool_name}"
        
        if os.path.exists(bin_path):
            print(f"[!] {tool_name} est déjà installé à {bin_path}")
            install = input("[?] Voulez-vous vraiment l'installer ? (y/N) ")
            if install.lower() in ["o", "y"]:
                print(f"[+] Installation de {tool_name}...")
                print(f"[+] Execution de {tool_install}...")
                subprocess.run(tool_install, shell=True)
                replace = input(f"[-] Veux-tu remplacer {bin_path} ? (y/N) ")
                if replace.lower() in ["o", "y"]:
                    print(f"[+] Remplacement de {bin_path}...")
                    replace_bin = f"sudo ln -sfv {tool_exec} /usr/bin/{tool_name}"
                    subprocess.run(replace_bin, shell=True)
                    print(f"[+] Fin de l'installation de {tool_name}")
            else:
                print(f"[+] Annulation de l'installation de {tool_name}")
                print(f"[+] Tool déjà existant à {bin_path}")
                #subprocess.run(tool_name, shell=True)
        else:
            print(f"[+] Installation de {tool_name}...")
            print(f"[+] Execution de {tool_install}...")
            subprocess.run(f"cd {repo_path}/tools/{tool_categorie} && {tool_install}", shell=True)
        
    else:
        print(f"[-] Tool {args.install} pas trouvé")
# ================ INSTALL ================ #

# ================ LIST ================ #
if args.list:
    print(f"[+] Liste de {args.list} :")
    for section in sect:
        print(f"[+] {section}\ndescription : {tool_description}")
# ================ LIST FUNCTION ================ #

# ================ TAG FUNCTION ================ #
#if args.tag:
#    print("[+] Recherche tag des tools :")
#    for section in sect:
#        if (tool_tag) == args.tag:
#            print(f"[+] {section}\ndescription : {tool_description}")
# ================ TAG FUNCTION ================ #

# ================================================ OPTIONS ================================================ #
# ================================================ OPTIONS ================================================ #
# ================================================ OPTIONS ================================================ #
