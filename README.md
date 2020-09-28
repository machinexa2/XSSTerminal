# XSS Terminal
Develop your own XSS payload for CTFs and read response smartly. Typing the payload manually in browser and finding that specific text in view-source is booring. This is the upgrade you need.

## Features:
1. Easy to view response without lot of shits.
2. Interactive testing whether `WAF` has blocked or not using error string.
3. Run and save xsst sessions for future use.
4. Go version is currently in development.

Python3 code is most developed and stable version. Although you may use python3 version, go version is also in development. Please open pull requests to make go version better!

## Installation:
For Python3:
`git clone https://github.com/machinexa2/XSSTerminal && cd XSSTerminal/python3_version && ./XSSTerminal.py`

For golang:
Its disabled until go is perfectly developed: `go get -u -v github.com/machinexa2/XSSTerminal`  
Instead,
`git clone https://github.com/machinexa2/XSSTerminal && cd XSSTerminal/golang_version && go build xsst.go && mv xsst /usr/bin/XSSTerminal`

## Example:
For Python3: (Go is quite similar)
1. Using one get parameter
./XSSTerminal.py -u https://baseurl.com/?vulnerable_parameter= -p sometext -e string_to_indicate_WAF_block
2. Using multiple get parameter
./XSSTerminal.py -u https://baseurl.com/?par1=yes&par2=no&par3=nothing&vulnerable_parameter= -p sometext -e string_to_indicate_WAF_block
3. POST is still in development

Using python3 version, this is what xss development looks like. I was developing xss payload for Brutal Lands: Clownflare CTF.  
The argument was something like this:- `python3 XSSTerminalX.py --base-url http://brutal.x55.is/?src= -p 'startingtext' -e 'Blocked'`
![medevelopingxss](https://cdn.discordapp.com/attachments/741721459520438396/751493373587750962/unknown.png)  

At last, i came up with the payload with console.log()

## Notes:
1. Golang version is in development
2. There are some other issue like which make it suitable for GET request only
3. Bugs maybe there.
4. Session saving and restoring from file hasnt been implemented in go version and python3 version, POST parameter isnt avialable for now!
