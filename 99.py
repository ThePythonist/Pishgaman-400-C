import os
command = "ping 4.2.2.4 -t"
os.system(f"start /B start cmd.exe @cmd /k {command}")
