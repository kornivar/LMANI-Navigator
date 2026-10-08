# LMANI-Navigator
A Python-based Narrow AI (ANI) with Limited Memory navigation system that finds optimal routes using the Dijkstra algorithm, stores travel history in PostgreSQL, analyzes accumulated data, and uses historical information to improve future route recommendations.

The project combines graph algorithms, database management, data analysis, and Narrow AI with Limited Memory.

# Features

- Graph-based city map with weighted roads

- Custom implementation of the Dijkstra shortest-path algorithm

- PostgreSQL + Neon database for storing route history

- Recording expected and actual travel times and distances

- Route usage statistics and historical analysis

- Narrow AI-based route recommendations using accumulated travel data

- Comparison of mathematically optimal and historically efficient routes

- User-specific route history

# Technologies

- Python

- PostgreSQL
  
- Neon

- Dijkstra algorithm

# AI Concept

The system can be classified as Narrow AI (ANI) with Limited Memory. It uses accumulated historical data about previous trips to analyze route performance and improve future recommendations.

Dijkstra determines the mathematically shortest route, while the AI component considers historical travel data to determine whether an alternative route may be more efficient in practice.
