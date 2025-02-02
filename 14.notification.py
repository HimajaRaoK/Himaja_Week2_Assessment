'''14. Implement method overriding for a `Notification` class where 
`send()` is overridden in `EmailNotification` and `SMSNotification`.'''

class Notification:
    def send(self):
        print("Notification")

class SMSNotification(Notification):
    def __init__(self,message):
        self.message=message
    
    def send(self):
        super().send()
        print(f"the message in SMS is: {self.message}")

class EmailNotification(Notification):
    def __init__(self,message):
        self.message=message
    
    def send(self):
        print(f"the message in Email is: {self.message}")

S=SMSNotification("Hi im Hima")
E=EmailNotification("I love coding")
S.send()
E.send()