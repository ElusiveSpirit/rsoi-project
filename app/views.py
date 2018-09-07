from aiohttp import web


async def index(_request):
    return web.Response(text='Hello world')
