import asyncio
from typing import Any, Awaitable
import httpx


async def send_and_parse(
    method:str, url: str, headers:dict, params:dict=None, json:dict=None,
    files:dict=None
) -> dict:
    async with httpx.AsyncClient() as client:
        r = await client.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            json=json,
        )
    if r.status_code in range(200,299):
        return r
    raise Exception(f"TryLeap response error: {r.text}")


async def run_parallel(*functions: Awaitable[Any]) -> None:
    return await asyncio.gather(*functions)
