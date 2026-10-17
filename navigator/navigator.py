from graph.dijkstra import dijkstra
from graph.map import GRAPH
from database.repository import save_route, get_routes
from ai.recommender import recommend_route


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

    shortest_result = calculate_route(start, finish)

    if shortest_result is None:
        return None

    shortest_route, shortest_distance, shortest_time = shortest_result

    history = get_routes(start, finish)

    recommendation = recommend_route(
        start,
        finish,
        history,
    )

    if recommendation is None:
        return {
            "shortest_route": shortest_route,
            "shortest_distance": shortest_distance,
            "shortest_time": shortest_time,
            "recommendation_available": False,
        }

    selected_route = recommendation["route"]

    average_traffic = calculate_average_traffic(selected_route)

    saved_route = save_route(
        start_point=start,
        finish_point=finish,
        route=selected_route,
        distance=recommendation["distance"],
        time=recommendation["time"],
        traffic=average_traffic,
    )

    return {
        "id": saved_route.id,
        "route": selected_route,
        "distance": recommendation["distance"],
        "time": recommendation["time"],
        "estimated_time": recommendation["estimated_time"],
        "traffic": average_traffic,
        "source": recommendation["source"],
        "history_count": recommendation["history_count"],
        "shortest_route": shortest_route,
        "shortest_distance": shortest_distance,
        "shortest_time": shortest_time,
        "recommendation_available": True,
    }