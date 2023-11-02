from machine import Pin, I2C
from time import sleep
from BME280 import BME280
import array as arr


# 计算平均温度
def tempAverage(temp):
    total = 0
    for i in range(5):
        total += temp[i]
    return total / 5.0


# 维护一个临时数组，用于存储温度值
temp_array = arr.array("d")
# 维护一个存储数组，用于存储到数据库中
dataset_temp = arr.array("d")


# temp是上一时刻的温度值，temp是存储在dataset_temp中的最后一个元素
def tempKalman(temp, T):
    currntTemp = temp + 0.3 * (T - temp)
    print("temprature after kalmanfilter is ", currntTemp)
    return currntTemp


# ESP32 - Pin assignment
i2c = I2C(scl=Pin(22), sda=Pin(21), freq=10000)
# ESP8266 - Pin assignment
# i2c = I2C(scl=Pin(5), sda=Pin(4), freq=10000)


# 温度统计值
T = 0
while True:
    bme = BME280(i2c=i2c)
    # 下方t是读取的温度值,测量值
    str_t = bme.temperature  # 获取带有字符串C的字符串形式的温度
    str_t = str_t.replace("C", "")  # 去掉带有字符串C的字符串形式的温度
    t = float(str_t)  # 将字符串形式的温度转化成浮点数形式
    temp_array.append(t)  # 将温度值添加到临时数组中
    # hum = bme.humidity
    # pres = bme.pressure
    # uncomment for temperature in Fahrenheit
    # temp = (bme.read_temperature()/100) * (9/5) + 32
    # temp = str(round(temp, 2)) + 'F'

    if len(temp_array) == 5:
        T = tempAverage(temp_array)  # 当临时数组的元素个数为5个时，求平均
        length = len(dataset_temp)  # 计算dataset_temp的长度

        if length == 0:
            dataset_temp.append(T)
        else:
            length -= 1
            temp = dataset_temp[length]
            dataT = tempKalman(temp, T)
            print("-----------------------------")
            dataset_temp.append(dataT)
        temp_array = []

    # print('Humidity: ', hum)
    # print('Pressure: ', pres)
    sleep(0.25)
