import json
import urllib.request, urllib.parse, urllib.error

url = input("Enter URL: ")
print("Retrieving ", url)
data = urllib.request.urlopen(url).read()
info = json.loads(data)
print('comments count:', len(info["comments"]))
total = 0
for item in range(len(info["comments"])):
    total += int(info["comments"][item]["count"])
print(total)
