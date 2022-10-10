import requests
import json

def getComms(un):
  if not isinstance(un, str):
    return "Please enter a valid username"

  rep = 'https://api.github.com/users/' + un + '/repos'
  get = requests.get(rep)
  jason = json.loads(get.text)
  name = []

  for obj in jason:
    name.append(obj["name"])

  s = 0

  for i in name:
    comts = 'https://api.github.com/repos/' + un + '/' + i + '/commits'
    com = requests.get(comts)
    x = json.loads(com.text)
    print('Repo: ' + i + ' Number of commits: ' + str(len(x)))
    s = s + len(x)

  length = len(name) + s
  return length

print(getComms("riya-divakaran"))


