from pathlib import Path
import sys

PROJECT_DIR = str(
    Path(__file__).resolve().parent.parent
)
sys.path.append(PROJECT_DIR)

from py_leap_api.leap import TryLeap
import asyncio


async def main():
    leap = TryLeap("1be670a8-f8b6-4942-a7ee-bf4a96be6db7")

    model = await leap.create_model(title="test")
    print(model)
    
    leap.set_model(model=model["id"])
    

if __name__ == "__main__":
    asyncio.run(main())