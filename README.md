# Turn14 Formatter
This is a formatter to take data from Turn14.com's product data CSV export and import it to a google sheet that is formatted for Shopify's CSV import process. I made this before Turn14.com released their REST API, but I feel this is still useful to those who do not have experience with APIs.

## Dependencies
1. [GSpread](https://github.com/burnash/gspread)
1. [Requests](https://github.com/requests/requests)
1. [oauth2client](https://github.com/google/oauth2client)  
### Installing Dependencies
Simply run the following command:
```python
pip install -r requirements.txt
```

## Product Data Loadsheet
Go to [Turn14](turn14.com), go to data, and download Product Data Loadsheet. Unzip the file into your working folder.

## Shopify CSV Import Template
Use the following as a template for your Google Sheet:
[Shopify Import Template](https://docs.google.com/spreadsheets/d/1MzTcc7LXwM0p0kZE3tjKCZG0LRWAc0DoPb1R51TsR34/edit?usp=sharing)

## GSpread API
This script uses the gspread package to work with Google sheets. Be sure to include "client_secret.json" in your working directory.  
If you're unsure on how to get your client_secret.json, please follow this tutorial completely: [Using OAuth2 for Authorization](http://gspread.readthedocs.io/en/latest/oauth2.html)  
Rename your credentials file to client_secret.json, as that's how this script retreives the file.  
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
What you're going to need to do is take your **`"client_meail": "your client email"`** and share your Google Sheet with this user, giving them editing rights. If you do not do this, you will not have access to your sheet.
