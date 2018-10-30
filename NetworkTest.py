import ipaddress



net4 = ipaddress.ip_network('10.2.25.0/28')


for x in net4.hosts():
    print(x)

print("Netmask: " + str(net4.netmask))
print("Broadcast: " + str(net4.broadcast_address))
