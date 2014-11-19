#!/usr/bin/python

import httplib
import socket
import csv
 
def csv_reader(file_obj):
    online=0
    total=0
    reader = csv.reader(file_obj)
    for row in reader:
        total=total+1
        #conn = httplib.HTTPSConnection(''.join(row), 443, timeout=5)
        conn = httplib.HTTPConnection(''.join(row), 80, timeout=5)
        try:
            conn.request("HEAD", "/")
            r1 = conn.getresponse()
            if r1.status == 200:
                online=online+1
            print row, r1.status, r1.reason
        except:
            print row,"error"

    print "online:", online, "/", total
 
if __name__ == "__main__":
    csv_path = "sites.csv"
    with open(csv_path, "rb") as f_obj:
        csv_reader(f_obj)
