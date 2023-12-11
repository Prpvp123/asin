import asyncio


# def multiply(a, b):
#     return a * b

async def async_function(a):
    while True:
        print(a)
        a *= 1234567890

asyncio.run(async_function(1234567890))
