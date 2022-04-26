# Utwórz dekorator @timepassed mierzący czas działania dowolnej funkcji.

import time

def timepassed(func):
    def inside():
        start = time.time()
        func()
        end = time.time()
        return end - start

    return inside

@timepassed
def daily_news():
    return 'important'

@timepassed
def smart_news():
    return 'smart'


print(daily_news())

print(smart_news())