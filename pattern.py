import aiohttp
import asyncio
from typing import Coroutine, Any


async def fetch_data(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()
        

async def main() -> None:
    url = "https://jsonplaceholder.typicode.com/posts/1"  # 예제 URL, 원하는 URL로 변경 가능
    
    # gather 사용 5번 요청 
    tasks: list[Coroutine[Any, Any, str]] = [fetch_data(url) for _ in range(5)]
    results: Any = await asyncio.gather(*tasks)
    
    # 결과 출력
    for i, result in enumerate(results, 1):
        print(f"Response {i}: {result}")
        


if __name__ == "__main__":
    asyncio.run(main())