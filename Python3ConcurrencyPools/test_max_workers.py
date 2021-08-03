import time
from concurrent.futures import ThreadPoolExecutor

a = None
b = None
c = None
d = None

def wait_on_d():
    global d
    time.sleep(5)
##    print(b.result())  # b will never complete because it is waiting on a.
    d = "D" 

def wait_on_c():
    global c
    time.sleep(5)
##    print(b.result())  # b will never complete because it is waiting on a.
    c = "C"

def wait_on_b():
    global b
    time.sleep(5)
##    print(b.result())  # b will never complete because it is waiting on a.
    b = "B"

def wait_on_a():
    global a
    time.sleep(5)
##    print(a.result())  # a will never complete because it is waiting on b.
    a = "A"


executor = ThreadPoolExecutor(max_workers=2)
a1 = executor.submit(wait_on_a)
b1 = executor.submit(wait_on_b)
c1 = executor.submit(wait_on_c)
d1 = executor.submit(wait_on_d)
s = 0
while (a is None) or (b is None) or (c is None) or (d is None):
    print(f"a:{a}; b:{b}; c:{c}; d:{d} - elapsed {s}s")
    time.sleep(1)
    s += 1
print(f"a:{a}; b:{b}; c:{c}; d:{d} - elapsed {s}s")
