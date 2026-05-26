# FastBox Delivery System

## Overview
This project simulates a logistics delivery system.

## Features
- JSON file parsing
- Euclidean distance calculation
- Nearest agent assignment
- Delivery simulation
- Report generation
- CSV export
- Random delivery delays

## Files
- fastbox.py
- data.json
- report.json
- top_performer.csv

## Assumptions
- If two agents are equally near, first encountered agent is selected.
- Agent returns are not considered.
- Efficiency = total distance / packages delivered.
- One package delivered at a time.

## Run Project

```bash
python fastbox.py
```


## Assumptions & Engineering Decisions

Since some scenarios were not explicitly defined in the assignment, the following logical assumptions were made:

1. Nearest agent is selected using Euclidean distance from agent location to warehouse location.

2. If two agents are at the same distance from a warehouse (tie case), the first encountered agent in the dictionary order is selected.

3. Each package is delivered independently (one package at a time).

4. Agents do not return to their original position after delivery.

5. Agent locations remain fixed during the simulation.

6. Total delivery distance is calculated as:
   
   Agent → Warehouse + Warehouse → Destination

7. Efficiency is calculated using:
   
   Efficiency = Total Distance / Packages Delivered

8. Lower efficiency value is considered better because it means fewer travel units per package.

9. Random delivery delays are simulated only for realism and do not affect efficiency calculations.

10. The system assumes all package destinations and warehouse coordinates are valid.

11. If an agent delivers no packages, efficiency is set to 0.

12. Routing optimization between multiple packages was not implemented because the assignment specified package-level assignment.
## Author
NISHANT MANDAVKAR
