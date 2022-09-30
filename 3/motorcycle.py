motorcycle = ['honda','yamaha','suzuki']
print(motorcycle)
motorcycle[0] = 'ducati'
print(motorcycle)
motorcycle.append('honda')
print(motorcycle)

motorcycle = []
motorcycle.append('honda')
motorcycle.append('yamaha')
motorcycle.append('suzuki')
motorcycle.append('ducati')
print(motorcycle)

motorcycle.insert(4,'bwm')
print(motorcycle)

del motorcycle[4]
print(motorcycle)

popped_motorcycle = motorcycle.pop(1)
print(motorcycle)
print(popped_motorcycle)

motorcycle.remove('ducati')
print(motorcycle)
