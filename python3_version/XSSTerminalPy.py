#!/usr/bin/python3
import readline

from os import system
from requests import Session
from termcolor import colored
from argparse import ArgumentParser
from urllib.parse import unquote_plus

from lib.Globals import *
from lib.Functions import starter, exit_handler

parser = ArgumentParser(description=colored("XSS Terminal", color='yellow'), epilog=colored('<script>window.location="https://bit.ly/3n60FQ4";</script>', color='yellow'))
string_group = parser.add_mutually_exclusive_group()
parser.add_argument('-u', '--base-url', type=str, help="Base URL")
parser.add_argument('-p', '--payload', type=str, help="Starting payload")
string_group.add_argument('-e', '--error-string', type=str, help="Error string")
string_group.add_argument('-s', '--match-string', type=str, help="Match string")
string_group.add_argument('-b', '--blind-string', type=str, help="Blind error string")
parser.add_argument('-m', '--method', type=str, choices=['GET','POST'], help="HTTP Method (Default get)")
parser.add_argument('-o', '--output', type=str, help="Output file name")
parser.add_argument('-r', '--resume', type=str, help="Filename to resume XSST session")
parser.add_argument('-B', '--banner', action="store_true", help="Print banner and exit")
argv = parser.parse_args()

xss_base, xss_payload = starter(argv)
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

    def return_xsscolor(self, xss_payload, joinable) -> str:
        xssz = unquote_plus(unquote_plus(xss_payload)).rstrip(' ')
        if len(joinable) > 1:
            if not "".join(joinable[1:]) in xssz:
                xss_payload = joinable[0] + colored(xssz, color='red') + "".join(joinable[1:])
        elif len(joinable) == 1:
            if not xssz in joinable[0]:
                xss_payload = joinable[0] + colored(xssz, color='red')
            else:
                xss_payload = joinable[0].split(xssz)[0] + colored(xssz, color='red')
        return xss_payload

    def stringxss_check(self, xss_list) -> str:
        for xssy in xss_list:
            if argv.match_string:
                if unquote_plus(unquote_plus(argv.match_string)) in unquote_plus(xssy):
                    return xssy
            else:
                if unquote_plus(unquote_plus(self.xss_payload)) in unquote_plus(xssy):
                    return xssy
        return 'WAF Triggered'

    def errorxss_check(self, xss_list) -> str:
        for xssy in xss_list:
            xssz = unquote_plus(xssy)
            if not unquote_plus(argv.error_string) in xssz:
                return xssy
            if unquote_plus(argv.error_string) in xssz:
                return 'WAF Triggered'
        return 'WAF Triggered'

    def blindxss_check(self, xss_list) -> str:
        for xssy in xss_list:
            xssz = unquote_plus(xssy)
            if urllib.parse.unquote(argv.blind_string) in xssz:
                return 'WAF Triggered'
        return 'Blind'

    def make_xss(self):
        try:
            self.xss_payload = self.xss_input(f"{ColorObj.information} XSS Payload :> ", self.xss_payload)
            url = self.base_url + self.xss_payload
            response = s.get(url).text
            xss_list = response.split('\n')
            if argv.error_string:
                xssy = self.errorxss_check(xss_list)
            elif argv.match_string:
                xssy = self.stringxss_check(xss_list)
            elif argv.blind_string: #under development
                xssy = self.stringxss_check(xss_list)
            else:
                xssy = self.stringxss_check(xss_list)
        except Exception as E:
            print(E)
        if not xssy == 'WAF Triggered' and not xssy == 'Blind':
            colorful_xss = self.return_xsscolor(self.xss_payload, [xssx for xssx in xssy.strip().split(self.xss_payload) if xssx])
            print(f"{ColorObj.good} {colorful_xss}")
        elif xssy == 'WAF Triggered':
            print(f"{ColorObj.bad} {xssy}")
        elif xssy == 'Blind':
            print(f"{ColorObj.good} Successfully executed")
    
if __name__ == "__main__":
    Terminal = XSST(xss_base, xss_payload)
    while True:
        try:
            Terminal.make_xss()
        except KeyboardInterrupt:
            if not argv.output:
                exit_handler(Terminal.base_url, Terminal.xss_payload)
            else:
                exit_handler(Terminal.base_url, Terminal.xss_payload, filename=argv.output)
        except Exception as E:
            print(E,E.__class__)
            exit()
