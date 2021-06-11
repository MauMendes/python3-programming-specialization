#pip install requests

import requests
import json

from requests.api import request

#page = requests.get("https://api.datamuse.com/words?rel_rhy=funny")
#print(type(page))
#print(page.text[:150]) # print the first 150 characters
#print(page.url) # print the url that was fetched
#print("------")
#x = page.json() # turn page.text into a python object
#print(type(x))
#print("---first item in the list---")
#print(x[0])
#print("---the whole list, pretty printed---")
#print(json.dumps(x, indent=4)) # pretty print the results

#page = requests.get("https://www.google.com/search?q=%22violins+and+guitars%22&tbm=isch")
#print(type(page))
#print(page.text[:500]) # print the first 150 characters
#print(page.url) # print the url that was fetched
#print("------")
#x = page.json() # turn page.text into a python object
#print(type(x))
#print("---first item in the list---")
#print(x[0])
#print("---the whole list, pretty printed---")
#print(json.dumps(x, indent=4)) # pretty print the results

#kval_pairs = {'rel_rhy': 'funny'}
#page = requests.get("https://api.datamuse.com/words", params=kval_pairs)
#print(page.text[:150]) # print the first 150 characters
#print(page.url) # print the url that was fetched

#d = {'q':'violins and guitars', 'tbm':'isch'}
#results = requests.get("https://google.com/search",params=d)
#print(results.url)
#print(results.text)

#d = {'q':'acdc band'}
#results = requests.get("https://google.com/search",params=d)
#print(results.url)
#print(results.text)

#def get_rhymes(word):
#    baseurl="https://api.datamuse.com/words"
#    params_diction = {}
#    params_diction["rel_rhy"] = word
#    params_diction["max"] = "3" # get at most 3 results
#    resp = requests.get(baseurl, params=params_diction)
#    words_ds = resp.json()
#    print(resp.url)
#    return [d['word'] for d in words_ds]
#print(get_rhymes("funny"))


import requests_with_caching
# it's not found in the permanent cache
res = requests_with_caching.get("https://api.datamuse.com/words?rel_rhy=happy")
print(res.text[:100])
# this time it will be found in the temporary cache
res = requests_with_caching.get("https://api.datamuse.com/words?rel_rhy=happy", permanent_cache_file="datamuse_cache.txt")
# This one is in the permanent cache.
res = requests_with_caching.get("https://api.datamuse.com/words?rel_rhy=funny", permanent_cache_file="datamuse_cache.txt")
