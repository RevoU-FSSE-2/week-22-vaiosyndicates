from prisma import Prisma
from prisma.models import Follow

async def addFollower(idSelf, idOther):

    db = Prisma(auto_register=True)
    await db.connect()

    follow = await Follow.prisma().create(data={'idSelf': idSelf, 'idOther': int(idOther)})
    await db.disconnect()

    return follow

async def deleteFollower(idSelf, idOther):
    db = Prisma(auto_register=True)
    await db.connect()

    follow = await Follow.prisma().delete_many(where={'idSelf': idSelf, 'idOther': int(idOther)})
    await db.disconnect()

    return follow

async def checkIsIDExist(idSelf, idOther):
    db = Prisma(auto_register=True)
    await db.connect()


    user = await Follow.prisma().find_first(
    where={
        'AND': [
            {
                'idSelf': idSelf,
            },
            {
                'idOther': int(idOther),
            },
        ],
    },
    )
    toJson = user.model_dump()
    await db.disconnect()
    
    return toJson
