import asyncio


async def count(counter):
    print(f'количество записей в списке {counter}')
    while True:
        await asyncio.sleep(1 / 1000)
        counter.append(1)


async def print_every_sec(counter):
    while True:
        await asyncio.sleep(1)
        print(f'- one sec passed. Count = {len(counter)}')


async def print_every_5_sec():
    while True:
        await asyncio.sleep(5)
        print(f'5 sec passed')


async def print_every_10_sec():
    while True:
        await asyncio.sleep(10)
        print(f'10 sec passed')


async def main():
    counter = list()
    # task1 = asyncio.create_task(count(counter))
    # task2 = asyncio.create_task(print_every_sec(counter))
    # task3 = asyncio.create_task(print_every_5_sec())
    # task4 = asyncio.create_task(print_every_10_sec())
    # await asyncio.wait([task1, task2, task3, task4])

    task_list = [
        count(counter),
        print_every_sec(counter),
        print_every_5_sec(),
        print_every_10_sec()
    ]
    await asyncio.gather(*task_list)

asyncio.run(main())
