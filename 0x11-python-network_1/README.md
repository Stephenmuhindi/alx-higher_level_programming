import urllib.request

url = "https://example.com"
response = urllib.request.urlopen(url)
html = response.read()
print(html)

2
decoded_html = html.decode("utf-8")
print(decoded_html)

3
url = "https://api.example.com/data"
response = urllib.request.urlopen(url)
data = response.read()
print(data)

4
pip install requests

5
import requests

url = "https://api.example.com/data"
response = requests.get(url)
data = response.text
print(data)

6
import requests

url = "https://api.example.com/submit"
data = {"key1": "value1", "key2": "value2"}
response = requests.post(url, data=data)
result = response.json()  # Assuming the response is JSON
print(result)

7
import requests

url = "https://api.example.com/json_data"
response = requests.get(url)
json_data = response.json()

# Manipulate data
for item in json_data["items"]:
    print(item["name"])

