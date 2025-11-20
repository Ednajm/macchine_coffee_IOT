import asyncio
from aiocoap import *

async def main():
    uri = "coap://127.0.0.1:5683/temperature"

    # Crea contesto CoAP
    protocol = await Context.create_client_context()

    # Crea richiesta GET
    request = Message(code=GET, uri=uri)

    # Invia richiesta e attendi risposta
    try:
        response = await protocol.request(request).response
        print("Risposta server:")
        print(response.payload.decode())
    except Exception as e:
        print("Errore:", e)

if __name__ == "__main__":
    asyncio.run(main())
