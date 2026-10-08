from graph.map import GRAPH


def dijkstra(graph: dict, start: str, finish: str) -> tuple[list[str], float, float]:
    distances = {
        location: float("inf")
        for location in graph
    }

    previous = {
        location: None
        for location in graph
    }

    distances[start] = 0

    unvisited = set(graph)

    while unvisited:
        current = min(
            unvisited,
            key=lambda location: distances[location]
        )

        if distances[current] == float("inf"):
            break

        unvisited.remove(current)

        if current == finish:
            break

        for neighbor, road in graph[current].items():
            new_distance = (
                distances[current]
                + road["distance"]
            )

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current

    if distances[finish] == float("inf"):
        return [], 0, 0

    route = []
    current = finish

    while current is not None:
        route.append(current)
        current = previous[current]

    route.reverse()

    total_time = 0

    for i in range(len(route) - 1):
        current = route[i]
        next_location = route[i + 1]

        total_time += GRAPH[current][next_location]["time"]

    return route, distances[finish], total_time