from asyncua.sync import Client
import matplotlib.pyplot as plt
import numpy as np
import time
opcua_server_url = "opc.tcp://localhost:4840"
nodeid = "ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL_AxisData.lrAxisPosition" 

client = Client(opcua_server_url)
positionData = []
timeData = []
try:
    client.connect()
    print(f"Connected to OPC UA server: {opcua_server_url}")

    node = client.get_node(nodeid)

    startTime = time.time()
    while len(positionData) < 1000:
        position = node.read_value()

        positionData.append(position)
        timeData.append(time.time() - startTime)

        print(f"Axis Position: {position:.2f}")
        time.sleep(.01)  # Read every 1 second

    # Plotting the data
    plt.plot(timeData,positionData)
    plt.title("Axis Position Over Time")    
    plt.xlabel("Time (s)")
    plt.ylabel("Axis Position")
    plt.grid()
    plt.show()
    print("Plotting complete.")

except Exception as e:
    print(f"Error: {e}")
finally:
    client.disconnect()
    print("Disconnected from OPC UA server.")