"""
import requests
import sys

if len(sys.argv)!=2:
    sys.exit()

response= requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" +sys.argv[1])
print(response.json())

#has been standardised as a dictionary
#uses almost the same syntax
"""

#another library called json to make it better
"""
import json
import requests
import sys

if len(sys.argv)!=2:
    sys.exit()

response= requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" +sys.argv[1])
print(json.dumps(response.json(), indent=2))
"""

#{}->dictionary->collection of key value pairs
#[]->list


#now we are making it better by 
import json
import requests
import sys

if len(sys.argv)!=2:
    sys.exit()

response= requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" +sys.argv[1])
o= response.json()
for result in o["results"]:
    print(result["trackName"])

#can we use break instead of sys.exit()?
#no use break for loops 
#and use sys.exit() to exit out of the program