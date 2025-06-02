import asyncio

async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f"Accepted connection from {addr}")

    while True:
        data = await reader.read(100)
        if not data:
            print(f"Close connection from {addr}")
            writer.close()
            await writer.wait_closed()
            break
        message = data.decode()
    print(f"Received message from {addr}: {message}")
    res = "Message received"
    writer.write(res.encode())
    await writer.drain()
async def start_async_server():
    server = await asyncio.start_server(handle_client, '127.0.0.1', 65432)
    addr = server.sockets[0].getsockname()
    print(f"Server is listening on {addr}")
    async with server:
        await server.serve_forever()
if __name__ == '__main__':
    asyncio.run(start_async_server())
