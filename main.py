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

            locations = " → ".join(
                f"{point} ({LOCATIONS[point]})"
                for point in result["route"]
            )

            print(f"\nRoute: {locations}")
            print(f"Distance: {result['distance']} km")
            print(f"Estimated time: {result['time']} min")
            print(f"Record ID: {result['id']}")

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