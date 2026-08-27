

def hi():
    '''
    this is my documenatation
    :return:
    '''
    pass

# help(hi)

# 1 star
def greeting():
    '''
    printing hello
    :return: None
    '''
    print('hello, danny')

d = {1: 'a'}
res = d.pop(1)  # return value
a = [4,3]
a.sort()  # inplace -- return None

print(res)

greeting()

# 5 stars
def say_hello(name="incognito"):
    '''
    say hello to user
    :param name: name of the user to say hello. default is "incognito"
    :return: None
    '''
    print('Hello,', name)

danny = "Danny"
mor = "Mor"
# Hello, Danny
# Hello, Mor
say_hello()  # parameter = None
say_hello(danny)
say_hello(mor)
say_hello("John")

# user_name = input("Enter your name: ")
# say_hello(user_name)

# def print_square
#   get parameter x. default = 0
#   print x**2
#   create doc string
#   view the docstring
# call the function with 0, 5, 10, None
def print_square(x=0):
    '''
    printing square
    :param x:number
    :return: None
    '''
    print(x**2)
print_square()
print_square(x=0)
print_square(5)
print_square(10)

def add(x=0, y=0):
    '''
    add two numbers
    :param x: 1st number
    :param y: 2nd number
    :return:  sum of x+y
    '''
    # global sum_xy  # bad
    sum_xy = x + y
    return sum_xy


result = add(x=5, y=10)
print('add returned', result)
print(add(5, 10))
# print(sum_xy)

# rectangle_area
# width, height. no default
# return area . width*height
#   create doc string
#   view the docstring
# call the function with (5, 10) , (10, 10), (7.5, 12) and print the result
def rectangle_area(width, height):
    '''
    calculate area of rectangle
    :param width: width of rectangle
    :param height: height of rectangle
    :return: area of rectangle
    '''
    return width * height

result = rectangle_area(width=5, height=10)
print(f'area width=5 height=10 ==> {result}')
print('area width=7.5 height=12 ==>', rectangle_area(7.5, height=12))

def max_number(a=0, b=0):
    # 1
    if a > b:
        return a
    else:
        return b

    # 2 -- same
    # if a > b:
    #     return a
    # return b

print(max_number(10, 9))

# def get_even_odd
# get parameter a. default = 0
# if a % 2 == 0: return "zugi" ("even")
#         otherwise: return "e-zugi" ("odd")
# add docstring
# try it with 0, 2, 7, 11, -3
def get_even_odd(a=0):
    '''
    get even or odd number
    :param a:
    :return: even or odd
    '''
    if a % 2 == 0:
        return "even"
    return "odd"
print(get_even_odd(0))
print(get_even_odd(2))
print(get_even_odd(7))
print(get_even_odd(11))
print(get_even_odd(-3))

def count_letters(text):
    '''
    count letters
    :param text: text phrase
    :return: dict of count of letters
    '''
    d = {}
    for c in text:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

print(count_letters('missiiiissippi'))  #  {'m': 1, 'i': 7, 's': 4, 'p': 2}
print(count_letters('incognito'))




