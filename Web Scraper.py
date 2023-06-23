import requests
import bs4
result=requests.get("http://www.example.com")
print(type(result))
print(result.text)