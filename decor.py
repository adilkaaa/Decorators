#1
# def main():
#     print('Я главная функция')
#     def f2():
#         print('Я ложенная функция')
#     f2()
# main()

# func_2()

#2
# dictionary = {
#     'a':1,
#     'b':2,
#     'c':3
# }

# def get_keys_values(d):
#     a = tuple(d.values())
#     b = tuple(d.keys())
#     return a,b

# print(get_keys_values(dictionary))


#3
# def is_prime(n):
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     return True if n!=1 and n>=-1 else False

# print(is_prime(int(input('is number prime: '))))


#4
# def decor(f):
#     def delete_duplicate():
#         l = f()
#         return list(set(l))
#     return delete_duplicate

# @decor
# def create_100_num():
#     from random import randint
#     l = [randint(10,50) for i in range(100)]
#     return l

# print(create_100_num())



#5

# log = input('login: ')
# password = input('password: ')

# def decor(f,*args):
    
#     def shifr(*args):
#         shifr_log = ''
#         shifr_password = ''
#         log, password = f(*args)
#         all_of_them = zip(log,password)
#         for l,p in all_of_them:
#             shifr_log+=str(ord(l))+'*'
#             shifr_password+=str(ord(p)) +'*'
#         return shifr_log, shifr_password
#     return shifr

# @decor
# def login(l,p):
#     return l,p

# print(login(log,password))

#6


# def add(a,b):
#     return a+b

# def substract(a,b):
#     return a-b

# def multiply(a,b):
#     return a*b

# def divide(a,b):
#     return a/b



