import asyncio
async def tcp_client(msg):
    reader, writer = await asyncio.open_connection('127.0.0.1', 65432)
    print(f"Sending: {msg}")
    writer.write(msg.encode())
    await writer.drain()
    data = await reader.read(100)
    print(f"Received: {data.decode()}")
    print("Closing the conection")
    writer.close()
    await writer.wait_closed()

if __name__ == '__main__':
    msg = "Hello, async server!"
    asyncio.run(tcp_client(msg))
