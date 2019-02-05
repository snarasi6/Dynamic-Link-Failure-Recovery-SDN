#CODE TO CONSTRUCT TOPOLOGY

from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import Link, TCLink
from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSKernelSwitch, UserSwitch

def topology():
		net = Mininet(controller=RemoteController, link=TCLink, switch=OVSKernelSwitch)
		
		#CREATING HOSTS
		h1 = net.addHost('h1', mac="00:00:00:00:00:01")
        h2 = net.addHost('h2', mac="00:00:00:00:00:02")
		h3 = net.addHost('h3', mac="00:00:00:00:00:03")
		
		#CREATING SWITCHES
        S1 = net.addSwitch('s1')
        S2 = net.addSwitch('s2') 
        S3 = net.addSwitch('s3') 
        S4 = net.addSwitch('s4')
        S5 = net.addSwitch('s5') 
        S6 = net.addSwitch('s6') 
        S7 = net.addSwitch('s7') 
		
		#CREATING CONTROLLER
        c0 = net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=6633) 
        
		#ADDING LINKS 
		
        net.addLink(h1, S1)  
		net.addLink(h2, S7) 
        net.addLink(h3, S2) 
		
        net.addLink(S1,S2)
        net.addLink(S1,S3)        
        net.addLink(S1,S6)
		
        net.addLink(S2,S3)
        net.addLink(S2,S6)
        
        net.addLink(S3,S4)
        net.addLink(S3,S5)
        net.addLink(S3,S6)
        net.addLink(S3,S7)
		
        net.addLink(S4,S5)
		net.addLink(S4,S6)
		
		net.addLink(S5,S6)
		net.addLink(S6,S7)
        
		#CONSTRUCT THE NETWORK 
		net.build()	
		c0.start()	
        S1.start([c0])
        S2.start([c0])
        S3.start([c0])
        S4.start([c0])
        S5.start([c0])
        S6.start([c0])
        S7.start([c0])

        h1.cmd("arp -s 10.0.0.2 00:00:00:00:00:02")
        h2.cmd("arp -s 10.0.0.1 00:00:00:00:00:01") 
        h1.cmd("tcpdump -i h1-eth0 -nn -X 'icmp' -w send &")
        h2.cmd("tcpdump -i h2-eth0 -nn -X 'icmp' -w receive &")

        print "*** Running CLI"
        
		#INVOKING CLI
		CLI(net)
		
        print "*** Stopping network"
        net.stop()
		
if __name__ == '__main__':
    setLogLevel('info')
    topology()