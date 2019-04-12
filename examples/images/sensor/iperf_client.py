import iperf3
import time

def iperf():
    client = iperf3.Client()
    client.duration = 1
    client.server_hostname = '10.0.0.252'
    client.port = 5201
    result = client.run()
    return (result.sent_Mbps)


if __name__ == "__main__":
    while(True):
        print(iperf())
        time.sleep(5)
