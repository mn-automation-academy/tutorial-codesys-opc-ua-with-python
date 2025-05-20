from asyncua.sync import Client
import matplotlib.pyplot as plt
import numpy as np
import time
opcua_server_url = "opc.tcp://localhost:4840"
nodeids = ["ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL_AxisData.lrAxisPosition",
"ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL_AxisData.lrAxisVelocity",
"ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL_AxisData.lrAxisAcceleration",]

client = Client(opcua_server_url)
positionData = []
velocityData = []
accelerationData = []
timeData = []
try:
    client.connect()
    print(f"Connected to OPC UA server: {opcua_server_url}")

    nodes = [client.get_node(nodeid) for nodeid in nodeids]

    startTime = time.time()
    while len(positionData) < 1000:
        # Read multiple values at once
        data_values = client.read_values(nodes) # Pass list of node objects

        positionData.append(data_values[0])
        velocityData.append(data_values[1])
        accelerationData.append(data_values[2])
        timeData.append(time.time() - startTime)
        
        print(f"Axis Position: {data_values[0]:.2f}, Velocity: {data_values[1]:.2f}, Acceleration: {data_values[2]:.2f}")
        time.sleep(.01)  # Read every 1 second

    # Plotting the data
    plt.figure(figsize=(10, 8))

    # Subplot for Position
    plt.subplot(3, 1, 1)
    plt.plot(timeData, positionData, color='blue')
    plt.title("Axis Position Over Time")
    plt.xlabel("Time (s)")
    plt.ylabel("Position")
    plt.grid()

    # Subplot for Velocity
    plt.subplot(3, 1, 2)
    plt.plot(timeData, velocityData, color='red')
    plt.title("Axis Velocity Over Time")
    plt.xlabel("Time (s)")
    plt.ylabel("Velocity")
    plt.grid()

    # Subplot for Acceleration
    plt.subplot(3, 1, 3)
    plt.plot(timeData, accelerationData, color='green')
    plt.title("Axis Acceleration Over Time")
    plt.xlabel("Time (s)")
    plt.ylabel("Acceleration")
    plt.grid()
    plt.tight_layout()  # Adjust subplots to fit into figure area.
    plt.show()
    print("Plotting complete.")

except Exception as e:
    print(f"Error: {e}")
finally:
    client.disconnect()
    print("Disconnected from OPC UA server.")