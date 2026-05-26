import json
import math
import random
import csv


# Distance Function
def euclidean_distance(point1, point2):

    x1, y1 = point1
    x2, y2 = point2

    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# Find nearest agent
def find_nearest_agent(warehouse_location, agents):

    nearest_agent = None
    minimum_distance = float('inf')

    for agent_id, agent_location in agents.items():

        distance = euclidean_distance(
            agent_location,
            warehouse_location
        )

        if distance < minimum_distance:

            minimum_distance = distance
            nearest_agent = agent_id

    return nearest_agent, minimum_distance


# Read JSON file
with open("data.json", "r") as file:

    data = json.load(file)


# Extract data
warehouses = data["warehouses"]

agents = data["agents"]

packages = data["packages"]


# Create report dictionary
report = {}

for agent_id in agents:

    report[agent_id] = {

        "packages_delivered": 0,

        "total_distance": 0.0,

        "efficiency": 0.0
    }


print("\nFASTBOX DELIVERY SYSTEM\n")


# Start simulation
for package in packages:

    package_id = package["id"]

    warehouse_id = package["warehouse"]

    warehouse_location = warehouses[warehouse_id]

    destination = package["destination"]

    # Find nearest agent
    nearest_agent, agent_to_warehouse_distance = find_nearest_agent(
        warehouse_location,
        agents
    )

    # Warehouse to destination distance
    warehouse_to_destination_distance = euclidean_distance(
        warehouse_location,
        destination
    )

    # Total trip distance
    total_trip_distance = (
        agent_to_warehouse_distance +
        warehouse_to_destination_distance
    )

    # Random delay
    delay = random.randint(0, 15)

    # Update report
    report[nearest_agent]["packages_delivered"] += 1

    report[nearest_agent]["total_distance"] += total_trip_distance

    # Print delivery details
    print("--------------------------------")

    print(f"Package ID      : {package_id}")

    print(f"Assigned Agent  : {nearest_agent}")

    print(f"Warehouse       : {warehouse_id}")

    print(f"Destination     : {destination}")

    print(f"Distance        : {round(total_trip_distance, 2)}")

    print(f"Delay           : {delay} mins")

    print(f"Route           : {nearest_agent} -> {warehouse_id} -> DELIVERY")


# Calculate efficiency
best_agent = None

best_efficiency = float('inf')

for agent_id in report:

    delivered = report[agent_id]["packages_delivered"]

    total_distance = report[agent_id]["total_distance"]

    if delivered > 0:

        efficiency = total_distance / delivered

    else:

        efficiency = 0

    report[agent_id]["total_distance"] = round(total_distance, 2)

    report[agent_id]["efficiency"] = round(efficiency, 2)

    # Find best agent
    if efficiency < best_efficiency and delivered > 0:

        best_efficiency = efficiency

        best_agent = agent_id


# Add best agent
report["best_agent"] = best_agent


# Save report.json
with open("report.json", "w") as file:

    json.dump(report, file, indent=4)


# Export CSV
with open("top_performer.csv", "w", newline="") as csvfile:

    writer = csv.writer(csvfile)

    writer.writerow([
        "Agent",
        "Packages Delivered",
        "Total Distance",
        "Efficiency"
    ])

    writer.writerow([
        best_agent,
        report[best_agent]["packages_delivered"],
        report[best_agent]["total_distance"],
        report[best_agent]["efficiency"]
    ])


# Final report
print("\nFINAL REPORT\n")

for agent_id in agents:

    print("--------------------------------")

    print(f"Agent: {agent_id}")

    print(
        f"Packages Delivered: "
        f"{report[agent_id]['packages_delivered']}"
    )

    print(
        f"Total Distance: "
        f"{report[agent_id]['total_distance']}"
    )

    print(
        f"Efficiency: "
        f"{report[agent_id]['efficiency']}"
    )

print("\n-------------------------------")

print(f"BEST AGENT: {best_agent}")

print("\nFiles Created:")
print("1. report.json")
print("2. top_performer.csv")