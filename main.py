from graph.map import LOCATIONS
from navigator.navigator import find_route


def main():
    print("Available locations:")
    for point, location in LOCATIONS.items():
        print(f"{point} — {location}")

    print()

    start = input("Starting point: ").upper()
    finish = input("Endpoint: ").upper()

    try:
        result = find_route(start, finish)
    except ValueError as error:
        print(f"Error: {error}")
        return

    if result is None:
        print("Route not found.")
        return

    print("\n Route:")

    for i, point in enumerate(result["route"]):
        print(f"{point} — {LOCATIONS[point]}", end="")
        if i < len(result["route"]) - 1:
            print(" → ", end="")

    print("\n")
    print(f"Distance: {result['distance']} km")
    print(f"Estimated time: {result['time']} min.")
    print(f"Average traffic congestion level: {result['traffic']:.1f}")
    print(f"Database Record ID: {result['id']}")


if __name__ == "__main__":
    main()