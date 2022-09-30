invitor = ['zhang jinwen','lv lanxiang','zheng yinghan','wei xiaowen']
print(invitor)

poped_invitor = invitor.pop(3)
print(invitor)
print("The invitor who can't is " + poped_invitor.title() + '.')

invitor.insert(3,'zhang ning')
print(invitor)

print("I've found a bigger table.")
invitor.insert(1,'chen yangxin')
invitor.insert(2,'chen zhiyi')
invitor.append('chen lingfeng')
print(invitor)

print("Sorry, I can only invite two visiters to come to eat dinner.")

number = len(invitor)
print(number)

