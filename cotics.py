import asyncio
import httpx


async def download(current_activity):
    url = f'https://www.boredapi.com/api/activity'

    async with httpx.AsyncClient() as client:
        r = await client.get(url)
        if r.status_code == 200:
            _r = r.json()
            print(_r.get('activity'), )
        else:
            print(r.status_code)
        print(f'Рекомендую {current_activity}')


async def main():
    page_count = int(input('сколько развлечений нужно?    '))

    current_activity = 0
    while current_activity < page_count:
        current_activity += 1
        await download(current_activity)
    print('Done')

asyncio.run(main())
