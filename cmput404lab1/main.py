import requests

print(requests.__version__)

#r = requests.get("http://www.google.com")
#print(dir(r))
#print(r.text)
#print(r.status_code)
r = requests.get("https://github.com/xinyizhuang/cmput404lab1/edit/master/main.py")
print(dir(r))
print(r.text)
print(r.status_code)