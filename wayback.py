import requests
import json
import sys
import getopt

def usage():
    print(
    '''
    =======================================
    |                                     |
    |                                     |
    |          Sarvan sharma              |
    |                                     |
    |                                     |
    =======================================
    
    [*] Usage is 
        python3 wayback.py <target_url> <True or False to include subdomains (First letter should be a capital)>

    [*] For Help 
        python3 wayback.py -h
        python3 wayback.py --help

    [*] If you are facing an error,
        1. Check if you have specified "True" as true in small letters, same with False.
        2. Check the Target url specified.


    '''
    
    )


options1 = "h"
options2 = ["help"]
 
try:
    arguments, values = getopt.getopt(options1, options2)
    for currentArgument, currentValue in arguments:
 
        if currentArgument in ("-h", "--help"):
            usage()

except getopt.error as err:
    print (str(err))




def func(target, subdyesorno):
    if subdyesorno:
        waybackurl = 'http://web.archive.org/cdx/search/cdx?url=*.%s/*&output=json&fl=original&collapse=urlkey' %target
    else:
        waybackurl = 'http://web.archive.org/cdx/search/cdx?url=%s/*&output=json&fl=original&collapse=urlkey' %target
    r = requests.get(waybackurl)
    response = r.json()
    return response[1:]

if __name__ == '__main__':
    sysargcount = len(sys.argv)
    if sysargcount < 3:
        usage()
        sys.exit()
    
    target = sys.argv[1]
    subdyesorno = sys.argv[2]

    finalurls = func(target, subdyesorno)
    urls_in_json = json.dumps(finalurls)
    if finalurls:
        filename = '%s_waybackurls.txt' %target
        with open(filename, 'w') as f:
            f.write(urls_in_json)
        print('[*] Saved urls to %s' % filename)
    else:
        print('[-] Not able to find any url')
