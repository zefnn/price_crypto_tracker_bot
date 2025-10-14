import asyncio
import aiohttp
from typing import Optional, Dict

class CryptoPriceClient:
    def __init__(self):
        self.base_url = "https://api.coingecko.com/api/v3"

    # Асинхронно получает цену криптовалюты
    async def get_price(self, coin_id: str, vs_currency: str = 'usd,rub') -> Optional[Dict]:
        url = f"{self.base_url}/simple/price"
        params = {
            "ids": coin_id,
            "vs_currencies": vs_currency,
            "include_24hr_change": 'true'
        }

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, params=params, timeout=10) as response:
                    if response.status == 200:
                        data = await response.json()
                        return {
                            "coin": coin_id,
                            "price_usd": data[coin_id]['usd'],
                            "price_rub": data[coin_id]['rub'],
                            "change_24h": data[coin_id].get(f"usd_24h_change")
                        }
                    else:
                        print(f"API вернул {response.status}")
                        return None
        except asyncio.TimeoutError:
            print("Таймаут при запросе к API")
            return None
        except Exception as e:
            print(f"Ошибка при запросе: {e}")
            return None