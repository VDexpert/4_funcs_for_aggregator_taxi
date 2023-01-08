from functools import wraps
import time

def universal_cache(cache2file = False, cache_minutes = 10):
    """Декаоратор, который кэширует результаты вложенной функции inner."""
    def wrapper(func):
        cache_result = {}
        timer = time.time()
        @wraps(func)
        def inner(route, comf_class, additions, *args, **kwargs):
            nonlocal timer
            format_arguments = f"({route}, {comf_class}, {additions}, {args}, {kwargs})"
            if time.time() - timer < cache_minutes*60 and format_arguments in cache_result:
                print("Закэшированные расчеты")
                result = cache_result[format_arguments]
            else:
                result = func(route, comf_class, additions, *args, **kwargs)
                if format_arguments in cache_result:
                    del cache_result[format_arguments]
                cache_result[format_arguments] = result
                start_func = time.strftime('%d/%m/%Y %H:%M:%S')
                timer = time.time()
                with open("cache_log.txt", "a+") as file:
                    if cache2file == True:
                        file.write(f"{start_func};{func.__name__};({route}, {comf_class}, {additions}, {args}, {kwargs});{result}; \n")
            return result
        return inner
    return wrapper

@universal_cache(cache2file = True, cache_minutes = 1)
def calc_price(route, comf_class, additions, *args, **kwargs):
    """Функция расчета стоимости поездки."""
    result = route * comf_class * additions
    for i in args:
        result += i
    for v in kwargs.values():
        result += v
    print("Calculating...")
    return result

print(calc_price(40, 20, 5, 20, 20, 5, a=20, b=20))
print(calc_price(35, 25, 10, 20, 20, 5, a=20, b=20))
print(calc_price(30, 25, 10, 20, 20, 5, a=20, b=20))
print(calc_price(100, 10, 5, 20, 20, 5, a=20, b=20))
print(calc_price(20, 25, 10, 20, 20, 5, a=20, b=20))
time.sleep(70)
print(calc_price(40, 20, 5, 20, 20, 5, a=20, b=20))
print(calc_price(40, 20, 5, 20, 20, 5, a=20, b=20))
print(calc_price(30, 25, 10, 20, 20, 5, a=20, b=20))
print(calc_price(100, 10, 5, 20, 20, 5, a=20, b=20))
print(calc_price(20, 25, 10, 20, 20, 5, a=20, b=20))