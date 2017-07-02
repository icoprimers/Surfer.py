# Surfer.py

Yeah you've opened the readme so that shows some commitment to try this script out. Take a deep breath before we dive in the whole framework.  Here's a list of all the functions:

- btrequest(uri)

Lets say we want to get the balance of our BTC wallet:

Step 1: assign the uri of the api function you want to a variable.  The values however you leave for string substitution ({0} {1} etc) so you can keep reusing it with .format().


    balance = '/account/getbalance?currency={0}'  
    print(balance.format('btc')
    print(btrequest(balance.format('btc')))

Step 2: Use this btrequest function and string substitute the uri variable with the desired value. This returns a parsed json result like this:
    
    btcbalance = btrequest(balance.format('btc')

You can also create dictionaries with it if you prefer:

    balances = {'btc': btrequest(balance.format('btc')),
               'eth': btrequest(balance.format('eth'))}


So this way you have the whole API to your disposal. If you put it in loops it'd be kind of you to put a little sleep function in between.

Below is the API reference I used to prevent constantly switching windows. 
I postfixed _COMMANDS but /public/, /market/ and /account/ are the first part of the uri you have to build.
A null value is something you can query right away and the others need to have string substituion.  So here are two examples.

    ACCOUNT_COMMANDS['getbalances']:

    in a single command:
        balances = btrequest('/account/getbalances')

    MARKET_COMMANDS['sellimit'] would be:
    
    in a single command:
        sellorder = btrequest('/market/selllimit?market=btc-eth&quantity=10&rate=0.1')
        
    with string substitution in a second variable:
        sellorder = '/market/selllimit?market={0}&quantity={1}&rate={2}'
        panicsellorder = sellorder.format('btc-eth', 10, 0.1)
        result = btrequest(panicsellorder)
        
    with string substition the function:
        sellorder = '/market/selllimit?market={0}&quantity={1}&rate={2}'    
        result = btrequest(sellorder.format('btc-eth', 10, 0.1))
    
You can decide for yourself to create a panicsell variable for btrequest,  or call the btrequest function right away. So these string substitions are practical templates that can be used in different places. If it doesn't work, go to the bittrex documentation. Below is reference.

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
