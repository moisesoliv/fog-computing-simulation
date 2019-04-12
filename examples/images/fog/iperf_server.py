import iperf3
import time

def iperf():
    server = iperf3.Server()
    result = server.run()
    return (result.remote_host)
if __name__ == "__main__":
    while(True):
        print(iperf())
        time.sleep(1)
