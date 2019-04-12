#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import time
import os
import sys
from random import randint

import psutil
# This is the Publisher

class Sensor():
    def __init__(self):
        self.MB = 1000000
        self.sent_c = 0
        self.loss_c = 0
        self.total_pkgs = 0
        self.client = mqtt.Client()
        # self.host = "127.0.0.1"
        self.host = "10.0.0.1"
        self.port = 1883
        self.topic = "fog/"+str(os.uname()[1])
        self.t0 = time.time()
        self.elapsed_time = 0
        self.pkg_len = 0

    def cpu_u(self): #precisa ser thread
        # t = [proc.cpu_percent(interval=0.1) for proc in psutil.process_iter()]
        t = psutil.cpu_percent(interval=0.1)
        return (t)

    def debug(self):
        os.system('clear')
        print("tempo: " + str(self.elapsed_time)) # TODO corrigir isso
        print("topic: ", self.topic)
        print("pkgs enviados: ", self.total_pkgs)
        print('pkgs perdidos: ',self.loss_c)
        print("pkg size: ",self.pkg_len)
        print("memory: ", (psutil.virtual_memory().percent))
        # print("tx : ",(sys.getsizeof(s)/elapsed_time)/MB)
        print("bw: ", self.net_stat()) #?
        print("upload")
        print("download")
        print('CPU load: ',self.cpu_u())

    def net_stat(self): #TODO precisa ser thread
        dwl0 = psutil.net_io_counters().bytes_recv
        upl0 = psutil.net_io_counters().bytes_sent
        return psutil.net_io_counters()

    def get_mensage(self):
        s = ''.join(chr(97 + randint(0, 25)) for i in range(160000))
        self.pkg_len = sys.getsizeof(s)
        return s

    def send_msg(self):
        self.total_pkgs += 1
        try:
            self.client.connect(self.host, self.port, 60)
            self.client.publish(self.topic , payload=self.get_mensage())
            self.elapsed_time = time.time() - self.t0 # TODO calcular direito esse tempo
            self.t0 = self.elapsed_time
            # print("publicado em topic/"+str(os.uname()[1]))
            self.sent_c+=1
        except:
            # print("falha ao publicar em topic/"+str(os.uname()[1]))
            self.loss_c+=1
            self.client.disconnect()
        print("sent")

    def run(self):
        while(True):
            self.send_msg()
            self.debug()
            time.sleep(0.5)

if __name__ == "__main__":
    s = Sensor()
    s.run()