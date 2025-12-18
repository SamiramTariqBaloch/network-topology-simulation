# Network Topology Simulation with Node Failure Analysis

##  Project Overview

This project demonstrates the simulation of common **computer network topologies** using Python. It visualizes how different topologies behave when a **node failure** occurs. The project is especially useful for students studying **Computer Networks** and **Graph Theory**.

The following network topologies are simulated:

* Star Topology
* Bus Topology
* Ring Topology
* Mesh Topology

Each topology is displayed **before and after node failure** to analyze network reliability.


##  Objectives

* Understand different network topologies
* Visualize network structures using graphs
* Simulate node failure in networks
* Analyze fault tolerance of each topology


##  Technologies Used

* **Python 3.x**
* **NetworkX** (for network/graph creation)
* **Matplotlib** (for visualization)


##  Project Structure

```
network_topology_simulation.py   # Main Python file
README.md                        # Project documentation
```

---

##  How to Run the Project

### Step 1: Install Python

Make sure **Python 3** is installed on your system.
Check by running:

```bash
python --version
```

---

### Step 2: Install Required Libraries

Install the required Python libraries using pip:

```bash
pip install networkx matplotlib
```

If `pip` does not work, try:

```bash
python -m pip install networkx matplotlib
```

---

### Step 3: Clone or Download the Repository

Clone the repository using Git:

```bash
git clone https://github.com/your-username/network-topology-simulation.git
```

Or download the ZIP file and extract it.

---

### Step 4: Run the Program

Navigate to the project directory and run:

```bash
python network_topology_simulation.py
```

---

##  Output

* Graphical visualization of each topology
* Node failure simulation with updated network view
* Console messages indicating node removal

---

## 📊 Observations

| Topology | Effect of Node Failure                      |
| -------- | ------------------------------------------- |
| Star     | Entire network fails (central node failure) |
| Bus      | Network splits into parts                   |
| Ring     | Loop breaks                                 |
| Mesh     | Network remains operational                 |

---





⭐ If you find this project useful, feel free to star the repository!
