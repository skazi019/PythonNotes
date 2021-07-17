import asyncio
import time

'''
async def main():
	print("Hello...")
	await asyncio.sleep(5)
	print("...World")

# asyncio.run(main())
main()
'''

async def say_after(delay, what):
	await asyncio.sleep(delay)
	print(what)

async def main():
	print(f"Started at {time.strftime('%X')}")

	await say_after(1, 'hello')
	await say_after(3, 'world')

	print(f"Ended at {time.strftime('%X')}")

asyncio.run(main())