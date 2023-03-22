from pathlib import Path
import sys

PROJECT_DIR = str(
    Path(__file__).resolve().parent.parent
)
sys.path.append(PROJECT_DIR)

from src.py_leap_api.leap import TryLeap
import asyncio


async def main():
    leap = TryLeap("API")

    model = await leap.create_model(title="test")
    print(model)
    
    leap.set_model(model=model["id"])
    

if __name__ == "__main__":
    asyncio.run(main())