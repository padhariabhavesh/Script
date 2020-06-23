# Programmer  Bhavesh Padharia

# Perform Google Search using Python

from googlesearch import search
query = "padhariabhavesh"

for i in search(query, tld="co.in", num=10, stop=10, pause=2):
    print(i)

