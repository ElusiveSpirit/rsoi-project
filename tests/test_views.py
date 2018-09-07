from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop
from app.main import init_app



class TestIndexView(AioHTTPTestCase):
    async def get_application(self):
        return init_app()

    @unittest_run_loop
    async def test_example(self):
        request = await self.client.request('GET', '/')
        assert request.status == 200
        text = await request.text()
        assert 'Hello world' in text
