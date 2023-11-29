from prisma import Prisma

async def getUsers():
    prisma = Prisma()
    await prisma.connect()

    users = await prisma.user.find_many(where={'role': 'user'})
    await prisma.disconnect()

    toJson = [users.model_dump() for users in users]
    return toJson

async def getDetailUser(id):
    prisma = Prisma()
    await prisma.connect()

    user = await prisma.user.find_unique(where={'id': id})
    if user is not None:
        await prisma.disconnect()
        toJson = user.model_dump()
        return toJson
    else:
        return {}

async def deleteUser(id):
    prisma = Prisma()
    await prisma.connect()

    users = await prisma.user.delete(where={'id': id})
    await prisma.disconnect()

    return users

async def activateUser(id, isApproved):
    prisma = Prisma()
    await prisma.connect()

    users = await prisma.user.update(where={'id': id}, data={'isApprove': not isApproved})
    await prisma.disconnect()

    return users