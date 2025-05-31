import asyncio

async def fetch_weather():
    print("Fetching weather data...")
    await asyncio.sleep(2)
    print("Weather data received.")
    return {"temp": 28, "condition": "Sunny"}

async def fetch_news():
    print("Fetching news headlines...")
    await asyncio.sleep(3)
    print("News data received.")
    return ["Headline 1", "Headline 2", "Headline 3"]

async def main():
    print("Starting asynchronous tasks...\n")

    # Run both coroutines concurrently and wait for both to complete
    weather, news = await asyncio.gather(
        fetch_weather(),
        fetch_news()
    )

    print("\nResults:")
    print(f"Weather: {weather}")
    print(f"News: {news}")

if __name__ == "__main__":
    asyncio.run(main())