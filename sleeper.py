import asyncio
import datetime


async def my_sleep():
    print('my sleep start')
    await asyncio.sleep(2)
    print('my sleep stop')


async def main():
    print('sleep now')
    await my_sleep()
    print('sleep stop')

asyncio.run(main())
