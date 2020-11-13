package main

import "fmt"
import "os"
import "strings"
import "regexp"
import "github.com/levigross/grequests"
import "github.com/machinexa2/gobasic"
import "github.com/akamensky/argparse"


func display_banner() {
	fmt.Println("Displayed");
}

func parse_file(filename string) {
	fmt.Println(filename);
}

func errorxss_check(resp string, errstr string, xss_payload string) string {
	xss_list := strings.Split(resp, "\n");
	for i := 0;i < len(xss_list); i++ {
		xssy := xss_list[i];
		xssz := gobasic.Urldecode(xssy);
		matched, err := regexp.MatchString(gobasic.Urldecode(errstr), xssz);
		gobasic.ErrorHandler(err);
		if matched {
			return "WAF Triggered";
		}
		if !(matched) {
			xss_matched, err := regexp.MatchString(gobasic.Urldecode(xss_payload), xssz);
			gobasic.ErrorHandler(err);
			if xss_matched {
				return xssy;
			}
		}
	}
	return "WAF Triggered";
}

func stringxss_check(resp string, xss_payload string) string {
	xss_list := strings.Split(resp, "\n");
	for i := 0;i < len(xss_list); i++ {
		xssy := xss_list[i];
		xssz := gobasic.Urldecode(xssy);
		xss_matched, err := regexp.MatchString(gobasic.Urldecode(xss_payload), xssz);
		gobasic.ErrorHandler(err);
		if xss_matched {
			return xssy
		}

	}
	return "WAF Triggered";
}

func main() {
	var xss_base,xss_payload,xss_url,xssy string;

	parser := argparse.NewParser("print", "XSS Terminal: Interactive XSS Development");
	base := parser.String("u", "baseurl", &argparse.Options{Required: true, Help: "Base URL for XSS"});
	payload := parser.String("p", "payload", &argparse.Options{Required: true, Help: "Starting payload"});
	errorstr := parser.String("e", "error-string", &argparse.Options{Required: false, Help: "String to identify blocked response"});
	_ = parser.String("o", "output", &argparse.Options{Required: false, Help: "Output filename"});
	resume := parser.String("r", "resume", &argparse.Options{Required: false, Help: "Resume XSST session by filename"});
	banner := parser.Flag("b", "banner", &argparse.Options{Required: false, Help: "Print banner and exit"});
	err := parser.Parse(os.Args);
	xss_base = *base;
	xss_payload = *payload;
	gobasic.ArgumentErrorHandler(err);

	if *banner == true {
		display_banner();
	} else if *resume != "" {
		parse_file(*resume);
	} else {
		fmt.Println("XSS Terminal");
		for {
			xss_url = xss_base + xss_payload; //slasher(xss_base), payloader(xss_payload)
			xss_payload = gobasic.PrefilledInputRead(xss_payload);
			response, err := grequests.Get(xss_url, nil);
			gobasic.ErrorHandler(err);
			xssy = "WAF Triggered";
			if *errorstr != "" {
				xssy = errorxss_check(response.String(), *errorstr, xss_payload);
			} else {
				xssy = stringxss_check(response.String(), xss_payload);
			}

			if xssy != "WAF Triggered" {
				fmt.Println(xssy);
			} else {
				fmt.Println(xssy);
			}

			break;
		}
	}
}

