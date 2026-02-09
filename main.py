from fastapi import FastAPI, WebSocket

app = FastAPI()
clients = []

@app.websocket("/ws")
async def ws_endpoint(ws: WebSocket):
    await ws.accept()
    clients.append(ws)
    try:
        while True:
            msg = await ws.receive_text()
            for c in clients:
                if c != ws:
                    await c.send_text(msg)
    except:
        clients.remove(ws)
