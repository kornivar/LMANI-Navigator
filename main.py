from graph.dijkstra import dijkstra
from graph.map import GRAPH, LOCATIONS


def main():
    start = input("Starting point: ").upper()
    finish = input("Endpoint: ").upper()

    if start not in GRAPH or finish not in GRAPH:
        print("Error: unknown point.")
        return

    route, distance, time = dijkstra(
        GRAPH,
        start,
        finish,
    )

    if not route:
        print("Route not found.")
        return

    print()
    print("Route:")
    print(" → ".join(route))

    print(f"Distance : {distance} km")
    print(f"Time: {time} min.")

    print()
    print("Locations:")

    for location in route:
        print(f"{location} — {LOCATIONS[location]}")


if __name__ == "__main__":
    main()