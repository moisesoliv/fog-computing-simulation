#!usr/bin/python
"""
This is the most simple example to showcase Fogbed.
"""

#TODO limitar CPU = 1
#TODO usar uma imagem Docker menor(alpine)


import time

from src.fogbed.experiment import FogbedExperiment, FogbedDistributedExperiment
from src.fogbed.resourcemodel import CloudResourceModel, EdgeResourceModel, FogResourceModel, PREDEFINED_RESOURCES
from src.fogbed.topo import FogTopo
from src.mininet.link import TCLink
from src.mininet.log import setLogLevel
from src.mininet.node import OVSSwitch


setLogLevel('info')

topo = FogTopo()

c1 = topo.addVirtualInstance("cloud")
f1 = topo.addVirtualInstance("fog")
e1 = topo.addVirtualInstance("sensor")

erm = EdgeResourceModel()
frm = FogResourceModel()
crm = CloudResourceModel()

e1.assignResourceModel(erm)
f1.assignResourceModel(frm)
c1.assignResourceModel(crm)

d1 = c1.addDocker('d1', ip='10.0.2.1', dimage="cloud:latest", resources=PREDEFINED_RESOURCES['large'])
d2 = f1.addDocker('f1', ip='10.0.0.1', dimage="fog:latest", resources=PREDEFINED_RESOURCES['large'])
d8 = topo.addDocker('d8', ip='10.0.0.2', dimage="manager:latest", resources=PREDEFINED_RESOURCES['medium'])


d3 = e1.addDocker('pre', ip='10.0.0.3', dimage="sensor:latest", resources=PREDEFINED_RESOURCES['large'])
d4 = e1.addDocker('bio', ip='10.0.0.4', dimage="sensor:latest", resources=PREDEFINED_RESOURCES['tiny'])
d5 = e1.addDocker('lum', ip='10.0.0.6', dimage="sensor:latest", resources=PREDEFINED_RESOURCES['tiny'])
d4 = e1.addDocker('tem', ip='10.0.0.7', dimage="sensor:latest", resources=PREDEFINED_RESOURCES['tiny'])
d5 = e1.addDocker('umi', ip='10.0.0.8', dimage="sensor:latest", resources=PREDEFINED_RESOURCES['tiny'])
'''
s = []
for i in range(20):
    ip = '10.0.0.%s'%(i+4)
    id = 'd%s'%(i+4)
    s.append(e1.addDocker(id, ip=ip, dimage="sensor:latest", resources=PREDEFINED_RESOURCES['tiny']))
    # s.append(e1.addDocker(id, ip=ip, dimage="sensor:latest"))
'''


s1 = topo.addSwitch('s1')
s2 = topo.addSwitch('s2')
# topo.addLink(d4, s1)
topo.addLink(s1, s2)
topo.addLink(s2, e1)
topo.addLink(c1, f1, cls=TCLink, delay='54ms', bw=1)
topo.addLink(f1, e1, cls=TCLink, delay='54ms', bw=0.1)

exp = FogbedExperiment(topo, switch=OVSSwitch)
exp.start()

try:
    print(exp.get_node(d2).cmd("ifconfig"))

    print("waiting 2 seconds for routing algorithms on the controller to converge")
    time.sleep(2)

    print(exp.get_node(d2).cmd("ping -c 5 10.0.0.3"))
    print(exp.get_node(d2).cmd("ping -c 5 10.0.0.4"))
    print(exp.get_node(d2).cmd("ping -c 5 10.0.0.5"))
    print(exp.get_node(d2).cmd("ping -c 5 10.0.0.6"))
    print(exp.get_node(d2).cmd("ping -c 5 10.0.0.7"))
    print(exp.get_node(d2).cmd("ping -c 5 10.0.0.8"))

    exp.pingAll()
    exp.CLI()
finally:
    exp.stop()
