'''12. Write a `Payment` class with a method `process_payment()`. 
Implement subclasses `CreditCardPayment`, `PayPalPayment`, and `BitcoinPayment` 
that override the method differently.'''

class Payment:
    def pay(self):
        pass

class CreditCardPayment(Payment):
    def pay(self):
        print("Payment done using credit card")

class PayPalPayment(Payment):
    def pay(self):
        print("Payment done using PayPal")

class BitcoinPayment(Payment):
    def pay(self):
        print("Payment done using Bitcoin")

obj1 = CreditCardPayment()
obj1.pay()

obj2 = PayPalPayment()
obj2.pay()

obj3 = BitcoinPayment()
obj3.pay()
