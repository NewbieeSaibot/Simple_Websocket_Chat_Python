import asyncio
import websockets

disconnect_message = "0"
connections = []

async def handle_client(websocket, path):
    global disconnect_message
    name = await websocket.recv()
    connections.append([websocket, str(name)])
    while True:
        msg = await websocket.recv()
        print(msg)
        if(msg == disconnect_message):
            connections.remove([websocket, str(name)])
            break
        for i in range(len(connections)):
            if(connections[i][0] != websocket):
                await connections[i][0].send(name + ": " + msg)

start_server = websockets.serve(handle_client, "127.0.0.1", 5000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()