import pyfiglet
ascii_banner = pyfiglet.figlet_format("ALI")
print(ascii_banner)

print("Welcome to my 1st Program")
import subprocess

data = subprocess.check_output(["netsh","wlan","show","profiles"]).decode("utf-8").split("\n")
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile in i"]
for i in profiles:
    results = subprocess.check_output(["netsh","wlan","show","profile", i, "key=clear"]).decode("utf-8").split("\n")
    results = [b.split(":")[1][1:-1] for b in results if ("Key Content") in b]
