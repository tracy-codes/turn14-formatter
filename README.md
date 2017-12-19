# Turn14 Formatter
This is a formatter to take data from Turn14.com's product data CSV export and import it to a google sheet that is formatted for Shopify's CSV import process.
## Product Data Loadsheet
For speed's sake I did not include a download function to automatically download the product data loadsheet. You may use download.py to download the loadsheet without needing to go to turn14.com. Edit turn14_creds.json to your Turn14.com login and then use download.py to download the loadsheet.
I would recommend manually downloading the loadsheeet before starting (it takes a few minutes sometimes and I don't like waiting for a script to stop running).
I made this before Turn14.com released their REST API, but I feel this is still useful to those who do not have experience with APIs.
Dependencies: gspread, 