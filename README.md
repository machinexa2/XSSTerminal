# XSSTerminal
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![XSSTerminal](lib/XSSTERMINAL.png)

## Description
Develop your own XSS payload for CTFs and read response smartly. Typing the payload manually in browser and finding that specific text in view-source is booring. This is the upgrade you need.

## Features:
1. Easy to view response without lot of shits.
2. Interactive testing whether `WAF` has blocked or not using error string.
3. Run and save xsst sessions for future use.
4. Both Go and Python3 version are available.

## Python3 or Golang?
Its obviously your choice! Python3 has easy syntax and lot of features are present! Go on the other hand is quite memory friendly.
Python3 code is most developed and stable. Go version is in development. Please open pull requests to make go version better!

## Installation:
For Python3:  
* `git clone https://github.com/machinexa2/XSSTerminal && cd XSSTerminal/python3_version && python3 -m pip install -r requirements.txt; ln -s "$(pwd)""/XSSTerminalPy.py" /usr/bin/XSSTerminal `

For Go:
* `git clone https://github.com/machinexa2/XSSTerminal && cd XSSTerminal/golang_version && go build xsst.go && mv xsst /usr/bin/XSSTerminal`

## Usage
```
usage: PyXSSTerminal [-h] [-u BASE_URL] [-p PAYLOAD] [-e ERROR_STRING | -s MATCH_STRING | -b BLIND_STRING] [-m {GET,POST}] [-o OUTPUT] [-r RESUME]

XSS Terminal

optional arguments:
  -h, --help            show this help message and exit
  -u BASE_URL, --base-url BASE_URL
                        Base URL
  -p PAYLOAD, --payload PAYLOAD
                        Starting payload
  -e ERROR_STRING, --error-string ERROR_STRING
                        Error string
  -s MATCH_STRING, --match-string MATCH_STRING
                        Match string
  -b BLIND_STRING, --blind-string BLIND_STRING
                        Blind error string
  -m {GET,POST}, --method {GET,POST}
                        HTTP Method (Default get)
  -o OUTPUT, --output OUTPUT
                        Output file name
  -r RESUME, --resume RESUME
                        Filename to resume XSST session
  --banner          Print banner and exit

<script>window.location="https://bit.ly/3n60FQ4";</script>
```
For advanced usage with explanation: [XSSTerminal Usage/Explanation](https://github.com/machinexa2/XSSTerminal/wiki/Usage)

## Example:
For Python3: (Go is quite similar)
1. Using one GET parameter:   
* ``` ./XSSTerminal.py -u https://baseurl.com/?v= -p hello.com'><script> -e 'Your IP has been blocked'```

2. Using multiple GET parameter:    
* ``` ./XSSTerminal.py -u https://baseurl.com/?par1=y&par2=n&par3=s&vulnerable_parameter= -p 'hello.com"><script>' -e 'Your IP has been blocked'```

3. Using multiple POST parameter:  
* ``` ./XSSTerminal.py -u https://baseurl.com/waf.php -p 'par1=y&par2=n&par3=s&vulnerable_parameter=hello.com"><script>' -e 'Your IP has been blocked' --method POST ```

## Live Example:
Using python3 version, this is what xss development looks like. I was developing xss payload for Clownflare WAF.  
The argument was something like this:-  

`python3 XSSTerminalX.py --base-url http://brutal.x55.is/?src= -p 'startingtext' -e 'Blocked'`

![medevelopingxss](https://cdn.discordapp.com/attachments/741721459520438396/751493373587750962/unknown.png)  

At last, i came up with the payload with console.log()

## Notes:
1. Golang version is in development so is python3. May encounter bugs
2. DOM XSS soon coming (not sure if that could be implemented)
3. Session saving and restoring from file hasnt been implemented in go version and python3 version, POST parameter isnt avialable for now!
