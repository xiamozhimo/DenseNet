
# -*- coding: utf-8 -*-


import logging; logging.basicConfig(level=logging.INFO)
import asyncio, os, json, time
from datetime import datetime
from aiohttp import web

def index(request):
    return web.Response(body = b'<h1>Hi, there!</h1>', headers = {"content-type": "text/html"})

def login(request):
    text = '<h1>Login %s!</h1>' % request.match_info['name']
    return web.Response(body = text.encode(), headers = {"content-type": "text/html"})

async def init(loop):
    app = web.Application()
    app.add_routes([web.get("/", index),web.get("/login{name}", login)])

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '127.0.0.1', 8000)
    logging.info('server started at http://127.0.0.1:8000...')
    await site.start()

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()