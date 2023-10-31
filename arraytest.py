from machine import Pin, I2C
from time import sleep
import BME280
import array as arr


def tempAverage(temp):
    total = 0
    for i in range(10):
        total += temp(i)
    return total / 10.0


# 维护一个数组，用于存储温度值
temp = arr.array("d")


# ESP32 - Pin assignment
i2c = I2C(scl=Pin(22), sda=Pin(21), freq=10000)
# ESP8266 - Pin assignment
# i2c = I2C(scl=Pin(5), sda=Pin(4), freq=10000)

# 计数器
num = 0

# 温度统计值
T = 0
while True:
    bme = BME280.BME280(i2c=i2c)
    # 下方t是读取的温度值,测量值
    t = bme.temperature
    temp.append(t)
    # hum = bme.humidity
    # pres = bme.pressure
    # uncomment for temperature in Fahrenheit
    # temp = (bme.read_temperature()/100) * (9/5) + 32
    # temp = str(round(temp, 2)) + 'F'

    if len(temp) == 10:
        T = tempAverage(temp)
    print("Temperature: ", T)
    # print('Humidity: ', hum)
    # print('Pressure: ', pres)
    num += 1
    sleep(0.5)
