import httpx
import asyncio
from datetime import datetime

async def fetch_hello(client, url):
    try:
        response = await client.post(url, data='hi')
        return response.text
    except httpx.RequestError as e:
        return f"An error occurred: {e}"

async def main():
    urls = ["http://localhost:8080/hello", "http://localhost:8081/hello"]
    
    async with httpx.AsyncClient(http2=True) as client:
        while True:
            # Send request to server 1
            result1 = await fetch_hello(client, urls[0])
            print(f"{datetime.now()} - Server 1 response: {result1}")
            await asyncio.sleep(1)  # 1 second delay
            
            # Send request to server 2
            result2 = await fetch_hello(client, urls[1])
            print(f"{datetime.now()} - Server 2 response: {result2}")
            await asyncio.sleep(1)  # 1 second delay

if __name__ == "__main__":
    asyncio.run(main())

