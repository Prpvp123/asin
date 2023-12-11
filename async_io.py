import asyncio


async def async_func(task_no):
    print(f'....start {task_no}')
    await asyncio.sleep(2)
    print(f'....end {task_no}')


async def main():
    task_list = []
    task1 = asyncio.create_task(async_func('a'))
    task2 = asyncio.create_task(async_func('b'))
    task3 = asyncio.create_task(async_func('c'))
    await asyncio.wait([task1, task2, task3])


if __name__ == '__main__':
    asyncio.run(main())
