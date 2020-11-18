from os import system
from requests import Session
from termcolor import colored
from urllib.parse import unquote_plus as urldecode

from lib.Globals import Color
from lib.Functions import xss_input

s = Session()
class XSST:
    def __init__(self, base, xss_payload):
        self.payload = ""
        self.base_url = base 
        self.xss_payload = xss_payload
        system('clear')

    def return_xsscolor(self, xss_payload, joinable) -> str:
        xssz = urldecode(urldecode(xss_payload)).rstrip(' ')
        if len(joinable) > 1:
            if not "".join(joinable[1:]) in xssz:
                xss_payload = joinable[0] + colored(xssz, color='red') + "".join(joinable[1:])
        elif len(joinable) == 1:
            if not xssz in joinable[0]:
                xss_payload = joinable[0] + colored(xssz, color='red')
            else:
                xss_payload = joinable[0].split(xssz)[0] + colored(xssz, color='red')
        return xss_payload

    def stringxss_check(self, xss_list, match_string=None) -> str:
        for xssy in xss_list:
            if match_string:
                if urldecode(urldecode(match_string)) in urldecode(xssy):
                    return xssy
            else:
                if urldecode(urldecode(self.xss_payload)) in urldecode(xssy):
                    return xssy
        return 'WAF Triggered'

    def errorxss_check(self, xss_list, error_string=None) -> str:
        for xssy in xss_list:
            xssz = urldecode(xssy)
            if not urldecode(error_string) in xssz:
                return xssy
            if urldecode(argv.error_string) in xssz:
                return 'WAF Triggered'
        return 'WAF Triggered'

    # def blindxss_check(self, xss_list, blind_string=None) -> str:
        # for xssy in xss_list:
            # xssz = urldecode(xssy)
            # if urllib.parse.unquote(blind_string) in xssz:
                # return 'WAF Triggered'
    #     return 'Blind'

    def make_xss(self, argv):
        try:
            self.xss_payload = xss_input(f"{Color.information} XSS Payload :> ", self.xss_payload)
            url = self.base_url + self.xss_payload
            response = s.get(url).text
            xss_list = response.split('\n')
            if argv.error_string:
                xssy = self.errorxss_check(xss_list, error_string=argv.error_string)
            elif argv.match_string:
                xssy = self.stringxss_check(xss_list, match_string=argv.match_string)
            elif argv.blind_string:
                xssy = self.stringxss_check(xss_list, blind_string=argv.blind_string)
            else:
                xssy = self.stringxss_check(xss_list)
        except Exception as E:
            print(f"{Color.bad} Error {E},{E.__class__} occured! Exiting");
            exit(0);

        if not xssy == 'WAF Triggered':# and not xssy == 'Blind':
            colorful_xss = self.return_xsscolor(self.xss_payload, [xssx for xssx in xssy.strip().split(self.xss_payload) if xssx])
            print(f"{Color.good} {colorful_xss}")
        elif xssy == 'WAF Triggered':
            print(f"{Color.bad} {xssy}")
        #elif xssy == 'Blind':
        #    print(f"{Color.good} Successfully executed")
