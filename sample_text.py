#!/usr/bin/env python3
import houndify
import sys

CLIENT_ID = sys.argv[1]
CLIENT_KEY = sys.argv[2]
QUERY = sys.argv[3]
#print("Query: ", QUERY)

requestInfo = {
  ## Pretend we're at SoundHound HQ.  Set other fields as appropriate
  'Latitude': 37.388309, 
  'Longitude': -121.973968
}

client = houndify.TextHoundClient(CLIENT_ID, CLIENT_KEY, "test_user", requestInfo)

## Uncomment the lines below to see an example of using a custom
## grammar for matching.  Use the file 'turnthelightson.wav' to try it.
# clientMatches = [ {
#   "Expression" : '([1/100 ("can"|"could"|"will"|"would")."you"].[1/10 "please"].("turn"|"switch"|(1/100 "flip"))."on".["the"].("light"|"lights").[1/20 "for"."me"].[1/20 "please"])|([1/100 ("can"|"could"|"will"|"would")."you"].[1/10 "please"].[100 ("turn"|"switch"|(1/100 "flip"))].["the"].("light"|"lights")."on".[1/20 "for"."me"].[1/20 "please"])|((("i".("want"|"like"))|((("i".["would"])|("i\'d")).("like"|"want"))).["the"].("light"|"lights").["turned"|"switched"|("to"."go")|(1/100"flipped")]."on".[1/20"please"])"',
#   "Result" : { "Intent" : "TURN_LIGHT_ON" },
#   "SpokenResponse" : "Ok, I\'m turning the lights on.",
#   "SpokenResponseLong" : "Ok, I\'m turning the lights on.",
#   "WrittenResponse" : "Ok, I\'m turning the lights on.",
#   "WrittenResponseLong" : "Ok, I\'m turning the lights on."
# } ]
# client.setHoundRequestInfo('ClientMatches', clientMatches)

# TODO: if I input hello, custom output: world!

response = client.query(QUERY)
#print(client.query("Tell me a math joke"))
#print(response)

toContinue = True
while toContinue:
    
    print("1. Query")
    print("2. Key/Value map")
    print("3. Quit")
    choice = int(input("Choose an option: "))
    
    if choice == 1:
        myQuery = input("Input query: ").lower()
        if myQuery == "q" or myQuery == "quit":
            toContinue = False
            print("Good bye loser!")
        else:
            response = client.query(myQuery)
            #print(response)
            print(response)
            #print("Response:", response["AllResults"][0]["WrittenResponse"])
    elif choice == 2:
        key = input("Input key: ")
        value = input("Input value: ")
        
        if key.lower() == "q" or value.lower() == "q":
            toContinue = False
            print("Good bye loser!")
        else:
            client.setHoundRequestInfo("city", "san francisco")
    elif choice == 3:
        toContinue = False
        print("Good by loser!")
    else:
        print("Oops! Please enter a number between 1 and 3")
            
            
        