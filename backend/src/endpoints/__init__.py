"""Routers class"""
from fastapi.applications import FastAPI
from src.endpoints import routers, health_check

def include_all_routers(app: FastAPI, handler, CONFIG) -> FastAPI:
    """
    Add all routers to the FastAPI app
    """
    prefix = "/api"
    app.include_router(health_check.router, prefix=prefix)

    router = routers.create_router(handler, CONFIG)
    app.include_router(router, prefix=prefix)

    return app