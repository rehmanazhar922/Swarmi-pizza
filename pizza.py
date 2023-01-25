import os, sys
import subprocess
from colorama import Fore, Style
file = open("Pizzafile", "r")
content = file.readlines()

exec_status = 0
help_list = ["network", "repl", "label", "cpu", "mem", "name"]
commands_list = ["create", "scale", "node", "_print_", "version '1'"]

try:
    if sys.argv[(1)] == "--exec":
        exec_status = 1
        print(Fore.BLUE, "This Script will be Executed", Style.RESET_ALL)

    if sys.argv[(1)] == "--help" or sys.argv[(1)] == "-h":
        print(Fore.BLUE, f"Vars: {help_list} \n Commands: {commands_list}", Style.RESET_ALL)
        os._exit(0)
    
except Exception as error:
    print(Fore.RED, f"The Execution is skiped!\n The error: {error}", Style.RESET_ALL)

if "version '1'" in content[0]:
    print(Fore.GREEN, "Version 1 detected",  Style.RESET_ALL)
elif "version" in content[0]:
    if "'1'" not in content[0]:
        print(Fore.RED, f"Wrong {content[0]}" , Style.RESET_ALL)
        os._exit(0)
else:
    print(Fore.RED, "Please define the version at the first line", Style.RESET_ALL)
    os._exit(0)

outfile = open("Pizzaout.sh", "w")

lines = 0

for line in content:
    #Args
    line = line.replace("name=", "--name ")
    line = line.replace("repl=", "--replicas ")
    line = line.replace("label=", "--container-label ")
    line = line.replace("cpu=", "--limit-cpu ")
    line = line.replace("mem=", "--limit-memory ")
    line = line.replace("network=", "--network ")

    if "create " in line or "scale " in line:
        line = f"sudo docker service {line}"
        outfile.write(f"{line}")
        lines = lines + 1 

    if "node " in line or "ps" in line:
        line = f"sudo docker {line}"
        outfile.write(f"{line}")
        lines = lines + 1 
    
    if "_print_ " in line:
        line = f"echo -e '{line}'"
        outfile.write(f"{line}")
        lines = lines + 1 
        
        
        
outfile.write(f"\necho 'Operation finished'")
lines = lines + 1

if exec_status == 1:
    cmd = subprocess.getoutput("bash Pizzaout.sh")
    print(f"Executed: {cmd}")

print(Fore.BLUE, "All operations", Fore.GREEN , f"done! wrote {lines} lines", Style.RESET_ALL)