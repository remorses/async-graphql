from async_graphql import Client
import json
import asyncio



client = Client('http://clusterimages.fun:4466')



async def main():
    query = """
        bots {
            instagram {
                username
            }
        }
    """
    resp = await client.execute(query)

    print(resp.get('data') or f'error {json.dumps(resp)}')



asyncio.run(main())
