print(issubclass(bool, int))
print(int(True))
print(int(True)+int(True))
print(int(False))
print(hex(id(True)))
print(hex(id(4>3)))
print((4>3) == True)
print((4>3) is True)
print()

print(True == 1)
print(True is 1)
print()
print(hex(id(True)))
print(hex(id(1)))
print()

print(3 == False)
print('4' == 4)
print()

a, b = 1, 2
print(a)
print(b)
print(a > b, b < a)
print(a > b, b == 2)
print(True > False)
x = True + True
print(x)
print(100 * False)
print()

result = ''
if result:
    print('result is not empty')
else:
    print('result is not empty')
print()

result = ''
if bool(result):
    print('result is not empty')
else:
    print('result is not empty')
print()



var1 = ''
if var1:
    print('var1 truthy value is True')
else:
    print('var1 truthy value is False')
print()

var1 = 'ss'
if var1:
    print('var1 truthy value is True')
else:
    print('var1 truthy value is False')
print()

var1 = []
if var1:
    print('var1 truthy value is True')
else:
    print('var1 truthy value is False')
print()

var1 = [1, 2]
if var1:
    print('var1 truthy value is True')
else:
    print('var1 truthy value is False')
print()


var1 = 0
if var1:
    print('var1 truthy value is True')
else:
    print('var1 truthy value is False')
print()

var1 = 1
if var1:
    print('var1 truthy value is True')
else:
    print('var1 truthy value is False')
print()


var1 = 0.0
if var1:
    print('var1 truthy value is True')
else:
    print('var1 truthy value is False')
print()

var1 = 1.0
if var1:
    print('var1 truthy value is True')
else:
    print('var1 truthy value is False')
print()


