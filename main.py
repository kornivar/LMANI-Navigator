from graph.map import LOCATIONS
from navigator.navigator import find_route
from navigator.history import show_history, add_trip_result


def main():
    while True:
        print("\n===== AI NAVIGATOR =====")
        print("1. Find a route")
        print("2. Add trip result")
        print("3. Route history")
        print("0. Exit")

        choice = input("Your choice: ").strip()

        if choice == "1":
            print("Available locations:")
            for point, location in LOCATIONS.items():
                print(f"{point} — {location}")

            print()

            start = input("Starting point: ").strip().upper()
            finish = input("Destination: ").strip().upper()

            try:
                result = find_route(start, finish)
            except ValueError as error:
                print(f"Error: {error}")
                continue

            if result is None:
                print("Route not found.")
                continue

            print(
                f"\nShortest route: "
                f"{' → '.join(result['shortest_route'])}"
            )
            print(f"Distance: {result['shortest_distance']} km")
            print(f"Estimated time: {result['shortest_time']} min")

            if result["source"] == "history":
                locations = " → ".join(
                    f"{point} ({LOCATIONS[point]})"
                    for point in result["route"]
                )

                print("\nRecommended route:")
                print(locations)
                print(f"Distance: {result['distance']} km")
                print(
                    f"Estimated time based on graph: "
                    f"{result['time']} min"
                )
                print(
                    f"Estimated trip time: "
                    f"{result['estimated_time']:.1f} min"
                )
                print(
                    f"Based on {result['history_count']} completed trips."
                )
                print(f"Record ID: {result['id']}")

            else:
                print(
                    "\nInsufficient trip history to recommend "
                    "a personalized route."
                )
                print(
                    "Only the shortest route is available."
                )

        elif choice == "2":
            add_trip_result()

        elif choice == "3":
            show_history()

        elif choice == "0":
            break

        else:
            print("Invalid menu option.")


if __name__ == "__main__":
    main()