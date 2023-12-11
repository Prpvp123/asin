import asyncio


async def plus(a, b):
    print(f'сложение началось')
    await asyncio.sleep(3)
    return a + b


async def square(a):
    print(f'возведение в квадрат')
    await asyncio.sleep(1)
    print(a ** 2)


async def main():
    count = list()

    task1 = asyncio.create_task(plus(4, 6))
    task2 = asyncio.create_task(square(12345678))

    await asyncio.gather(task1, task2)

asyncio.run(main())