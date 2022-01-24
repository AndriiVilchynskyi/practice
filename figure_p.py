# def logger(func):
#     def inner(*args, **kwargs):
#         "This decorator dumps out the arguments passed to a function before calling it"
#         b = [str(x) for x in args]
#         b = ", ".join(b)
#         kwargsnames = ""
#         for x in kwargs.values():
#             kwargsnames += str(x) + ", "
#         kwargsnames = kwargsnames[:-2]
#         fname = func.__name__
#         print(f"Executing of function {fname} with arguments {b}{kwargsnames}...")
#         return func(args, **kwargs)
#     return inner
#
#
# @logger
# def concat(*args, **kwargs):
#     a = ""
#     for x in args:
#         for j in x:
#             a += str(j)
#     for x in kwargs.values():
#         a += str(x)
#     return a
#
#
# print(concat('first string',1, "asfasf", second=2, third='second string'))
#
#
#
#
# def function(a):
#     a = [3, 4]
#     print(a, end = " ")
#
# a = [1,2]
# function(a)
# print(a)
# def outer():
#     massage = "outer string"
#     def inner():
#         nonlocal massage
#         massage = "inner string"
#     inner()
#     return massage
#
# print(outer())

#
# def function(item, list = []):
#     list.append(item)
#     print(list, end = " ")
# function(1)
# function(2)
def add_value(a):
    global a
    a +=1
    return a

b = 10
add_value(b)
print(b)