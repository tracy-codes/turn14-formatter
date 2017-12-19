import csv
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# opens turnfourteen.csv (this is what comes from turn14.com when you do a product data csv export)
csv_file = list(csv.reader(open("turnfourteen.csv", "r"), delimiter=","))

# main method
def get_data(s):
    # set brand name we are looking for to br
    br = s
    # loop through all rows in csv_file
    for row in csv_file:
        # if brand exists in row
        if br in row[0]:
            # use creds to create a client to interact with the Google Drive API
            scope = ['https://spreadsheets.google.com/feeds']
            g_creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
            client = gspread.authorize(g_creds)
            # replace "Your Workbook" with the title of your workbook
            book = client.open("Your Workbook")
            # open the right worksheet (0 is first, 1, is second, 2 is third and so on...)
            sheet = book.get_worksheet(2)
            # get current row count
            row_count = sheet.row_count
            # assign important product values
            sku = row[3]
            title = row[4]
            min_price = row[9]
            retail = row[6]
            stock = row[14]
            weight = float(row[19])*453.59237
            brand = row[0]
            # generate url handle (this is not perfect)
            handle1 = title.lower() + " " + sku.lower()
            handle2 = handle1.replace("/", "-")
            handle3 = handle2.replace(".", "-")
            handle = "-".join(handle3.split())
            # initialize new product object
            new_prod = []
            # append product data in order of the Shopify CSV template
            new_prod.append(handle)
            new_prod.append(title)
            new_prod.append("")
            new_prod.append(brand)
            new_prod.append("")
            new_prod.append("brand_"+brand)
            new_prod.append("TRUE")
            new_prod.append("Title")
            new_prod.append("Default Title")
            new_prod.append("")
            new_prod.append("")
            new_prod.append("")
            new_prod.append("")
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
            # set index of the new row
            new_row = row_count+1
            # inserts new row
            sheet.insert_row(new_prod, index=new_row)
            print "Added SKU " + row[3] + " to the spreadsheet"
            new_row = new_row+1

# replace Brand Name with the brand you are needing to import
get_data("Brand Name")
