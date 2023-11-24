from prisma import Prisma
from prisma.models import Post

async def getAllPost():
    db = Prisma(auto_register=True)
    await db.connect()

    post = await Post.prisma().find_many()
    toJson = [post.model_dump() for post in post]
    await db.disconnect()
    return toJson

async def getAllPostById(id):
    print('id', id)
    db = Prisma(auto_register=True)
    await db.connect()

    post = await Post.prisma().find_many(where={'authorId': int(id)})
    toJson = [post.model_dump() for post in post]
    await db.disconnect()
    return toJson

async def createPost(title, idUser):
    db = Prisma(auto_register=True)
    await db.connect()

    post = await Post.prisma().create(data={'title': title, 'authorId': idUser})
    await db.disconnect()

    return post
