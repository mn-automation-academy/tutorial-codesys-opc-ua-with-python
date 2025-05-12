# CoDeSys OPC-UA Communication with Python Tutorial

[![YouTube Video Link](https://img.shields.io/badge/YouTube-Watch_Tutorial-red?logo=youtube)](https://youtu.be/YOUR_VIDEO_ID_HERE) <!-- Replace with your actual video link! -->

Welcome! This repository contains the source code and CoDeSys projects for the YouTube tutorial demonstrating how to communicate between a CoDeSys V3 PLC (running in Simulation mode) and a Python script using the OPC-UA protocol.

We will start with a basic CoDeSys SoftMotion project, configure it as an OPC UA server, and then use Python scripts to connect, read data cyclically, and plot it using Matplotlib.

**Key Technologies Used:**

*   **CoDeSys:** V3.5 SP19 patch 5
*   **SoftMotion:** Virtual Axis for simulation
*   **OPC UA:** The communication protocol
*   **Python:** 3.7+
*   **python-opcua (`asyncua` sync wrapper):** Python library for OPC UA communication (`asyncua.sync`)
*   **Matplotlib:** Python library for plotting data

## YouTube Tutorial

**(Link to the accompanying YouTube video will be placed here once available)**
[Watch the Tutorial on YouTube](https://youtu.be/YOUR_VIDEO_ID_HERE) <!-- Replace with your actual video link! -->

## Prerequisites

1.  **CoDeSys Development System:** Version 3.5 SP16 or later. Downloadable for free from the [CoDeSys Store](https://store.codesys.com/codesys.html). (Requires registration).
2.  **Python:** Python 3.7 or later installed. You can get it from [python.org](https://www.python.org/) or use distributions like Anaconda/Miniconda.
3.  **(Optional but Recommended) OPC UA Client Tool:** [UaExpert](https://www.unified-automation.com/downloads/opc-ua-clients.html) is a popular, free client useful for browsing the OPC UA server structure and testing the connection independently of Python.
4.  **Basic Knowledge:** Familiarity with basic PLC programming concepts (variables, GVLs) and basic Python syntax is helpful.

## Setup Instructions

### 1. CoDeSys Project Setup

*   **Download:** Clone or download this repository.
*   **Open Project:** Open the `CoDeSys_Projects/OPC-UA_Server Example Project - Start.project` in your CoDeSys Development System.
    *   This project contains a simple program (`PLC_PRG`) controlling a virtual SoftMotion axis (`Axis1`) and a Global Variable List (`OPC_GVL`) to hold data for OPC UA.
*   **(Follow Video for Setup):** The video tutorial walks through these steps using the `Start` project:
    *   **Symbol Configuration:** Adding a 'Symbol Configuration' object, building the project, selecting `OPC_GVL` (or specific variables inside it) for exposure, and enabling "Support OPC UA features".
    *   **Enable OPC UA Server:** Double-clicking 'Device', going to the 'OPC UA Server' tab, checking 'Activate OPC UA Server'. Note the endpoint URL (usually `opc.tcp://localhost:4840`).
*   **Reference Project:** `OPC-UA_Server Example Project - Complete.project` has the Symbol Configuration and OPC UA server already set up for comparison.
*   **Run Simulation:**
    *   Enable Simulation mode (`Online` -> `Simulation`).
    *   Login (`Online` -> `Login`).
    *   Download the project if prompted.
    *   Start the PLC (`Debug` -> `Start` or F5).
    *   You can manually toggle variables like `bEnable` or `bMoveVel` in `PLC_PRG` to see the simulated axis move and `OPC_GVL.rAxisPosition` update.

### 2. Python Environment & Libraries

*   **(Recommended) Use a Virtual Environment:** While not enforced in the tutorial, using a virtual environment prevents dependency conflicts between projects.
    *   Using `venv` (built-in):
        ```bash
        python -m venv .venv
        # Activate (Windows CMD/PowerShell)
        .\.venv\Scripts\activate
        # Activate (Linux/macOS)
        # source .venv/bin/activate
        ```
    *   Using `conda`:
        ```bash
        conda create --name codesys_opcua python=3.9 # Or your preferred version
        conda activate codesys_opcua
        ```
*   **Install Libraries:** Open your terminal or command prompt (with the virtual environment activated if you created one) and run:
    ```bash
    pip install asyncua matplotlib
    ```
    *   *Note:* We are installing `asyncua`, but for simplicity in this tutorial, we will use its synchronous wrapper: `asyncua.sync`.

### 3. (Optional) Test with UaExpert

*   Launch UaExpert.
*   Click 'Add Server' (`+` icon).
*   Under 'Custom Discovery', double-click '<Double click to Add Server...>'.
*   Enter the CoDeSys OPC UA Endpoint URL: `opc.tcp://localhost:4840`
*   Click 'OK'.
*   Find the server in the list, right-click, and select 'Connect'. Keep security settings as default (Anonymous/None) unless you changed them in CoDeSys.
*   Once connected, browse the 'Address Space' panel: `Objects` -> `DeviceSet` -> `CODESYS Control Win V3` (or similar) -> `Resources` -> `Plc Logic` -> `Application` -> `GVLs` -> `GVL_AxisData`.
*   You should see `lrAxisPosition`, `lrAxisVelocity`, `lrAxisAcceleration`. Drag them to the 'Data Access View' panel to see their values update live when you interact with the simulation in CoDeSys.



