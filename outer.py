# def outer(name):
#     def inner():
#         print(f"Hello, {name}!")
#     return inner
#
# a = outer("Andriy")
# a()
#

def benchmark(func):
    import time
    def wrapper(*args,**kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print(f"[*] Execution time: {end-start}sec.")
        return return_value
    return wrapper

def fetch_webpage(url):
    import requests
    webpage = requests.get(url)
    return webpage.txt
webpage = fetch_webpage("https://google.com.ua")
print(webpage)
print(benchmark(fetch_webpage("...")))
print(benchmark(len)("Hello"))