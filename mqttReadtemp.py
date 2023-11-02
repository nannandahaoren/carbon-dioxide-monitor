import time
import network
import ujson
from simple import MQTTClient  # 上面的步骤就是在下载umqtt.simple到ESP32设备
from machine import Pin
from wifi import do_connect
from umqtt import sub_cb, on_connect, on_message
import array as arr
from kalman_average import tempAverage, tempKalman
import struct
from machine import Pin, SoftI2C
from BME280 import BME280

MQTT_CLIENT = None
LED = None

# 发布订阅模式需要确定订阅什么主题
pub_topic = "temperature"
sub_topic = "sensor"
# 下面根据实际情况进行修改


# 维护一个临时数组，用于存储温度值
temp_array = arr.array("d")
# 维护一个存储数组，用于存储到数据库中
dataset_temp = arr.array("d")

# ESP32 - Pin assignment
i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)

# 存放临时数组的平均值
T = 0


def main():
    global MQTT_CLIENT, LED, temp_array, dataset_temp, T, i2c
    global pub_topic, sub_topic

    # 1.链接WiFi
    do_connect()
    # 创建mqtt客户端
    # 第一个参数 客户端的名字
    # 第二个参数mqtt服务端的ip地址
    # 第三个参数mqtt服务端的端口号
    # 第四个参数mqtt服务端的管理员账号
    # 第五个参数mqtt服务端的管理员密码
    # 第六个参数默认设置
    MQTT_CLIENT = MQTTClient(
        "ESP32_1", "101.43.132.163", 1883, "admin", "Lj112358", keepalive=60
    )

    print("connectted to mqtt_server !")

    MQTT_CLIENT.set_callback(on_message)  # 设置回调函数
    MQTT_CLIENT.connect()  # 建立连接
    MQTT_CLIENT.subscribe(sub_topic)

    time.sleep(1)

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

        if len(temp_array) == 6:
            T = tempAverage(temp_array)  # 当临时数组的元素个数为5个时，求平均
            print("T: ", T)
            length = len(dataset_temp)  # 计算dataset_temp的长度

            if length == 0:
                dataset_temp.append(T)
            else:
                length -= 1
                temp = dataset_temp[length]
                dataT = tempKalman(temp, T)
                round_number = round(dataT, 1)
                print("-----------------------------")
                print("temprature after kalmanfilter is ", round_number)
                dataset_temp.append(dataT)
                msg = struct.pack("f", round_number)
                MQTT_CLIENT.publish(pub_topic, msg)
            temp_array = []

        MQTT_CLIENT.check_msg()

        # msg = b"22.78"
        # 发送自动配置MQTT服务的数据包

        time.sleep(0.5)


if __name__ == "__main__":
    main()
