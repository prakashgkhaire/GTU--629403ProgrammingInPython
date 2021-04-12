# Python program to swap two variables

# To take inputs from the user
x = input('Enter value of x: ')
y = input('Enter value of y: ')

# create a temporary variable and swap the values
x = x + y
y = x - y
x = x - y

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))
