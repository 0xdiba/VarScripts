import httplib
import csv
 
def csv_reader(file_obj):
    """
    Read a csv file
    """
    reader = csv.reader(file_obj)
    for row in reader:
        conn = httplib.HTTPConnection(row)
        conn.request("HEAD", "/")
        r1 = conn.getresponse()
        print row, r1.status, r1.reason
 
if __name__ == "__main__":
    csv_path = "sites.csv"
    with open(csv_path, "rb") as f_obj:
        csv_reader(f_obj)
