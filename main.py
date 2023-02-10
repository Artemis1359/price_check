import requests
import time

class Coin:

    def __init__(
                self, 
                name: str, 
                price: float=0, 
                old_price: float=0, 
                max_price: float=0, 
                max_price_lh: float=0.4)->None:
        self.name = name
        self.price = price
        self.old_price = old_price
        self.max_price = max_price
        self.max_price_lh = max_price_lh

    def price_info(self):
        url = 'https://www.binance.com/bapi/composite/v1/public/marketing/symbol/list'
        headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 YaBrowser/23.1.1.1138 Yowser/2.5 Safari/537.36"
        }
        result = requests.get(url, headers=headers).json()
        for coin in result['data']:
            if coin['name'] == self.name:
                self.price = coin['price']
                return self.price
            else:
                return False
    
    def price_check(self):
        if self.old_price != self.price_info():
            self.old_price = self.price_info()
            self.max_price = self.max_price_check()
        else:
            return False

    def max_price_check(self):
        if self.price>self.max_price:
            return self.price
        else: 
            return self.max_price
            
    def price_change(self):
        change = self.max_price/(self.max_price_lh/100)-100
        if change<=(-1) and self.max_price_check is False:
            print('Message')
        
    
    def hour_update(self):
        time.sleep(5)
        self.max_price_lh = self.max_price
        return self.max_price_lh


def main():
    coin1=Coin('XRP')
    

if __name__ == '__main__':
    while True:
        asyncio.run(main())

# import requests
# import threading
# import time

# class Coin:

#     def __init__(
#                 self, 
#                 name: str, 
#                 price: float=0, 
#                 old_price: float=0, 
#                 max_price: float=0, 
#                 max_price_lh: float=0.3)->None:
#         self.name = name
#         self.price = price
#         self.old_price = old_price
#         self.max_price = max_price
#         self.max_price_lh = max_price_lh

#     def price_info(self):
#         url = 'https://www.binance.com/bapi/composite/v1/public/marketing/symbol/list'
#         headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 YaBrowser/23.1.1.1138 Yowser/2.5 Safari/537.36"
#         }
#         while True:    
#             result = requests.get(url, headers=headers).json()
#             for coin in result['data']:
#                 if coin['name'] == self.name:
#                     self.price = coin['price']
#                     if self.old_price != self.price:
#                         print (f'old_price {self.old_price}')
#                         print(f'price {self.price}')
#                         self.old_price = self.price
#                         if self.price>self.max_price:
#                             self.max_price = self.price
#                             print(f'max_price {self.max_price}')
#                         else:        
#                             change = self.max_price/(self.max_price_lh/100)-100
#                             print(f'change {change}')
#                             if change<=(-1):
#                                 print('Message')
                        
                        
        

#     def hour_update(self):
#         while True:
#             self.max_price_lh = self.max_price
#             time.sleep(3600)
#             print(f'max_price_lh {self.max_price_lh}')        


# if __name__ == '__main__':
#     coin1=Coin('XRP')
    
#     a = threading.Thread(target=coin1.price_info, name="A")
#     b = threading.Thread(target=coin1.hour_update, name = "B", daemon=True)

#     a.start()
#     b.start()