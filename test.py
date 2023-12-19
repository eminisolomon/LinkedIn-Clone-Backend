import asyncio
import motor.motor_asyncio

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.test
collection = database.test


async def insert():
    res = await collection.insert_one({"id": 2})
    print(res.inserted_id)


async def read():
    async for document in collection.find({}):
        print(document)


# Run the asynchronous functions using asyncio
asyncio.run(insert())
asyncio.run(read())
