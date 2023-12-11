import time
import asyncio


async def brew_coffe():
    print('Start brew coffee')
    await asyncio.sleep(2)
    print('Finish brew coffee')
    return 'coffe is ready'


async def toast_begal():
    print('Start toast begal')
    await asyncio.sleep(4)
    print('Finish toast begal')
    return 'begal is ready'


async def main():
    start = time.time()

    # batch = asyncio.gather(brew_coffe(), toast_begal())
    # result_coffee, result_begal = await batch

    taskc = asyncio.create_task(brew_coffe())
    taskd = asyncio.create_task(toast_begal())

    result_coffee = await taskc
    result_begal = await taskd

    end = time.time()

    print(result_coffee)
    print(result_begal)
    print(f'spend time {end - start:.2f} seconds')


if __name__ == '__main__':
    asyncio.run(main())
