#!/bin/python3
import random
import string
import requests
import time
startTime = time.time()

base = "https://www.YourURLHere.com/"
extension = "File Extension (.jpg,.bak,.sh, etc)"
count = int(input("How many times do you want to run the loop? "))
for i in range (count):
    # get random string of letters and digits
    source = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(source) for i in range(20)))
    # Send request to FQDN
    x = requests.get(base+result_str+extension)
    url = base+result_str+extension
    print(url)
    statuscode = x.status_code
    print(statuscode)
    if str(statuscode) == "200":
        f = open("hits.txt","a")
        f.write("HIT: " + url + "\n")
        f.close()
executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))
