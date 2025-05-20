from asyncua.sync import Client
import time
opcua_server_url = "opc.tcp://localhost:4840"
nodeid = "ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL_AxisData.lrAxisPosition" 

client = Client(opcua_server_url)

try:
    client.connect()
    print(f"Connected to OPC UA server: {opcua_server_url}")

    node = client.get_node(nodeid)

    while True:
        position = node.read_value()
        print(f"Axis Position: {position:.2f}")
        time.sleep(.1)  # Read every .1 second

except Exception as e:
    print(f"Error: {e}")
finally:
    client.disconnect()
    print("Disconnected from OPC UA server.")