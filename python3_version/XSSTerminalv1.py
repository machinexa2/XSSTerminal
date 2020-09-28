#V1 and V2 are deprecated dont use
import urllib.parse
import readline
from requests import Session
from bs4 import BeautifulSoup
from termcolor import colored
from os import system

yes = colored('[+]', color='green')
no = colored('[-]', color='red')
s = Session()

class XSST:
    def __init__(self, base, xss_payload):
        self.payload = ""
        self.base_url = base 
        self.xss_payload = xss_payload
        system('clear')

    def xss_input(self, prompt, text):
        def hook():
            readline.insert_text(text)
            readline.redisplay()
        readline.set_pre_input_hook(hook)
        result = input(prompt)
        readline.set_pre_input_hook()
        return result

    def return_xsscolor(self, xss, joinable):
        if len(joinable) > 1:
            if not "".join(joinable[1:]) in xss:
                xss_payload = joinable[0] + colored(xss, color='red') + "".join(joinable[1:])
        elif len(joinable) == 1:
            xss_payload = joinable[0] + colored(xss, color='red')
        return xss_payload

    def make_xss(self):
        self.xss_payload = self.xss_input(yes + ' ' +  "XSS Payload :> ", self.xss_payload)
        url = self.base_url + self.xss_payload
        response = s.get(url).text
        xss_list = response.split('\n')
        for xssy in xss_list:
            if self.xss_payload in xssy:
                colorful_xss = self.return_xsscolor(self.xss_payload, xssy.strip().split(self.xss_payload))
                print(colorful_xss)
        if not 'colorful_xss' in locals():
            print("WAF Triggered")
    
xss_base = 'http://brutal.x55.is/?src='        
xss_payload = 'google.com'
Terminal = XSST(xss_base, xss_payload)
while True:
    try:
        Terminal.make_xss()
    except KeyboardInterrupt:
        break
