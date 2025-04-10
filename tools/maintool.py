import base64
import socket
import re
import argparse
import time
import os
import readline

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
payload = [Exit_paylaod, 
           Crypto_paylaod, 
           Forensic_paylaod, 
           Network_paylaod, 
           Osint_paylaod, 
           Pwn_paylaod, 
           Reverse_paylaod, 
           Stegano_paylaod, 
           Web_paylaod, 
           Other_paylaod]

categorie = ["Exit",
        "Crypto",
        "Forensic",
        "Network",
        "Osint",
        "Pwn",
        "Reverse",
        "Stegano",
        "Web",
        "Other"]

choice = ["Back",
        "Tools",
        "Install",
        "Link",
        "Search"]

#================CRYPTO TOOLS================#
haiti = ["haiti", "sudo gem install haiti"]
john = ["john", "sudo apt install john"]
hashcat = ["hashcat", "sudo apt install hashcat"]
zip2john = ["zip2john", "sudo apt install john"]
#================FORENSIC TOOLS================#
autopsy = ["autopsy"]
binwalk = ["binwalk"]
volatility2 = ["volatility2"]
volatility3 = ["volatility3"]
crit = ["crit"]
volshell = ["volshell"]
photorec = ["photorec"]
#================NETWORK TOOLS================#
wireshark = ["wireshark", "sudo apt install wireshark"]
tshark = ["tshark", "sudo apt install tshark"]
hydra = ["hydra", "sudo apt install hydra"]
scapy = ["scapy", "sudo apt install scapy"]
radsniff = ["radsniff"]
ettercap = ["ettercap"]
#================OSINT TOOLS================#
blackbird = ["blackbird", "git clone https://github.com/p1ngul1n0/blackbird.git && cd blackbird && pipx -r requirements.txt && sudo ln -sfv /home/kali/blacklird/blackbird.py /usr/bin/blackbird"]
#================PWN TOOLS================#

#================REVERSE TOOLS================#
r2 = ["r2"]
gdb = ["gdb"]
binaryninja = ["binaryninja"]
hyda = ["hyda"]
#================STEGANO TOOLS================#
steghide = ["steghide"]
stegseek = ["stegseek"]
stegolsb = ["stegolsb"]
zsteg = ["zsteg"]
pngcheck = ["pngcheck"]
tweakPNG = ["tweakPNG"]
Back = ["Back"]
#================WEB TOOLS================#
jwt_tool = ["jwt_tool", "git clone https://github.com/ticarpi/jwt_tool.git && cd jwt_tool && pipx -r requirements.txt && sudo ln -sfv /home/kali/jwt_tool/jwt_tool.py /usr/bin/jwt_tool"]
burpsuite = ["burpsuite"]
dirb = ["dirb"]
sqlmap = ["sqlmap"]
graphqlmap = ["graphqlmap"]
sstimap = ["sstimap", "git clone https://github.com/vladko312/SSTImap.git && cd sstimap && pipx -r requirements.txt && sudo ln -sfv /home/kali/sstimap/sstimap.py /usr/bin/sstimap"]
xsstrick = ["xsstrike"]
flask_unsign = ["flask_unsign"]
ipsourcebypass = ["ipsourcebypass"]

Crypto = [Back, hashcat, john, haiti, zip2john]
Forensic = [Back, autopsy, binwalk, volatility2, volatility3, volshell, crit, photorec]
Network = [Back, wireshark, tshark, hydra, scapy, ettercap, radsniff, "USB-mouse-pcap-visualizer", "impacket"]
Osint = [Back, blackbird]
Pwn = [Back]
Reverse = [Back, "r2", "gdb", "binaryninja", "hyda"]
Stegano = [Back, steghide, stegseek, stegolsb, zsteg, pngcheck, tweakPNG]
Web = [Back, burpsuite, dirb, sqlmap, graphqlmap, sstimap, xsstrick, jwt_tool, flask_unsign, ipsourcebypass]
Other = [Back, "Schemas", "Wordlists", "Recovery", "Nessus", "Sublist3r"]

Tools = [Crypto, Forensic, Network, Osint, Pwn, Reverse, Stegano, Web, Other]
#=========================LIST=========================#
def input_user(user_input, n1, n2):
    while True:
        try: user_input = int(input("> "))
        except ValueError:
            print(f"Is not a valid input, print number between {n1}-{n2 -1}")
            continue
        if n1 <= user_input < n2: return user_input
        else: print(f"Enter input valid (number {n1}-{n2 -1})") 

def listing(here):
    for idx, l in enumerate(here):
        print(f"[{idx}] {l}")

inp_categorie = 1

while 0 <= inp_categorie < len(categorie):
    #===========PRINT + INPUT===========#
    print(f"\n{Main_payload}\n\nEnter a number between 0-{len(categorie) -1} :\n")
    listing(categorie)
    inp_categorie = input_user(inp_categorie, 0, len(categorie))
    print(f" inp_categorie : {inp_categorie}")
    #===========PRINT + INPUT===========#
    if inp_categorie == 0:
        print(Exit_paylaod)
        exit()

    inp_choice = 0
    while 0 <= inp_choice < len(choice):
        #===========PRINT + INPUT===========#
        print(f"{payload[inp_categorie]}\nWhat do you want ?\n")
        listing(choice)
        inp_choice = input_user(inp_choice, 0, len(choice))
        print(f"inp_choice : {inp_choice}")
        #===========PRINT + INPUT===========#
        selected_categorie = Tools[inp_categorie -1]

        if inp_choice == 0:
            break
        elif inp_choice == 1:
            print("Mode tool use :\n")
        elif inp_choice == 2:
            print("Mode install :\n")
        elif inp_choice == 3:
            print("Mode link :\n")
        elif inp_choice == 4:
            print("Mode search :\n")

        inp_tool = 0
        while 0 <= inp_tool < len(selected_categorie):
            #===========PRINT + INPUT===========#
            print('What tool do you want to use ?\n')
            for idx, t in enumerate(selected_categorie):
                print(f"[{idx}] {t[0]}")
            inp_tool = input_user(inp_tool, 0, len(selected_categorie))
            print(f" inp_tool : {inp_tool} {type(inp_tool)}")
            #===========PRINT + INPUT===========#

            if inp_tool == 0:
                break
            if 0 < inp_tool <= len(selected_categorie):
                selected_tool = selected_categorie[inp_tool][inp_choice -1]
                os.system(selected_tool)
                inp_use = input("[0] Back\n> ")
                print(f" inp_use : {inp_use}")
                if inp_use == "0":
                    break
                os.system(inp_use)

# inp = input choice
# selected = the input choice








#parser = argparse.ArgumentParser()
#parser.add_argument("-a")
#agrs = parser.parse_args()
