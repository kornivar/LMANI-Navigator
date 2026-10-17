
from graph.map import GRAPH


MIN_HISTORY_COUNT = 3
MAX_CANDIDATES = 20


def find_candidate_routes(
    graph: dict,
    start: str,
    finish: str,
    max_candidates: int = MAX_CANDIDATES,
) -> list[dict]:

    candidates = []

    def search(current: str, route: list[str]) -> None:
        if current == finish:
            distance = 0
            time = 0

            for i in range(len(route) - 1):
                road = graph[route[i]][route[i + 1]]
                distance += road["distance"]
                time += road["time"]

            candidates.append({
                "route": route.copy(),
                "distance": distance,
                "time": time,
            })
            return

        for neighbor in graph[current]:
            if neighbor not in route:
                search(neighbor, route + [neighbor])

    search(start, [start])

    candidates.sort(key=lambda candidate: candidate["distance"])

    return candidates[:max_candidates]


def get_route_history(
    route: list[str],
    history: list,
) -> list:

    route_key = tuple(route)
    reverse_key = tuple(reversed(route))

    matching_records = []

    for record in history:
        if record.actual_time is None:
            continue

        saved_route = tuple(record.route.split(","))

        if saved_route in (route_key, reverse_key):
            matching_records.append(record)

    return matching_records


def evaluate_route(
    candidate: dict,
    history: list,
) -> dict | None:

    records = get_route_history(candidate["route"], history)

    if len(records) < MIN_HISTORY_COUNT:
        return None

    average_time = sum(
        record.actual_time for record in records
    ) / len(records)

    return {
        **candidate,
        "estimated_time": average_time,
        "history_count": len(records),
        "source": "history",
    }


def recommend_route(
    start: str,
    finish: str,
    history: list,
) -> dict | None:

    candidates = find_candidate_routes(
        GRAPH,
        start,
        finish,
    )

    if not candidates:
        return None

    evaluated_routes = [
        result
        for candidate in candidates
        if (
            result := evaluate_route(candidate, history)
        ) is not None
    ]

    if not evaluated_routes:
        return None

    return min(
        evaluated_routes,
        key=lambda candidate: candidate["estimated_time"],
    )
