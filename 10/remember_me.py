import json

username = input("What's your name?")

filename = 'user.json'
with open(filename,'w') as f_obj:
	json.dump(username, f_obj)
	print("we will remember you when you come back, " + username + '!')