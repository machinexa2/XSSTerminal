#v1 and v2 are deprecated, dont use
import urllib.parse
import readline

from requests import Session
from bs4 import BeautifulSoup
from termcolor import colored
from os import system
from argparse import ArgumentParser

from lib.Globals import *
from lib.Functions import starter, exit_handler

s = Session()

parser = ArgumentParser(description="XSS Terminal")
parser.add_argument('-s', '--string', type=str, help="Identifying string (Make sure its unique and same as payload)")
parser.add_argument('-e', '--error-string', type=str, help="Error string (Leave empty for -s check)")
parser.add_argument('-u', '--base-url', type=str, help="Base URL")
parser.add_argument('-p', '--payload', type=str, help="Starting payload")
parser.add_argument('-r', '--resume', action="store_true", help="Filename to resume XSST session")
parser.add_argument('-b', '--banner', action="store_true", help="Print banner and exit")
argv = parser.parse_args()

xss_base, xss_payload = starter(argv)

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

    def return_xsscolor(self, xss, joinable) -> str:
        if len(joinable) > 1:
            if not "".join(joinable[1:]) in xss:
                xss_payload = joinable[0] + colored(xss, color='red') + "".join(joinable[1:])
        elif len(joinable) == 1:
            xss_payload = joinable[0] + colored(xss, color='red')
        return xss_payload

    def stringxss_check(self, xss_list) -> str:
        for xssy in xss_list:
            if argv.string in xssy:
                return xssy
        return 'WAF Triggered'

    def errorxss_check(self, xss_list) -> str:
        for xssy in xss_list:
            if not argv.error_string in xssy:
                if argv.string in xssy:
                    return xssy
            if argv.error_string in xssy:
                return 'WAF Triggered'
        return 'WAF Triggered'

    def make_xss(self):
        self.xss_payload = self.xss_input(f"{ColorObj.information} XSS Payload :> ", self.xss_payload)
        url = self.base_url + self.xss_payload
        response = s.get(url).text
        xss_list = response.split('\n')
        if argv.error_string:
            xssy = self.errorxss_check(xss_list)
        elif argv.string:
            xssy = self.stringxss_check(xss_list)
        if not xssy == 'WAF Triggered':
            colorful_xss = self.return_xsscolor(self.xss_payload, [xssx for xssx in xssy.strip().split(self.xss_payload) if xssx])
            print(colorful_xss)
        elif xssy == 'WAF Triggered':
            print(f"{ColorObj.bad} {xssy}")
    
xss_payload = '<script>alert(1)</script>'
Terminal = XSST(xss_base, xss_payload)
while True:
    try:
        Terminal.make_xss()
    except KeyboardInterrupt:
        if exit_handler(Terminal.base_url, Terminal.xss_payload):
            exit()
