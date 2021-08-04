import ssl
import warnings

from aiohttp import web, ClientSession

import config

app = web.Application()


class TelegramRouter(web.View):
    _session = None

    @classmethod
    async def get_session(cls):
        if not cls._session:
            cls._session = ClientSession()
        return cls._session

    async def proxy_post(self, url: str):
        session: ClientSession = await self.get_session()

        async with session.post(url, data=await self.request.read()) as resp:
            return web.Response(body=await resp.read())

    async def post(self):
        proxy_pass = self.request.query[config.QUERY_PROXY_KEY]
        return await self.proxy_post(proxy_pass)


try:
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ssl_context.load_cert_chain(config.SSL_CERT_FILE, config.SSL_KEY_FILE)
except:
    warnings.warn('SSL certificate not found.')
    ssl_context = None

app.router.add_post(config.TELEGRAM_ROUTE, TelegramRouter)
web.run_app(app, host=config.APP_HOST, port=config.APP_PORT, ssl_context=ssl_context)
