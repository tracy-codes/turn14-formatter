# Turn14 Formatter
This is a formatter to take data from Turn14.com's product data CSV export and import it to a google sheet that is formatted for Shopify's CSV import process.
## Product Data Loadsheet
For speed's sake I did not include a download function to automatically download the product data loadsheet. You may use download.py to download the loadsheet without needing to go to turn14.com.  
Edit turn14_creds.json to your Turn14.com login and then use download.py to download the loadsheet.  
I would recommend manually downloading the loadsheeet before starting (it takes a few minutes sometimes and I don't like waiting for a script to stop running).  
I made this before Turn14.com released their REST API, but I feel this is still useful to those who do not have experience with APIs.  
## GSpread API
This script uses the gspread package to work with Google sheets. Be sure to inclued "client_secret.json" in your working directory.  
If you're unsure on how to get your client_secret.json, please follow this tutorial completely: [Using OAuth2 for Authorization](http://gspread.readthedocs.io/en/latest/oauth2.html)  
Be sure to rename your credentials file as client_secret.json, as that's how this script retreives the file.  
Your client_secret.json will look like the following:
```json
{
  "type": "service_account",
  "project_id": "your project id",
  "private_key_id": "your private key id",
  "private_key": "-----BEGIN PRIVATE KEY-----PRIVATE KEY HERE-----END PRIVATE KEY-----\n",
  "client_email": "your client email",
  "client_id": "your client id",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://accounts.google.com/o/oauth2/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "your cert url"
}
```
What you're going to need to do is take your 
```json 
"client_meail": "your client email"
```
and share your Google Sheet with this user, giving them editing rights. If you do not do this, you will not have access to your sheet.
## Dependencies
1. GSpread
1. Requests
1. oauth2client