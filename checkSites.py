#!/usr/bin/python

import httplib
import csv
 
def csv_reader(file_obj):
    online=0
    total=0
    reader = csv.reader(file_obj)
    for row in reader:
        total=total+1
        conn = httplib.HTTPConnection(row)
        conn.request("HEAD", "/")
        r1 = conn.getresponse()
        if r1.status == 200:
            online=online+1
        print row, r1.status, r1.reason
    
    print online+"/"+total
 
if __name__ == "__main__":
    csv_path = "sites.csv"
    with open(csv_path, "rb") as f_obj:
        csv_reader(f_obj)
