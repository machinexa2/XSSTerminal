# XSS Terminal

Develop your own XSS payload for CTFs and read response smartly. Typing the payload manually in browser and finding that specific text in view-source is booring. This is the upgrade you need.

## Features:
1. Easy to view response without lot of shits.
2. Interactive testing whether `WAF` has blocked or not using error string.
3. Run and save xsst sessions for future use.
4. Go version is currently in development.

Python3 code is deprecated and archived. Please use go and improve it instead but i feel lazy sometimes and use python3 coz i feel its better.

## Installation:
`go get -u -v github.com/machinexa2/XSSTerminal` or you can use git clone the use archived version.

## Example Use:
Using old python3 version, this is what xss development looks like. I was developing xss payload for CTF.  
The argument was something like this:- `python3 XSSTerminalX.py --base-url http://ctfsite.com/?src= -p 'startingtext' -e 'Blocked'`
![medevelopingxss](https://cdn.discordapp.com/attachments/741721459520438396/751493373587750962/unknown.png)  

At last, i came up with the payload with console.log()
## Notes:
1. Golang version is in development
2. There are some other issue like which make it suitable for GET request only
3. Bugs maybe there.
4. Session saving and restoring from file hasnt been implemented in go version.
