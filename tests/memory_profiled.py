import json
from memory_profiler import profile

URL = 'https://countries.trevorblades.com'
# URL = 'http://clusterimages.fun:4466'






@profile
def profiled():
    import asyncio
    async def main(loop):

        from async_graphql import Client, errors


        try:
            client = Client(URL, loop=loop)

            query = """
                query {
                    countries {
                        code
                    }
                }
            """
            resp = await client.execute(query,)

            print(json.dumps(resp, indent=4))

        except errors.HTTPError as e:
            print(e)
            print(e.msg)
            print()
            print(json.dumps(json.loads(e.read()),indent=4))
    loop=asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main(loop))

profiled()
