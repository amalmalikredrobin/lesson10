# i = 0
# while i <= 10:
#     if i % 2 == 1: break
#     print(i)
#     i+=1

# a = int(input('Enter 1st number: '))
# b = int(input('Enter 2nd number. Note that you cannot use 0: '))

# if b == 0:
#     i = 1
#     while True:
#         if i > 3:
#             print('Stupif asshole. Do not you know math?')
#         else: print ('Please enter non-zero value')
#         b = int(input('Enter 2nd number: Note that you cannot use 0'))
#         if b != 0:
#             print(a / b)
#             break
#         i+=1
# else:
#     print(a / b)


# a = int(input('Enter 1st number: '))
# b = int(input('Enter 2nd number. Note that you cannot use 0: '))
# while True:
#     b = int(input('Enter 2nd number. Note that you cannot use 0: '))
#     try:
#         print(a / b)
#     except:
#         print('Please enter non-zero value')

# a = int(input('Enter 1st number: '))
# i = 1
# while True:
#     b = int(input('Enter 2nd number. Note that you cannot use 0: '))
#     try:
#         print(a / b)
#         break
#     except:
#         if i > 3: print('Stupid asshole. Do not know you math?')
#         else: print('Please enter non-zero value')
#     i+=1


# a = int(input('Enter 1st number: '))
# i = 1
# while True:
#     b = int(input('Enter 2nd number. Note that you cannot use 0: '))
#     try:
#         print(a / b)
#         break
#     except(TypeError, ZeroDivisionError):
#         if i > 3: print('Stupid asshole. Do not know you math?')
#         else: print('Please enter non-zero value')
#     i+=1


# a = int(input('Enter 1st number: '))
# i = 1
# while True:
#     b = int(input('Enter 2nd number. Note that you cannot use 0: '))
#     try:
#         print(a / b)
#         break
#     except TypeError:
#         if i > 3: print('Stupid asshole. Do not know you math?')
#         else: print('Please enter non-zero value')
#     i+=1

while True:
    a = int(input('Enter positive number: '))
    if a > 0: breakelse: print('You were asked to enter positive number: ')

while True:
    try:
        a = int(input('Enter positive number: '))
        if a < 0: roise ValueError('You were asked to enter positive number: ')
        else: break
    except ValueError as ve:
        print(ve)


