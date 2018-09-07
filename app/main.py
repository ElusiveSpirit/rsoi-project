import logging

from aiohttp import web
from .routes import setup_routes
from .utils import load_config
from .consts import APP_ROOT


def init_app():
    app = web.Application()
    setup_routes(app)
    app.on_shutdown.append(shutdown)
    return app


async def shutdown(app):
    pass


def main():
    logging.basicConfig(level=logging.DEBUG)
    app = init_app()
    conf = load_config(APP_ROOT / 'config' / 'config.yml')
    host, port = conf['host'], conf['port']
    web.run_app(app, host=host, port=port)


if __name__ == '__main__':
    main()
