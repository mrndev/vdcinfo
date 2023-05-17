# vdcinfo
vdcinfo is a helper script to get virtual data center data and parse it to readable and "greppable" format.

The output format of the APIs is JSON, which is great, but this format is not very grep friendly for quick lookups and troubleshooting.  The trick that the script does is that it replaces the item[0].. json paths with object types (like "datacenter") and names ("Martins datacenter", "MyVM") - whatever you named the objects in the DCD or via the APIS). 

Here is an example - get app ip addresses of my servers

    python vdcinfo.py | egrep -i 'ips/'
    datacenter/My test datacenter/entities/servers/server/BootTestServer/entities/nics/nic/Internet/properties/ips/0 = '217.160.xxx.xxx'
    datacenter/My test datacenter/entities/lans/lan/Internet/entities/nics/nic/Internet/properties/ips/0 = '217.160.xxx.xxx'
    datacenter/Test 5/entities/servers/server/test5i1/entities/nics/nic/test5i1/properties/ips/0 = '185.132.xxx.xxx'
    datacenter/Test 5/entities/lans/lan/LAN/entities/nics/nic/test5i1/properties/ips/0 = '185.132.xxx.xxx'
    datacenter/MartinsDC/entities/servers/server/winbackuptest/entities/nics/nic/0/properties/ips/0 = '85.215.xxx.xxx'
    ...
    
The script always gets the configuration of all datacenters that are accessible with the given API token (environment variable IONOS_TOKEN must be set)
