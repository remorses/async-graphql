from async_graphql import Client
import json
import asyncio






async def main(loop):
    client = Client('http://clusterimages.fun:4466', loop=loop)

    query = """
        query {
            bots {
                instagram {
                    username
                }
            }
        }
    """
    resp = await client.execute(query,)

    print(resp.get('data') or f'error {json.dumps(resp)}')


loop=asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(main(loop))
