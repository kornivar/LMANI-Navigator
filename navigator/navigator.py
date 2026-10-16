from graph.dijkstra import dijkstra
from graph.map import GRAPH
from database.repository import save_route


def validate_route_points(start: str, finish: str) -> None:
    if start not in GRAPH or finish not in GRAPH:
        raise ValueError("Unknown location")

    if start == finish:
        raise ValueError("Starting point and endpoint must differ")


def calculate_route(start: str, finish: str) -> tuple[list[str], float, float] | None:
    route, distance, time = dijkstra(
        GRAPH,
        start,
        finish,
    )

    if not route:
        return None

    return route, distance, time


def calculate_average_traffic(route: list[str]) -> float:
    traffic_values = [
        GRAPH[route[i]][route[i + 1]]["traffic"]
        for i in range(len(route) - 1)
    ]

    return sum(traffic_values) / len(traffic_values)


def find_route(start: str, finish: str) -> dict | None:
    validate_route_points(start, finish)

    result = calculate_route(start, finish)

    if result is None:
        return None

    route, distance, time = result
    average_traffic = calculate_average_traffic(route)

    saved_route = save_route(
        start_point=start,
        finish_point=finish,
        route=route,
        distance=distance,
        time=time,
        traffic=average_traffic,
    )

    return {
        "id": saved_route.id,
        "route": route,
        "distance": distance,
        "time": time,
        "traffic": average_traffic,
    }