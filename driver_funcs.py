DRIVER_IDs = [36608123, 30487162, 90482770]

def outer(func):
    def inner(price):
        return func(price)
    return inner

percent_1 = 0
@outer
def driver_func_1(price):
    """Индивидуальнаяя функция расчета вознаграждения водителя"""
    global percent_1
    percent_1 += 0.01
    onetime_reward = price * percent_1 #вознаграждение ха текущую поездку
    driver_func_1.total_reward += onetime_reward
    return onetime_reward, driver_func_1.total_reward
driver_func_1.total_reward = 0 #вознаграждение за все поездки

percent_2 = 0
@outer
def driver_func_2(price):
    """Индивидуальнаяя функция расчета вознаграждения водителя"""
    global percent_2
    percent_2 += 0.01
    onetime_reward = price * percent_2
    driver_func_2.total_reward += onetime_reward
    return onetime_reward, driver_func_2.total_reward
driver_func_2.total_reward = 0

percent_3 = 0
@outer
def driver_func_3(price):
    """Индивидуальнаяя функция расчета вознаграждения водителя"""
    global percent_3
    percent_3 += 0.01
    onetime_reward = price * percent_3
    driver_func_3.total_reward += onetime_reward
    return  onetime_reward, driver_func_3.total_reward
driver_func_3.total_reward = 0

driver_func = {36608123: driver_func_1, 30487162: driver_func_2, 90482770: driver_func_3}

print(driver_func[36608123](200))  # стоимость поездки водителя с id 36608123 составляет 200
print(driver_func[36608123].total_reward)  # смотрим, сколько текущее вознаграждение
print(driver_func[36608123](300))  # стоимость поездки 300
print(driver_func[36608123].total_reward)  # смотрим, сколько текущее вознаграждение
print(driver_func[90482770].total_reward)
print(driver_func[90482770](300))
