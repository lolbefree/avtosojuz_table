import asyncio


async def f():
    for i in range(100)[::-1]:
        print(f"def f:{i}")
        if i == 50:
            await asyncio.sleep(5)


async def g():
    for i in range(100):
        print(f"def g:{i}")
        await asyncio.sleep(1)


async def main():
    main_loop.create_task(g())
    main_loop.create_task(f())


main_loop = asyncio.get_event_loop()
main_loop.run_until_complete(main())
main_loop.run_forever()
