# koinly-crypto-transaction-parser
Pulls all your crypto transactions from Koinly and parses them into an excel spreadsheet in a human-readable way.

## UPDATE
Now can also parse your transactions to tax-friendly excel sheet. 

## PLEASE NOTE
Use at your own risk -- do not rely on some stranger's code on github to extract proper documents. There may be bugs. 
Feel free to use as a starting point for your own more specific use case. 

### Why? 
When for example needing to withdraw larger sums of money from crypto exchanges to your traditional bank account you
 will need to provide the bank with a complete transaction history such that they can be confident that the incoming money 
 isn't fraudulent. 
 
You can connect all your crypto exchange accounts and wallets to Koinly and it does a great job creating a solid transaction history.
I couldn't find any way to extract all transactions so I wrote this script.

My bank was able to verify my transactions (over 1000 of them) in just a few hours and were extremely pleased with this way of
providing a history of transactions. So as long as you have connected all your accounts, you can be confident that
the resulting excel spreadsheet will go provide your authorities with all they need.
 

### How to use
* Go  to Koinly and connect all your accounts. 
* Go to Koinly's transaction page
* Open your browser's dev console and go to the network tab
* In the filter input field, enter "transactions"
* Step forward to the next page of your transactions in Koinly
* A request (type xhr) should be made in your network tab
* Select it, right-click and choose Copy -> Copy as cURL (bash)
* Go to https://curl.trillworks.com/ and paste in the curl command you copied
* Copy the headers object in the resulting python code and paste it into the script where requested
* Run the transactions-getter.py script to get all the data (stores it in a local json file)
* Run the transaction-parser.py script (parses the stored json file into a spreadsheet)
* Done!

Example copied headers
```
headers = {
    'authority': 'api.koinly.io',
    'caches-requests': '1',
    'x-csrf-token': 'csrf token',
    'x-portfolio-token': 'portfolio token',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'user agent',
    'accept': 'application/json, text/plain, */*',
    'x-auth-token': 'your auth token',
    'access-control-allow-credentials': 'true',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'sec-ch-ua-platform': '"macOS"',
    'origin': 'https://app.koinly.io',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://app.koinly.io/',
    'accept-language': 'sv-SE,sv;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'your cookie',
}
```
