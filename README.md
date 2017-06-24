# Surfer.py

Yeah you've opened the readme so that shows some commitment to try this script out. Take a deep breath before we dive in the whole framework.  Here's a list of all the functions:
- none(uri)
- btrequest(uri)

I only explain this twice so keep on reading. Lets say we want to get the balance of our BTC wallet:

Step 1: put the uri of the api function you want in this nonce function and assign it to a variable. 
The values however you leave for string substitution so you can keep reusing it. 
This nonce function adds the nonce to the uri so that's taken care of.

    getbalance = nonce('/account/getbalance?currency={0}')    

Step 2: Use this btrequest function and string substitute the uri variable with the desired value like this:
    balancebtc = btrequest(getbalance.format('btc')

You can also create dictionaries with it if you prefer:

    balance = {'btc': btrequest(getbalance.format('btc')),
               'eth': btrequest(getbalance.format('eth'))}


So this way you have the whole API to your disposal. 
If you put it in loops it'd be kind of you to put a little sleep function in between.

Below is the API reference I used to prevent constantly switching windows. 
I postfixed _COMMANDS but /public/, /market/ and /account/ are the first part of the uri you have to build.
A null value is something you can query right away and the others need to have string substituion.  So here are two examples.

ACCOUNT_COMMANDS['getbalances'] would be:

    balances = nonce('/account/getbalances')

MARKET_COMMANDS['sellimit'] would be:

    sellorder = nonce('/market/selllimit?market={0}&quantity={1}&rate={2}')
    panicsell = sellorder.format('btc-eth', ethquantity, marketbid)

So these string substitions are very useful as a reusable template.

#If it doesn't work, go to the bittrex documentation.

    PUBLIC_COMMANDS = '''{
        "getmarkets": null,
        "getcurrencies": null,
        "getticker": null,
        "getmarketsummaries": "market",
        "getorderbook": [ "market","type","depth" ],
        "getmarkethistory": "market"
    }'''

    MARKET_COMMANDS = '''{
        "buylimit": [ "market", "quantity", "rate" ],
        "sellimit": [ "market", "quantity", "rate" ],
        "cancel": [ "market", "quantity", "rate" ] ,
        "getopenorders": [ "market" ]
    }'''

    ACCOUNT_COMMANDS = '''{
        "getbalances": null,
        "getbalance": "currency",
        "getdepositaddress": "currency",
        "withdraw": [ "currency", "quantity", "address", "paymentid" ]
        "getorder": "uuid",
        "getorderhistory": "market",
        "getwithdrawalhistory": "currency",
        "getdeposithistory": "currency"
    }'''
