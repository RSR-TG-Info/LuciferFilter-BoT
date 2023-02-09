from aiohttp import web
from LuciferFilter import Configs

routes = web.RouteTableDef()

@routes.get("/", allow_head=Configs.STOP_BOT)
async def root_route_handler(request):
    return web.json_response("TechProjectsUpdates")
