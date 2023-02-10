import requests
import threading
import time


class Coin:

    def __init__(
                self,
                name: str,
                price: float = 0,
                old_price: float = 0,
                max_price: float = 0.01,
                max_price_lh: float = 0.01) -> None:
        self.name = name
        self.price = price
        self.old_price = old_price
        self.max_price = max_price
        self.max_price_lh = max_price_lh

    def price_info(self) -> None:
        url = (
            'https://www.binance.com/bapi/'
            'composite/v1/public/marketing/symbol/list'
        )
        headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0'
                    'YaBrowser/23.1.1.1138 Yowser/2.5 Safari/537.36'
        }
        while True:
            result = requests.get(url, headers=headers).json()
            for coin in result['data']:
                if coin['name'] == self.name:
                    self.price = coin['price']
                    if self.old_price != self.price:
                        self.old_price = self.price
                        if self.price > self.max_price:
                            self.max_price = self.price
                        else:
                            change = self.price / (self.max_price_lh/100) - 100
                            if change <= (-1):
                                print('Change down more than 1%')

    def hour_update(self):
        while True:
            self.max_price_lh = self.max_price
            self.max_price = 0.01
            time.sleep(6)


if __name__ == '__main__':
    coin1 = Coin('XRP')

    a = threading.Thread(target=coin1.price_info, name="A")
    b = threading.Thread(target=coin1.hour_update, name="B", daemon=True)

    a.start()
    b.start()
