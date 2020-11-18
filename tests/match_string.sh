(php -S 0.0.0.0:80 1>/dev/null 2>/dev/null &)
../XSSTerminal.py -u http://127.0.0.1/match_string?pay= -p 'ls<script%20></script>'
