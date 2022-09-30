# Python_note by Myc

## 简单数据类型

### 字符串

在**`name.title()`**中，`name`后面的句点`.`让**Python**对变量`name`执行方法`title()`指定的操作。

`title()` 以首字母大写的方式显示每个单词，即将每个单词的首字母都改为大写。

```python
name = "Ada Lovelace"
print(name.upper())
print(name.lower())
```

方法**`lower()`**很有用。很多时候，你无法依靠用户来提供正确的大小写，因此需要将字符串先转换为小写，再存储它们。



要在字符串中添加制表符，可使用字符组合**`\t`**

要在字符串中添加换行符，可使用字符组合**`\n`**

还可在同一个字符串中同时包含制表符和换行符。字符串**"`\n\t`"**让Python换到下一行，并在下一行开头添加一个制表符。

**Python**能够找出字符串开头和末尾多余的空白。要确保字符串末尾没有空白，可使用方法**`rstrip()`**

你还可以剔除字符串开头的空白，或同时剔除字符串两端的空白。为此，可分别使用方法**`lstrip()`**和**`strip()`**



### 数字

可调用函数**`str()`**，它让**Python**将非字符串值表示为字符串。



## 列表简介

### 从列表中插入元素

方法**`append()`**将元素`'ducati'`添加到了列表末尾。

```python
motorcycles.append('ducati')
```



使用方法**`insert()`**可在列表的任何位置添加新元素。

```python
motorcycles.insert(0,'ducati')
```



### 从列表中删除元素

如果知道要删除的元素在列表中的位置，可使用**`del`**语句。

```python
del motorcycles[0]
```

方法**`pop()`**可删除列表末尾的元素，并让你能够接着使用它。

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
```



实际上，你可以使用**`pop()`**来删除列表中任何位置的元素，只需在括号中指定要删除的元素的索引即可。例如：**`pop(0)`**



### 组织列表

方法**`sort()`**永久性地修改了列表元素的排列顺序。现在，汽车是按字母顺序排列的，再也无法恢复到原来的排列顺序。

```python
cars.sort()
```

使用函数**`sorted()`**能够按特定顺序显示列表元素，同时不影响它们在列表中的原始排列顺序。

```python
print(sorted(cars))
```

倒着打印列表

```python
cars.reverse()
```

确定列表的长度，使用函数**`len()`**

```python
cars=['bme','audi','toyota','subaru']
len(cars)
4
```



## 操作列表

### `for`循环

```python
for magician in magicains:
		print(magician)
```

### 创建数值列表

使用**`range()`**函数，能够轻松生成一系列数字。

```python
for value in range(1,5)
		print(value)
```

#### 使用**`range()`**创建数字列表：

要创建数字列表，可使用函数**`list()`**将**`range()`**的结果直接转换为列表。如果将**`range()`**
 作为**`list()`**的参数，输出将为一个数字列表。

```python
numbers = list(range(1,6))
print(numbers)
```

使用**`range()`**时，还可指定步长。例如：

```python
even_numbers = list(range(2,11,2))
print(even_numbers)
min(digits)
max(digits)
sum(digits)
```

#### 列表解析：

列表解析让你只需编写一行代码就能生成这样的列表。

```python
squares = [value**2 for value in range(1,11)]
print(squares)
```



### 使用列表的一部分

#### 切片

要创建切片，可指定要使用的第一个元素和最后一个元素的索引。

```python
print(players[0:3])
```

用于创建任意列表的任意子集。

其他示例：

如果没有指定起始索引，**Python**从列表开头开始提取：

```python
print(players[:4])
```

如果没有指定终止索引，**Python**默认取道列表最后：

```python
print(players[2:])
```



遍历切片。



#### 复制列表

要复制列表，可创建一个包含整个列表的切片，方法是同时省略起始索引和终止索引**`[:]`**。



### 元组

有时需要创造一系列不可修改的元素，元组可以满足这种需求。

**Python**将不能修改的值称为不可变的，而不可变的列表被称为元组。

元组看起来犹如列表，但使用圆括号而不是方括号来标识。



遍历元组：

```python
dimensions = (200,50)
for dimension in dimensions:
		print(dimension)
```



修改元组变量是合法的，可以给存储元组的变量赋值。



### 设置代码格式

**PEP 8**

访问https://python.org/dev/peps/pep-0008/



## `if`语句

```python
cars = ['audi','bme','subaru','toyota']
for car in cars:
	if car == 'bme':
		print(car.upper())
	else:
		print(car.title())
```

### 条件测试

1.检查是否相等：`==`

2.检查是否不等：`!=`

3.检查多个条件：

​	使用`and`：

```python
age_0 >= 21 and age_1 >= 21
(age_0 >= 21) and (age_1 >= 21)
```

​	使用`or`：

```python
age_0 >= 21 or age_1 >=21
```

4.检查特定值是否包含在列表中：`in`

```python
requested_toppings = ['mushrooms','onions','pineapple']
'mushrooms' in requested_toppings
```

5.检查特定值是否不包含在列表中：`not in`

```python
if user not in banned_users:
```

6.布尔表达式：条件测试的别名，与条件表达式一样，布尔表达式的结果要么为 `True`,要么为 `False`。



### `if`语句

1.`if-else`语句：

```python
age = 17
if age >= 18:
      print("You are old enough to vote!")
      print("Have you registered to vote yet?")
else:
      print("Sorry, you are too young to vote.")
      print("Please register to vote as soon as you turn 18!")
```

2.`if-elif-else`结构：

```python
age = 12

if age < 4:
      print("Your admission cost is $0.")
elif age < 18:
      print("Your admission cost is $5.")
else:
      print("Your admission cost is $10.")
```



**Python**并不要求`if-elif`结构后面必须有`else`代码块。



3.一系列独立的`if`语句：

```python
requested_toppings = ['mushrooms','extra cheese']

if 'mushrooms' in requested_toppings:
	print('Add mushrooms.')
if 'extra cheese' in requested_toppings:
	print('Add extra cheese.')
```



如果你只想执行一个代码块，就使用`if-elif-else`结构；如果要运行多个代码块，就使用一系列独立的`if`语句。

### 使用`if`语句处理列表

需要确定列表不是空的。

```python
if requested_toppings:
else:
```



## 字典

**Python**字典能将相关信息关联起来。

```python
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])
```

字典是一系列**键-值**对。每个**键**都与一个值相关联，你可以使用**键**来访问与之相关联的值。



添加**键-值**对:

`alien_0['x_position'] = 0`



由类似对象组成的字典:

```python
favorite_languages = {
	'jen' : 'python',
	'sarah' : 'c',
	'edward' : 'ruby',
	'phil' : 'python'
	}
```



### 遍历字典

#### 遍历所有**键值对**：

```python
user_0 = {
	'user_name' : 'efermi',
	'first' : 'enrico',
	'last' : 'fermi',
	}
for key,value in user_0.items():
	print("\nKey: " + key)
	print("value: " + value)
```



#### 遍历字典中的所有**键**：

方法`keys()`

```python
favorite_languages = {
	'jen' : 'python',
	'sarah' : 'c',
	'edward' : 'ruby',
	'phil' : 'python'
	}
for name in favorite_languages.keys():
	print(name.title())
```

`favorite_languages.key()`返回一个列表，其中包含字典中的所有键。



**按顺序**遍历字典中的所有键：

可以对返回的键进行排序：`sorted(favorite_languages.keys())`



#### **遍历字典中的所有值：**

方法：`values()`

```python
favorite_languages = {
	'jen' : 'python',
	'sarah' : 'c',
	'edward' : 'ruby',
	'phil' : 'python'
	}
for name in favorite_languages.values():
	print(name.title())
```



这种做法可能会产生大量的重复项，

为剔除重复项，可使用集合**`set()`**，集合类似于列表，但每个元素都必须是独一无二的。

```python
favorite_languages = {
	'jen' : 'python',
	'sarah' : 'c',
	'edward' : 'ruby',
	'phil' : 'python'
	}
for name in set(favorite_languages.values()):
	print(name.title())
```



### 嵌套

有时候，需要将一系列字典存储在列表中，或将列表作为值存储在字典中，这称为嵌套。

你可以在**列表中嵌套字典**、**在字典中嵌套列表**甚至**在字典中嵌套字典**。

**在列表中嵌套字典：**

```python
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0,alien_1,alien_2]
for alien_number in range(3,31):
	alien_new = {'color': 'green', 'points': 5}
	aliens.append(alien_new)

for alien in aliens[:30]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
	print(alien)
```



**在字典中存储列表：**

```python
#存储所点比萨的信息
pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'extra cheese'],
	}

#概述所点比萨信息

print("You ordered a " + pizza['crust'] + "with the following toppings:")

for topping in pizza['toppings']:
	print("\t" + topping)
```

每当需要将字典中将一个键关联到多个值时，都可以在字典中嵌套一个列表。

在有关喜欢的编程语言的示例中，如果将每个人的回答都存储在一个列表中，被调查者就可选择多种喜欢的语言：

```python
favorite_languages = {
	'jen' : ['python','ruby'],
	'sarah' : ['c'],
	'edward' : ['ruby','go'],
	'phil' : ['python', 'haskell']
	}
for name, laguages in favorite_languages.items():
	print("\n",name);
	for language in laguages:
		print(language)
```



**在字典中存储字典：**

```python
users = {
	'aeinstein':{
		'first': 'albert',
		'last': 'einstein',
		'location': 'princeton'
		},
	'mcurie':{
		'first': 'marie',
		'last': 'curie',
		'location': 'paris'
		}
	}

for username, user_info in users.items():
	print("\nUsername: " + username)
	full_name = user_info['first'] + ' ' + user_info['last']
	location = user_info['location']
	print("\tFull name: " + full_name.title())
	print("\tLocation: " + location.title())
```

我们首先定义了一个名为`users`的字典，其中包含两个键；与每个键相关联的值都是一个字典，其中包含用户的名、姓和居住地。

请注意，表示每位用户的字典的结构都相同，虽然**Python**并没有这样的要求，但这使得嵌套的字典处理起来更容易。倘若表示每位用户的字典都包含不同的键，`for`循环内部的代码将更复杂。



## 用户输入和`while`循环

### 函数 `input()`的工作原理

此函数让程序暂停运行，等待用户输入一些文本。获取用户输入后，**Python**将其存储在一个变量中，以方便你使用。

例如，下面的程序让用户输入一些文本，再将这些文本呈现给用户：

```python
message = input("Tell me somthing, and I will repeat it back to you: ")
print(message)
```



使用 `int()`来获得数值输入：

```python
age = int(age)
```

`int()`将这个**字符串转换成了数值**。



求模运算符`%`：

```python
>>> 4 % 3
1
>>> 5 % 3
2
```

求模运算符不会指出一个数是另一个数的多少倍，而只指出余数是多少。

如果一个数可被另一个数整除，余数就为0，因此求模运算符返回0。你可利用这一点来判断一个数是奇数还是偶数。



### `while`循环简介

你可以使用`while`循环来数数：

```python
current_number = 1
while current_number <= 5:
	print(current_number)
	current_number += 1
```

注意：`current_number += 1`是 `current_number = current_number + 1`的简写。



#### 让用户选择何时退出：

```python
prompt = input("Tell me somthing, and I will repeat it back to you: ")
prompt += "\nEnter 'quit' to end the program"
message = ""
while message != "quit":
	message = input(prompt)
	print(message)
```



#### 使用标志：

在要求很多条件都满足才继续运行的程序中，可定义一个变量，用于判断整个程序是否处于活动状态，这个变量被称为**标志**。

```python
prompt = input("Tell me somthing, and I will repeat it back to you: ")
prompt += "\nEnter 'quit' to end the program"

active = True
while active:
	message = input(prompt)
if message == 'quit':
	active = False
else:
	print(message)
```



#### 使用`break`退出循环：

要立即退出`while`循环，不再运行循环中余下的代码，也不管条件测试结果如何，可使用`break`语句。

`break`语句用于控制程序流程，可用它来控制哪些代码将执行，哪些代码不执行，从而让程序按你的要求执行你要执行的代码。

```python
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
	city = input(prompt)
if city == 'quit':
	break
else:
	print("I'd love to go to " + city.title() + "!")
```



#### 在循环中使用`continue`：

要返回到循环的开头，并根据条件测试结果决定是否继续执行循环，可使用 `continue`语句。

```python
current_number = 0
while current_number < 10:
	current_number += 1
	if current_number % 2 == 0:
		continue
	print(current_number)
```



#### 避免无限循环：

每个 `while`都必须有停止运行的途径，这样才不会没完没了地执行下去。

下面这个循环将没完没了地运行：

```python
x = 1
while x <= 5:
	print(x)
```

如果程序陷入无限循环，可按**Ctrl + C**，也可以关闭显示程序输出的终端窗口。



### 用while循环来处理列表和字典：

#### 在列表之间移动元素：

可以使用一个 `while`循环，实现列表间元素的移动：

```python
unconfirmed_users = ['alice','brian','candace']
confirmed_users = []

while unconfirmed_users:
	current_user = unconfirmed_users.pop()

	print("Verifying user: " + current_user.title())
	confirmed_users.append(current_user)

for confirmed_user in confirmed_users:
	print(confirmed_user.title())
```



#### 删除包含特定值的所有列表元素：

假设有一个列表，其中包含多个值相同的元素，要删除所有这些元素，可不断运行一个 `while`循环，直到列表中不再包含值 `cat`。

```python
pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)

while 'cat' in pets:
	pets.remove('cat')
print(pets)
```



#### 使用用户输入来填充字典：

```python
responses = {}
polling_active = True

while polling_active:
	name = input("\nWhat is your name? ")
	response = input("Which mountain would you like to climb someday? ")

	responses[name] = response

	repeat = input("Would you like to let another person respond? (yes/ no) ")
	if repeat == 'no':
		polling_active = False

print("\n--- Poll Results ---") 
for name, response in responses.items():
	print(name + " would like to climb " + response + ".")
```



## 函数

### 定义函数

下面定义一个打印问候语的简单函数，名为`greet_user()`：

```python
def greet_user():
	print("Hello!")

greet_user()
```

#### 向函数传递信息：

```python
def greet_user(username):
	print("Hello! " + username.title())

greet_user('ma yicheng')
```



#### 实参和形参：

在上面的代码块中，`username`是一个形参，`ma yicheng`是一个实参。实参是调用函数时传递给函数的信息。



### 传递实参

#### 位置实参

调用函数时，**Python**必须将函数调用中的每个实参都关联到函数定义中的一个形参。为此，最简单的关联方式是基于实参的顺序。这种关联方式被称为位置实参。

```python
def describe_pet(animal_type, pet_name):
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
```

可调用函数任意次。

位置实参的顺序很重要。

#### 关键字实参：

其是传递给函数的**名称—值**对。直接在实参中将名称和值关联起来了。

```python
def describe_pet(animal_type, pet_name):
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(animal_type = 'hamster', pet_name = 'harry')
```

关键字实参的顺序无关紧要，因为**Python**知道各个值该存储到哪个形参中。下面两个函数调用是等效的：

```python
describe_pet(animal_type = 'hamster', pet_name = 'harry')
describe_pet( pet_name = 'harry'，animal_type = 'hamster')
```

**注意** 使用关键字实参时，务必准确地指定函数定义中的形参名。

#### 默认值：

```python
def describe_pet(pet_name, animal_type='dog');
describe_pet('willie')
```

如果你发现调用`describe_pet()`时，描述的大都是小狗，就可将形参`animal_type`的默认值设置为`dog`。

**注意** 使用默认值时，在形参列表中必须先列出没有默认值的形参，再列出有默认值的实参。这让**Python**依然能够正确地解读位置实参。

#### 

**注意** 使用哪种调用方式无关紧要，只要函数调用能生成你希望的输出就行。使用对你来说最容易理解的调用方式即可。



#### 避免实参错误：

例如，如果调用函数`describe_pet()`没有指定任何实参，结果将出错。



### 返回值

#### 返回简单值

```python
def get_formatted_name(first_name, last_name):
	full_name = first_name + ' ' + last_name
	return full_name.title()
me = get_formatted_name('yicheng','ma')
print(me)
```

调用返回值的函数时，需要提供一个变量，用于存储返回的值。

#### 让实参变成可选的

有时候，需要让实参变成可选的，这样使用函数的人就只需在必要时才提供额外的信息，可使用默认值来让实参变成可选的。

在没有提供中间名时依然可行，可给实参`middle_name`指定一个默认值——空字符串，并将其移到形参列表的末尾。

```python
def get_formatted_name(first_name, last_name, middle_name='')：
		if middle_name:
    		full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
      	full_name = first_name + ' ' + last_name
    return full_name.title()
```

#### 返回字典

函数可返回任何类型的值，包括列表和字典等较复杂的数据结构。

```python
def build_person(first_name, last_name):
	person = {'first': first_name, 'last': last_name}
	return person

musician = build_person('jimi', 'hendrix')
print(musician)
```

#### 结合使用函数和`while`循环

```python
def get_formatted_name(first_name, last_name):
  	full_name = first_name + ' ' + last_name
    return full_name.title()
while True:
  	print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
   	
    f_name = input("First name: ")
    if f_name == 'q':
    		break
    l_name = input("Last name: ")
   	if l_name == 'q':
      	break
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
```

现在，这个程序将不断地问候，直到用户输入的姓或名为 `q`



### 传递列表

向函数传递列表很有用，这种列表包含的可能是名字、数字或更复杂的对象（如字典）。将列表传递给函数后，函数就能直接访问其内容。

```python
def greet_users(names):
	for name in names:
		msg = "Hello, " + name.title() + "!"
		print(msg)

usernames = ['hannah','ty','margot']
greet_users(usernames)
```

#### 在函数中修改列表：

将列表传递给函数后，函数就可对其进行修改。在函数中对这个列表所做的任何修改都是永久性的，这让你能够高效地处理大量的数据。

```python
def print_models(unprinted_designs, completed_models):
  	while unprinted_designs:
      	current_design = unprinted_designs.pop()
        
        print("Pringing model: " + current_design)
        completed_models.append(current_design)
def show_completed_models(completed_models):
  	print("\nThe following models have been printed:")
    for completed_model in completed_models:
      	print(completed_model)
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
```

#### 禁止函数修改列表：

为了留存原来的列表，可向函数传递列表的副本而不是原件；这样函数所做的任何修改都只影响副本，而丝毫不影响原件。

切片表示法`[:]`创建列表的副本。

例如：

```python
print_models(unprinted_designs[:],completed_models)
```

这样函数`print_models()`依然能完成工作，因为它获得了所有未打印的设计的名称。



#### 传递任意数量的实参：

有时候，你预先不知道函数需要接受多少个实参，好在**Python**允许函数从调用语句中收集任意数量的实参。

```python
def make_pizza(*toppings):
	print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')
```

形参名`*toppings`中的星号让**Python**创建一个名为`toppings`的空元组，并将收到的所有值都封装到这个元组中。

不管函数收到的实参是多少个，这种语法都管用。



##### 结合使用位置实参和任意数量实参：

如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最后。**Python**先匹配位置实参和关键字实参，再将余下的实参都收集到最后一个形参中。

例如，如果前面的函数还需要一个表示比萨尺寸的实参，必须将该形参放在形参`*toppings`的前面：

```python
def make_pizza(size, *toppings)
```



##### 使用任意数量的关键字实参：

有时候，需要接受任意数量的实参，但预先不知道传递给函数的会是什么样的信息。在这种情况下，可将函数编写成能够接受任意数量的键—值对——调用语句提供了多少就接受多少。

```python
def build_profile(first, last, **user_info):
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile
user_profile = build_profile('albert','einstein',location = 'princeton',field = 'phycics')
print(user_profile)
```

形参`**user_info`中的两个星号让**Python**创建一个名为`user_info`的空字典，并将收到的所有**名称—值**对都封装到这个字典中。在这个函数中，可以想像访问其他字典那样访问`user_info`中的**名称—值**对。



### 将函数存储在模块中

函数的优点之一是，使用它们可将代码块与主程序分离。通过给函数指定描述性名称，可让主程序容易理解得多。还可更进一步，将函数存储在被称为模块的独立文件中，再将模块导入到主程序中。`import`语句允许在当前运行的程序文件中使用模块中的代码。

#### 导入整个模块

**pizza.py**

```python
def make_pizza(*toppings):
	print(toppings)
```

**making_pizzas.py**

```python
import pizza
pizza.make_pizza('mushroom')
```

只需编写一条`import`语句并在其中指定模块名，就可在程序中使用该模块中的所有函数。

#### 导入特定函数

```python
from pizza import make_pizza

make_pizza(16, 'pepperoni')
```

若使用这种语法，调用函数时就无需使用句点。由于我们在`import`语句中显示地导入了函数`make_pizza()`，因此调用它时只需指定其名称。

#### 使用`as`给函数指定别名

下面给函数`make_pizza()`指定了别名`mp()`。这是在`import`语句中使用`make_pizza as mp`实现的，关键字`as`将函数重命名为你提供的别名：

```python
from pizza import make_pizza as mp

mp(16, 'pepperoni')
```

#### 使用`as`给模块指定别名

还可以给模块指定别名。通过给模块指定简单的别名（如给模块`pizza`指定别名`p`），让你能够更轻松地调用模块中的函数。

```python
import pizza as p

p.make_pizza(16,'pepperoni')
```

#### 导入模块中的所有函数（几乎不用）

使用星号（`*`）运算符可让**Python**导入模块中的所有函数：

```python
from pizza import *

make_pizza(16, 'pepperoni')
```

`import`语句中的星号让**Python**将模块`pizza`中的每个函数都复制到这个程序文件中。由于导入了每个函数，可通过名称来调用每个函数，而无需使用句点表示法。



## 类

**面向对象的编程**是最有效的软件编写方法之一。在面向对象编程中，你编写表示现实世界中的事物和情景的类，并基于这些类来创建对象。编写类时，你定义的一大类对象都有的通用行为。基于类创建对象时，每个对象都自动具备这种通用行为，然后可根据需要赋予每个对象独特的个性。使用面向对象编程可模拟现实情景，其逼真程度达到了令人惊讶的地步。

根据类来创建对象被称为实例化。

### 创建和使用类

使用类几乎可以模拟任何东西。下面来编写一个表示小狗的简单类`Dog`——它表示的不是特定小狗，而是任何小狗。

#### 创建`Dog`类

根据`Dog`类创建的每个实例都将存储名字和年龄，且被赋予蹲下（`sit()`）和打滚（`roll_over()`）的能力。

```python
class Dog():
	"""一次模拟小狗的简单尝试"""

	def __init__(self, name, age):
		"""初始化属性name和age"""
		self.name = name
		self.age = age

	def sit(self):
		"""模拟小狗被命令时蹲下"""
		print(self.name.title() + " is now sitting.")

	def roll_over(self):
		"""模拟小狗被命令时蹲下"""
		print(self.name.title() + " rolled over!")

```

##### 方法`__int__()`

类中的函数称为方法；`__int__()`是一个特殊的方法，每当根据`Dog`类创建新实例时，**Python**都会自动运行它。

形参`self`必不可少，必须位于其他形参的前面。

#### 根据类创建实例

可将类视为如何创建实例的说明。`Dog`类是一系列说明，让**Python**知道如何创建表示特定小狗的实例。

```python
class Dog():
  	--snip--
my_dog = Dog('willie',6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " year old.")
```

我们通常可认为首字母大写的名称（如`Dog`）指的是类，而小写的名称（如`my_dog`）指的是根据类创建的实例。

##### 访问属性

```python
my_dog.name
```

##### 调用方法

```python
class Dog():
  	--snip--
my_dog = Dog('willie',6)
my_dog.sit()
my_dog.roll_over()
```

##### 创建多个实例

可按需求根据类创建任意数量的实例。

```python
class Dog():
  	--snip--
my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)
```

### 使用类和实例

可以使用类来模拟现实世界中的很多情景。类编写好后，大部分时间将花在使用根据类创建的实例上。

#### `Car`类

编写一个表示汽车的类：

```python
class Car():

	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year

	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
```

#### 给属性指定默认值

类中的每个属性都必须有初始值，哪怕这个值是0或空字符串。在有些情况下，如设置默认值时，在方法`__int()__`内指定这种初始值是可行的；如果你对某个属性这样做了，就无需包含为它提供初始值的形参。

下面来添加一个名为`odometer_reading`的属性，其初始值总是为0。我们还添加了一个名为`read_odometer()`的方法，用于读取汽车的里程表。

```python
class Car():

	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year
    self.odometer_reading = 0

	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()
  
  def read_odometer(self):
    print("This car has " + str(self.odometer_reading) + " miles on it.")

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
```

#### 修改属性的值

可以通过三种不同的方式：直接通过实例进行修改；通过方法进行设置；通过方法进行递增（增加特定值）。

##### 直接修改属性的值

```python
class Car():
  --snip--

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
```

有时候需要像这样直接访问属性，但其他时候需要编写对属性进行更新的方法。

##### 通过方法修改属性的值

如果有替你更新属性的方法，将大有裨益。这样，你就无需直接访问属性，而可将值传递给一个方法，由它在内部进行更新。

```python
class Car():
  --snip--
  
  def update_odometer(self, mileage):
    self.odometer_reading = mileage
   	
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()
```

对`Car`类所做的唯一修改是添加了方法`update_odometer()`。这个方法接受一个里程值，并将其存储到`self.odometer()`中。

可对方法`update_odometer()`进行扩展，使其在修改里程表读数时做些额外工作。例如，添加一些逻辑，禁止任何人将里程表读数往回调：

```python
def update_odometer(self, mileage):
  if mileage >= self.odometer_reading:
    self.odometer_reading = mileage
  else:
    print("You can't roll back an odometer!")
```

##### 通过方法对属性的值进行递增

有时候需要将属性的值递增特定的量，而不是将其设置为全新的值。

```python
class Car():
  --snip--
  
  def update_odometer(self, mileage):
    --snip--
  
  def increment_odometer(self, miles):
    self.odometer_reading += miles

my_used_car = Car('subaru', 'outback', 2013)

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
```



### 继承

编写类时，并非总是要从空白开始。如果你要编写的类是另一个现成的类的特殊版本，可使用继承。一个类继承另一个类时，它将自动获得另一个类的所有属性和方法；原有的类称为父类，而新类称为子类。子类继承父类的所有属性和方法，同时还定义自己的属性和方法。

#### 子类的方法`__int__()`

创建子类时，父类必须包含在当前文件中，且位于子类前面。定义子类时，必须在括号内指定父类的名称。

```python
class Car():
  --snip--

class ElectricCar(Car):
  def __int__(self, make, model, year):
    super().__int__(make,model,year)

my_tesla = ElectricCar('tesla', 'model s', 2016)
```

`super()`是一个特殊函数，帮助**Python**将父类和子类关联起来。这行代码让**Python**调用`ElectricCar`的父类方法`__int__()`，让`Electric`实例包含父类的所有属性。父类也称为超类（**superclass**）。

#### 给子类定义属性和方法

让一个类继承另一个类后，可添加区分子类和父类所需的新属性和方法。

```python
class ElectricCar(Car):
  def __int__(self, make, model, year):
    super().__int__(make,model,year)
    self.battery_size = 70
  
 	def describe_battery(self):
    print("This car has a " + str(self.battery_size) + "-kWh battery.")
```

#### 重写父类的方法

对于父类的方法，只要它不符合子类模拟实物的行为，都可对其进行重写。为此，可在子类中定义一个这样的方法，即它与要重写的父类方法同名。**Python**将不会考虑这个父类方法，而只关注你在子类中定义的相应方法。

假设`Car`类有一个名为`fill_gas_tank()`的方法，它对全电动汽车来说毫无意义，因此你可能想重写它。下面演示了一种重写方式：

```python
def ElectricCar(Car):
  --snip--
  
  def fill_gas_tank():
    print("This car doesn't need a gas tank!")
```

使用继承时，可让子类保留父类那里继承而来的精华，并剔除不需要的糟粕。

#### 将实例用作属性

```python
class Battery():
  def __int__(self,battery_size=70):
    self.battery_size = battery_size
  
  def describe_battery(self):
    print("")

class ElectricCar(Car):
  
  def __int__(self, make, model, year):
    super().__int__(make, model, year)
    self.battery = Battery()
    
my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
```

### 导入类

**Python**允许将类存储在模块中，然后在主程序中导入所需的模块。

#### 导入单个类

下面创建一个只包含`Car`类的模块。

**car.py**

```python
"""一个可用于表示汽车的类"""

class Car():
	"""一次模拟汽车的简单尝试"""

	def __init__(self,make,model,year):
		"""初始化描述汽车的属性"""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		"""返回整洁的描述性名称"""
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def read_odometer(self):
		"""打印一条消息，指出汽车的里程"""
		print("This car has " + str(self.odometer_reading) + " miles on it.")

	def update_odometer(self, mileage):
		"""
		将里程表读数设置为指定的值
		拒绝将里程表往回拨
		"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")

	def increment_odometer(self,miles):
		"""将里程表读数增加指定的量"""
		self.odometer_reading += miles
```

下面来创建另一个文件——**my_car.py**，在其中导入`Car`类并创建其实例。

**my_car.py**

```python
from car import Car

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
```

#### 在一个模块中存储多个类

虽然同一个模块中的类之间应存在某种相关性，但可根据需要在一个模块中存储任意数量的类。

类`Battery`和`ElectricCar`都可帮助模拟汽车，因此可将它们都加入模块`car.py`中。

#### 从一个模块中导入多个类

```python
from car import Car, ElectricCar
```

#### 导入整个模块（推荐）

还可以导入整个模块，再使用句点表示法访问需要的类。

```python
import car

my_beetle = car.Car('volkswagen', 'beetle', 2016)
my_tesla = car.ElectricCar('tesla', 'roadster', 2016)
```

#### 导入模块中所有的类（不推荐）

要导入模块中所有的类，使用下面的语法：

```python
from module_name import *
```

#### 在一个模块中导入另一个模块

有时，需将类分散到多个模块中，以免模块太大。将类存储在多个模块中时，可能会发现一个模块中的类依赖于另一个模块中的类。在这种情况下，可在前一个模块中导入必要的类。



### Python标准库

是一组模块，安装**Python**都包含它。可使用标准库中的任何函数和类，为此只需在程序开头包含一条简单的`import`语句。

还可以从其他地方下载外部模块。许多项目都需要使用外部模块。



### 类编码风格

类名应采用**驼峰命名法**。将类名中的每个单词的首字母都大写。而不使用下划线。实例名和模块名都采用小写格式，并在单词之间加上下划线。

应在每个类定义后面包含一个文档字符串。`“”“”“”`

每个模块也都应包含一个文档字符串，对其中的类可用于做什么进行描述。`“”“”“”`



## 文件和异常

### 从文件中读取数据

文本文件可存储的数据多得难以置信，每当需要分析或修改存储在文件中的信息时，读取文件都很有用，对数据分析应用程序来说尤其如此。

#### 读取整个文件

```python
file_path = '/Users/mayicheng/Downloads/文稿/。txt/shakespeare.txt'
with open(file_path) as file_object:
  contents = file_object.read()
  print(contents.rstrip())
```

如上所示为用**绝对文件路径**检索文件。

#### 逐行读取

读取文件时，常常需要检查其中的每一行。要以每次一行的方式检查文件，可对文件对象使用`for`循环：

```python
filename = '/Users/mayicheng/Downloads/文稿/。txt/shakespeare.txt'

with open(filename) as file_object:
  for line in file_object:
    print(line.rstrip())
```

#### 创建一个包含文件各行内容的列表

使用关键字`with`时，`open()`返回的文件对象只在`with`代码块内可用。如果要在`with`代码块外访问文件的内容，可在`with`代码块内将文件的各行存储在一个列表中，并在`with`代码块外使用该列表。

```python
filename = '/Users/mayicheng/Downloads/文稿/。txt/shakespeare.txt'

with open(filename) as file_object:
  lines = file_object.readlines()

for line in lines:
  print(line.rstrip())
```

#### 使用文件的内容

```python
file_path = '/Users/mayicheng/Downloads/文稿/。txt/shakespeare.txt'
with open(file_path) as file_object:
  lines = file_object.readlines()

shakespeares_string = ''
for line in lines:
  shakespeares_string += line.strip()

print(shakespeares_string)
print(len(shakespeares_string))
```

**注意**	读取文本文件时，**Python**将其中的所有文本都解读为字符串。如果你读取的是数字，并要将其作为数值使用，就必须使用函数`int()`将其转换为整数，或使用函数`float()`将其转换为浮点数。

#### `Shakespeare.txt`文件中是否包含`Romeo`

```python
file_path = '/Users/mayicheng/Downloads/文稿/。txt/shakespeare.txt'
with open(file_path) as file_object:
  lines = file_object.readlines()

shakespeares_string = ''
for line in lines:
  shakespeares_string += line.strip()

if 'Romeo' in shakespeares_string:
  print('Yes') 
```

### 写入文件

保存数据最简单的方式之一是将其写入到文件中。

#### 写入空文件

要将文本写入文件，在调用`open()`时需要提供另一个实参，告诉**Python**你要写入打开的文件。

```python
filename = 'programming.txt'

with open(filename, 'w') as file_object:
	file_object.write("I love programming.")
```

打开文件时，可指定读取模式`'r'`，写入模式`'w'`，附加模式 `'a'`，或能够读取或写入文件的模式 `'r+'`。如果省略模式实参，**Python**将默认以只读模式打开文件。

**注意**	以写入 `w`模式打开文件时千万要小心，因为如果指定的文件已经存在，**Python**将在返回文件对象前清空该文件。

**注意**	**Python**只能将字符串写入文本文件。要将数值数据存储到文本文件中，必须先使用函数`str()`将其转换为字符串格式。

#### 写入多行

函数`write()`不会在写入的文本末尾添加换行符，因此如果写入多行时没有指定换行符，文件格式会出乎意料。

故，要让每个字符串都单独占一行，需要在`write()`语句中包含换行符：

```python
filename = 'programming.txt'

with open(filename, 'w') as file_object:
	file_object.write("I love programming.\n")
  file_object.write("I love creating new game.\n")
```

#### 附加到文件

若要给文件添加内容，可以以**附加模式**打开文件。

```python
filename = 'programming.txt'

with open(filename, 'a') as file_object:
  file_object.write("I also love finding meaning in large datasets.\n")
```



### 异常

**Python**使用被称为**异常**的特殊对象来管理程序执行期间发生的错误。每当发生不知所措的错误时，它都会创建一个异常对象。异常使用`try-except`代码块处理。

#### 处理**`ZeroDivisionError`**异常

```python
print(5/0)
```

使用`try-except`代码块：

```python
try:
  	print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
```

#### 使用异常避免崩溃

发生错误时，如果程序有工作未完成，妥善处理错误很重要。这种错误经常会出现在要求用户提供输入的程序；如果程序能妥善处理无效输入，就能再提示用户提供输入，而不至于崩溃。

#### `else`代码块

通过将可能引发错误的代码放在`try-except`代码块中，可提高这个程序抵御错误的能力。

```python
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
	first_number = input("\nFirst number: ")
	if first_number == 'q':
		break
	second_number = input("Second number: ")
	if second_number == 'q':
		break
	try:
		answer = int(first_number) / int(second_number)
	except ZeroDivisionError:
		print("You can't divide by 0!")
	else:
		print(answer)
```

通过预测可能发生错误的代码，可编写健壮的程序，它们即使面临无效数据或缺少资源，也能继续运行，从而能够抵御无意的用户错误和恶意攻击。

#### 处理`FileNotFoundError`异常

使用文件时，一种常见的问题是找不到文件。这种问题可以使用`try-except`代码块以直观的方式进行处理。

```python
filename = 'alice.txt'

try:
	with open(filename) as f_obj:
		contents = f_obj.read()
except FileNotFoundError:
	msg = "Sorry, the file " + filename + " does not exist."
	print(msg)
```

#### 分析文本

使用方法`split()`，它根据一个字符串创建一个单词列表。其以空格为分隔符将字符串拆成多个部分，并将这些部分都存储到一个列表中。结果是一个包含字符串中所有单词的列表，虽然有些单词可能包含标点。

为计算包含多少单词，对整个文本文件用`split()`，再计算得到的列表包含多少元素。

```python
file_path = '/Users/mayicheng/Downloads/文稿/。txt/shakespeare.txt'
try:
  with open(file_path) as file_object:
    contents = file_object.read()
except:
  msg = 'Sorry, the file does not exit.'
else:
  words = contents.split()
  num_words = len(words)
  print(num_words)
```

#### 使用多个文件

将上述程序大部分代码移到一个函数中：

```python
def count_words(filename):
	try:
		with open(filename) as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		msg = "can't find"
		print(msg)
	else:
		words = contents.split()
		num_words = len(words)
	return num_words

numb = count_words('/Users/mayicheng/Downloads/文稿/。txt/shakespeare.txt')
print(numb)
```

#### 失败时一声不吭

要让程序在失败时一声不吭，可像通常那样编写`try`代码块，但在`except`代码块中明确地告诉**Python**什么都不要做。**Python**有一个`pass`语句，可在代码块中使用它来让**Python**什么都不要做。

```python
try:
  --snip--
except FileNotFoundError:
  pass
```



### 存储数据

不管专注的是什么，程序都把用户提供的信息存储在列表和字典等数据结构中。一种简单的方式是使用模块`json`来存储数据。

模块`json`让你能够将简单的**Python**数据结构转存储到文件中，并在程序再次运行时加载该文件中的数据。你还可以使用`json`在**Python**程序之间分享数据。更重要的是，**JSON**数据格式并非**Python**专用的，这让你能够将此格式存储的数据与使用其他编程语言的人分享。

**JSON（JavaScript Object Notion）**格式最初是为**JavaScript**开发的，但随后成了一种常见的格式，被包括**Python**在内的众多语言采用。

#### 使用`json.dump()`和`json.load()`

```python
import json

number = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
  json.dump(numbers, f_obj)
```

```python
import json

filename = 'numbers.json'
with open(filename) as f_obj:
  numbers = json.load(f_obj)

print(numbers)
```

#### 保存和读取用户生成的数据

对于用户生成的数据，使用`json`保存它们大有裨益，因为如果不以某种方式进行存储，等程序停止运行时用户的信息将丢失。

存储用户的名字：

```python
import json

username = input("What's your name?")

filename = 'user.json'
with open(filename,'w') as f_obj:
	json.dump(username, f_obj)
	print("we will remember you when you come back, " + username + '!')
```

向其名字被存储的用户发出问候：

```python
import json

filename = 'user.json'

with open(filename) as f_obj:
	username = json.load(f_obj)
	print("Welcome back, " + username + '!')
```

将两程序合并到一个程序：

```python
import json

filename = 'username.json'
try:
  with open(filename) as f_obj:
    username = json.load(f_obj)
  except FileNotFoundError:
    username = input("What's your name?")
    with open(filename,'w') as f_obj:
      json.dump(username,f_obj)
      print("We'll remember you when you come back, " + username + "!")
 	else:
    print("Welcome back, " + username + "!") 
```

#### 重构

将代码划分为一系列完成具体工作的函数的过程称为重构。重构让代码更清晰、更易于理解、更容易扩展。



###### **注**	此文件由过去的Myc创建，仅作参考。

