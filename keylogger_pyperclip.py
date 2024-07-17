import pyperclip
import time


list = [] #making empty list to append the code later on

while True:
    if pyperclip.paste() != 'None':
        value = pyperclip.paste()

        if value not in list:
            list.append(value)
        
        time.sleep(3)