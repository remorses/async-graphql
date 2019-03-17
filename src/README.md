
[![CircleCI](https://circleci.com/gh/remorses/async-graphql/tree/master.svg?style=svg)](https://circleci.com/gh/remorses/async-graphql/tree/master)


Make graphql requests asynchronously, python 2.7 and more required.
Soon will come graphql subscriptions.


The library is tiny, memory usage loading the module is also is good:
```
Line #    Mem usage    Increment   Line Contents
================================================
    12     10.9 MiB     10.9 MiB   @profile
    13                             def profiled():
    14     13.0 MiB      2.1 MiB       import asyncio
    15     13.0 MiB      0.0 MiB       async def main(loop):
    16     13.5 MiB      0.5 MiB       from async_graphql import Client, errors
```
This is good when using graphql in lots of replicated micro-services to not go out of memory.
