# Dynamic-Link-Failure-Recovery-SDN                            
                                            
The project is emulated using Mininet V2.2.2. 
1.	The installation procedure is using the Mininet VM image downloaded from http://mininet.org/download/.  
2.	The VM image is used with Virtual Box on top of a Windows system.
3.	Log into Mininet with username: mininet and password: mininet.


Testing the project:
1.	Copy the files create_topology.py, dijkstra.py to the directory /home/mininet/pox/ext.
2.	Open to ssh terminals, in one pass the dijkstra file as a parameter along with other paramters to inbuilt pox python functions  (run the command as mininet user ./pox/pox.py openflow.discovery dijkstra py)
3.	Go to another ssh terminal run /pox/ext/create_topology.py
4.	Now, to make a link down, go to the second ssh terminal and type link <src> <dst> down/up ex: link S1 S3 down
5.	To ping from h1 to h2, type h1 ping h2 on the same terminal
6. 	You can verify the results in the first ssh terminal where the pox is running.

The configuration can be cleared using the command sudo mn -c
