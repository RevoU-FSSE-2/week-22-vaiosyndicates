from prisma import Prisma

async def getAllTodoById(id):
    prisma = Prisma()
    await prisma.connect()


    todo = await prisma.todo.find_many(where={'authorId': id, 'isDelete': False})
    toJson = [todo.model_dump() for todo in todo]
    await prisma.disconnect()
    return toJson

async def createTodo(title, task, priority, authorId):
    prisma = Prisma()
    await prisma.connect()

    todo = await prisma.todo.create(data={'title': title, 'task': task, 'priority': priority, 'authorId': authorId})
    await prisma.disconnect()

    return todo

async def checkTodo(idTodo, id):
    prisma = Prisma()
    await prisma.connect()

    # todo = await prisma.todo.update(where={'id': id}, data={'status': True})

    todo = await prisma.todo.find_first(
    where={
        'AND': [
            {
                'id': idTodo,
            },
            {
                'authorId': id,
            },
        ],
    },
    )

    if todo is not None:
        await prisma.disconnect()
        toJson = todo.model_dump()
        return toJson
    else:
        return {}

async def updateTodo(idTodo, title, task, priority, authorId):
    prisma = Prisma()
    await prisma.connect()

    todo = await prisma.todo.update(where={'id': idTodo}, data={'title': title, 'task': task, 'priority': priority, 'authorId': authorId})
    await prisma.disconnect()

    return todo

async def deleteTodo(idTodo,  isDeleted):
    prisma = Prisma()
    await prisma.connect()

    todo = await prisma.todo.update(where={'id': idTodo}, data={'isDelete': not isDeleted})
    await prisma.disconnect()

    return todo
