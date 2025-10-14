from services.crypto.price_client import CryptoPriceClient
import asyncio



async def main():
    parser = CryptoPriceClient()
    price_data = await parser.get_price("bitcoin", "usd,rub")
    print(f"Цена: ${price_data["price_usd"]:,.2f}")
    print(f"Цена: ${price_data["price_rub"]:,.2f}")
    print(f"Монета: {price_data["coin"]}")

if __name__ == "__main__":
    asyncio.run(main())
