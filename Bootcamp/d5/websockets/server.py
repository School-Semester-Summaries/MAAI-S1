import asyncio
import json
import logging
from datetime import datetime, timezone

from websockets import serve
from websockets.exceptions import ConnectionClosedOK, ConnectionClosedError

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")


def validate_object(obj):
    if not isinstance(obj, dict):
        raise ValueError("Payload must be a JSON object.")
    if len(obj) != 2:
        raise ValueError("Object must contain exactly two properties.")
    return True


async def send_json(ws, payload: dict):
    await ws.send(json.dumps(payload))

async def handle_client(ws):
    peer = ws.remote_address
    logging.info(f"Client connected: {peer}")

    try:
        async for raw in ws:
            # Parse JSON
            try:
                data = json.loads(raw)
            except json.JSONDecodeError:
                await send_json(ws, {
                    "status": "error",
                    "error": "invalid_json",
                    "message": "Message must be valid JSON."
                })
                continue

            # Validate object shape
            try:
                validate_object(data)
            except ValueError as e:
                await send_json(ws, {
                    "status": "error",
                    "error": "invalid_payload",
                    "message": str(e)
                })
                continue

            # Build and send response
            response = {
                "status": "ok",
                "received": data,
                "processedAt": datetime.now(timezone.utc).isoformat(),
                "info": "Processed object"
            }
            await send_json(ws, response)

    except (ConnectionClosedOK, ConnectionClosedError) as e:
        logging.info(f"Client disconnected {peer}: {e}")
    except Exception:
        logging.exception("Unexpected error in handler")
        # Best effort error back to client
        try:
            await send_json(ws, {
                "status": "error",
                "error": "server_error",
                "message": "An unexpected server error occurred."
            })
        except Exception:
            pass
    finally:
        logging.info(f"Connection closed: {peer}")


async def main():
    async with serve(handle_client, "localhost", 8765):
        print("Server is running on ws://localhost:8765")
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
