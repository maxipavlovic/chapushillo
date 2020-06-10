import asyncio

from pusher_client import pusher_client


async def push():
    await pusher_client.trigger('private-foobar', 'my-event', {'message': 'hello world'})


asyncio.run(push())
