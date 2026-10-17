from database.repository import (
    get_all_routes,
    get_route,
    update_actual_result,
)

def show_history() -> None:
    routes = get_all_routes()

    if not routes:
        print("The route history is empty.")
        return

    print("\n===== RUTE HISTORY =====")

    for route in routes:
        print(f"\nID: {route.id}")
        print(f"RUTE: {route.route.replace(',', ' → ')}")
        print(f"Distance: {route.distance} km")
        print(f"Estimated time: {route.time} min")
        print(f"Actual time: {route.actual_time or 'Not specified'}")
        print(f"Actual distance: {route.actual_distance or 'Not specified'}")
        print(f"Date: {route.created_at}")


def add_trip_result() -> None:
    try:
        route_id = int(input("Route record ID: "))
    except ValueError:
        print("Error: The ID must be an integer.")
        return

    route = get_route(route_id)

    if route is None:
        print("No route with that ID was found.")
        return

    print(f"Route: {route.route.replace(',', ' → ')}")
    print(f"Estimated time: {route.time} min")
    print(f"Estimated distance: {route.distance} km")

    try:
        actual_time = float(input("Actual time (min):"))
        actual_distance = float(input("Actual distance (km): "))
    except ValueError:
        print("Error: Please enter numeric values.")
        return

    if actual_time <= 0 or actual_distance <= 0:
        print("Time and distance must be greater than zero.")
        return

    if route.actual_time is not None:
        print("The actual result for this record has already been saved.")
        return

    updated = update_actual_result(
        route_id=route_id,
        actual_time=actual_time,
        actual_distance=actual_distance,
    )

    if updated:
        print("The trip results have been saved.")