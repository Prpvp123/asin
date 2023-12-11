import asyncio


async def calls():
    await asyncio.sleep(1)
    print(f'секретарь отвечает на звонки')
    await asyncio.sleep(1)
    print(f'разговаривает по телефону')


async def takes():
    await asyncio.sleep(1)
    print(f'секретарь принимает людей')


async def airlines():
    await asyncio.sleep(1)
    print(f'бронрует билеты')


async def graphics():
    await asyncio.sleep(1)
    print(f'редактирует график работ')


async def docks():
    await asyncio.sleep(1)
    print(f'заполняет документы')


async def main():
    task_list = [
        calls(),
        takes(),
        calls(),
        airlines(),
        calls(),
        graphics(),
        docks(),
    ]
    await asyncio.gather(*task_list)

asyncio.run(main())
