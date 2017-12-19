import gspread
import csv
from oauth2client.service_account import ServiceAccountCredentials
import requests

# opens turnfourteen.csv (this is what comes from turn14.com when you do a product data csv export)
csv_file = list(csv.reader(open("turnfourteen.csv", "r"), delimiter=","))

# main method
def get_data(s):
    # set brand name we are looking for to br
    br = s
    # loop through all rows in csv_file
    for row in csv_file:
        # if brand exists in ""
        if br in row[0]:
            # use creds to create a client to interact with the Google Drive API
            scope = ['https://spreadsheets.google.com/feeds']
            g_creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
            client = gspread.authorize(g_creds)

            book = client.open("T14")
            sheet = book.get_worksheet(2)
            row_count = sheet.row_count
            sku = row[3]
            title = row[4]
            min_price = row[9]
            retail = row[6]
            stock = int(row[14])
            weight = float(row[19])*453.59237
            handle1 = title.lower() + " " + sku.lower()
            handle2 = handle1.replace("/", "-")
            handle3 = handle2.replace(".", "-")
            handle = "-".join(handle3.split())
            new_prod = []
            new_prod.append(handle)
            new_prod.append(title)
            new_prod.append("")
            new_prod.append("T14")
            new_prod.append("")
            new_prod.append("brand_"+row[0])
            new_prod.append("TRUE")
            new_prod.append(sku)
            new_prod.append(weight)
            new_prod.append("shopify")
            new_prod.append(stock)
            new_prod.append("deny")
            new_prod.append("manual")
            new_prod.append(min_price)
            new_prod.append(retail)
            new_prod.append("TRUE")
            new_prod.append("TRUE")
            new_row = row_count+1
            sheet.insert_row(new_prod, index=new_row)
            print "Added SKU " + row[3] + " to the spreadsheet"
            new_row = new_row+1

get_data("Invidia")