from prisma import Prisma
from prisma.models import User
import json


async def registerUser(name, email, address, password):
    prisma = Prisma()
    await prisma.connect()

    user = await prisma.user.create(data={'name': name, 'email': email, 'address': address, 'password': password })
    
    await prisma.disconnect()
    return user

async def getUserByEmail(email):
    prisma = Prisma()
    await prisma.connect()


    user = await prisma.user.find_unique(where={'email': email})
    if user is not None:
        toJson = user.model_dump()
        await prisma.disconnect()
        return toJson
    else:
        return {}