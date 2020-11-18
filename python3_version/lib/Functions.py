import readline
from lib.Globals import Color

def xss_input(prompt, text):
         def hook():
             readline.insert_text(text)
             readline.redisplay()
         readline.set_pre_input_hook(hook)
         result = input(prompt)
         readline.set_pre_input_hook()
         return result
def banner():
    pass

def starter(argv):
    if argv.banner:
        banner()
        exit()
    if not argv.base_url or not argv.payload:
        print(f"{Color.bad} Use --help")
        exit()
    else:
        return argv.base_url, argv.payload

def exit_handler(*args, filename=None):
    pass
