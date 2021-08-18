#Written by Thecat8413, very basic, use with caution. 
import keyboard
import requests
import pyperclip

print("Enter Github RAW URL")
userIn=input()
try:
    file=requests.get(userIn)
    open('temp.yolol','wb').write(file.content)
except:
    print("ERROR")
s=open('temp.yolol',)
s=s.readlines()
for l in s: 
    pyperclip.copy(l)
    keyboard.wait('down')
print("NO MORE LINES; DONE")
