from prisma import Prisma
from prisma.models import User
import json

async def getUserAll():
    db = Prisma(auto_register=True)
    await db.connect()

    user = await User.prisma().find_many()
    toJson = [user.model_dump() for user in user]
    await db.disconnect()
    return toJson

async def registerUser(name, email, address, password, role):
    db = Prisma(auto_register=True)
    await db.connect()

    user = await User.prisma().create(data={'name': name, 'email': email, 'address': address, 'password': password, 'role': role})
    
    await db.disconnect()
    return user

async def getUserByEmail(email):
    db = Prisma(auto_register=True)
    await db.connect()

    user = await User.prisma().find_unique(where={'email': email})
    if user is not None:
        toJson = user.model_dump()
        await db.disconnect()
        return toJson
    else:
        return {}


async def getUserById(id):
    db = Prisma(auto_register=True)
    await db.connect()

    user = await User.prisma().find_unique(where={'id': int(id)})
    toJson = user.model_dump()
    await db.disconnect()
    return toJson

async def userProfileTes(id):
    # print('masuk', id)
    db = Prisma(auto_register=True)
    await db.connect()

    user = await User.prisma().find_unique(
        where={
            'id': int(id),
        },
        include={
            'posts': {
                'take': 2,
            },
            'follows': {
                'take': 2,
            },
        },
    )
    # print(user)

    toJson = user.model_dump()
    # print(toJson)

    await db.disconnect()
    return toJson