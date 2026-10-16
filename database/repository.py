from sqlalchemy import select

from database.connection import SessionLocal
from database.models import Route


def save_route(
    start_point: str,
    finish_point: str,
    route: list[str],
    distance: float,
    time: float,
    traffic: float,
) -> Route:
    with SessionLocal() as session:
        new_route = Route(
            start_point=start_point,
            finish_point=finish_point,
            route=",".join(route),
            distance=distance,
            time=time,
            traffic=traffic,
        )

        session.add(new_route)
        session.commit()
        session.refresh(new_route)

        return new_route


def get_route(route_id: int) -> Route | None:
    with SessionLocal() as session:
        return session.get(Route, route_id)


def get_routes(
    start_point: str,
    finish_point: str,
) -> list[Route]:
    with SessionLocal() as session:
        statement = (
            select(Route)
            .where(
                Route.start_point == start_point,
                Route.finish_point == finish_point,
            )
        )

        return list(session.scalars(statement).all())


def update_actual_result(
    route_id: int,
    actual_time: float,
    actual_distance: float,
) -> None:
    with SessionLocal() as session:
        route = session.get(Route, route_id)

        if route is None:
            raise ValueError("Route not found")

        route.actual_time = actual_time
        route.actual_distance = actual_distance

        session.commit()