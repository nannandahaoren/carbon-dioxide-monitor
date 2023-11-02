import time
import network
import ujson
from simple import MQTTClient  # 上面的步骤就是在下载umqtt.simple到ESP32设备
from machine import Pin
from wifi import do_connect


MQTT_CLIENT = None
LED = None

# 发布订阅模式需要确定订阅什么主题
pub_topic = "temperature"
sub_topic = "sensor"
# 下面根据实际情况进行修改


# 回调函数，用于打印订阅到的消息
def sub_cb(topic, msg):
    global MQTT_CLIENT
    print(topic, msg)


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.


# The callback for when a PUBLISH message is received from the server.
def on_message(topic, msg):
    print("消息主题: {}".format(topic))
    print("消息内容: {}".format(msg))


def main():
    global MQTT_CLIENT, LED

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
        MQTT_CLIENT.check_msg()
        time.sleep(1)
        msg = b"22.78"
        # 发送自动配置MQTT服务的数据包
        MQTT_CLIENT.publish(pub_topic, msg)

        time.sleep(1)


if __name__ == "__main__":
    main()
