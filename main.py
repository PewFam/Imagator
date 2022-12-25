import re, requests

import time
import os
import sys


from quo.dialog import MessageBox

MessageBox(
    title='Error',
    text='This tool doesnt work anymore, an update will be created. Go check my github : https://github.com/PewFam',
    ok_text  = "Ok")
    
payload = """     _ __       ,----.          ,-.-.      _,---.   ,---.             ___   
  .-`.' ,`.  ,-.--` , \,-..-.-./  \==\ .-`.' ,  \ .--.'  \     .-._ .'=.'\  
 /==/, -   \|==|-  _.-`|, \=/\=|- |==|/==/_  _.-' \==\-/\ \   /==/ \|==|  | 
|==| _ .=. ||==|   `.-.|- |/ |/ , /==/==/-  '..-. /==/-|_\ |  |==|,|  / - | 
|==| , '=',/==/_ ,    / \, ,     _|==|==|_ ,    / \==\,   - \ |==|  \/  , | 
|==|-  '..'|==|    .-'  | -  -  , |==|==|   .--'  /==/ -   ,| |==|- ,   _ | 
|==|,  |   |==|_  ,`-._  \  ,  - /==/|==|-  |    /==/-  /\ - \|==| _ /\   | 
/==/ - |   /==/ ,     /  |-  /\ /==/ /==/   \    \==\ _.\=\.-'/==/  / / , / 
`--`---'   `--`-----``   `--`  `--`  `--`---'     `--`        `--`./  `--`               """

class font_colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


default = """
.----------.---------------------------.
| Commands |        Utility            |
:----------+---------------------------:
| help     | shows all of the commands |
'----------'---------------------------'\n\n\n"""


help = ("""\n\n..........................................
: Commands :           Utility           :
:..........:.............................:
: download :      Downloads an image     :
:..........:.............................:\n\n
""")
def typingPrint(text):
        for character in text:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.007)
print(font_colors.OKBLUE + payload)
print(font_colors.OKGREEN + default + font_colors.FAIL)


while True:
    command= input("")
    if command == "help":
        print(f'{font_colors.WARNING}{help}{font_colors.FAIL}')
    if command == "download":

        def Download(link):
            
            p = r'<img.*?src="(.*?)"[^\>]+>'
            

            final = requests.get(link)
            text = final.text
            img = re.findall(p, text)
        

            for i in img:
                os.system("wget {}".format(i))

            typingPrint(f'\n{font_colors.OKCYAN}Image has been downloaded perfectly !{font_colors.FAIL}')
        typingPrint('\nEnter link ( don\'t forget "https://" )\n\n')
        response = input('')

        Download(response)
