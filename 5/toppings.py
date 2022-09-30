requested_toppings = ['mushrooms','extra cheese']

if 'mushrooms' in requested_toppings:
	print('Add mushrooms.')
if 'extra cheese' in requested_toppings:
	print('Add extra cheese.')

for toppings in requested_toppings:
	if toppings == 'mushrooms':
		print('sorry')
	else:
		print("Add " + toppings +'.')
