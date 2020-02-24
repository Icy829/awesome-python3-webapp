# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

# web app建立在asyncio的基础上，用aiohttp写一个基本的app.py
import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, _json, time
from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>awesome hello word</h1>', content_type='text/html')# 教程文档缺少content_type='text/html'
'''
@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('serve started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
'''

# 新

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('serve started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()