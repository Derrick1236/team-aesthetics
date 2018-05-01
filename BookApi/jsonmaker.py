import urllib
import requests
from pprint import pprint

link = "https://www.googleapis.com/books/v1/volumes?q=dog&callback=handleResponse"

f = requests.get(link)

json_string = f.text

json_string = json_string[31:-2]

text_file = open("Output.json", "w")
text_file.write(json_string)
text_file.close()
print (json_string)
