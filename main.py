import requests, time, os, subprocess
import json
import psutil

data_link = requests.get("https://pastebin.com/raw/").text
hwid = subprocess.check_output("wmic csproduct get uuid").decode().split('\n')[1].strip()

for proc in psutil.process_iter():
    name = proc.name()
    if name == "httpDebuder.exe":
        os._exit()

try:
    if hwid in data_link:
        pass
    else:
        print("invalid hwid")
        time.sleep(1)
        os._exit()
except:
    print("Databese Error")
    time.sleep(5)
    os._exit()

data = json.loads(data_link)
print("uid:", data["uid"])
print("user:", data["user"])
