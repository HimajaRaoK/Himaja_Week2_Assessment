'''11. Create a class `Logger` with a method `log(message)`. 
Implement method overloading to log different message types (`error`, `warning`, `info`).'''

class logger:
    def log(self,error=None,warning=None,info=None):
        print(f"error: {error}\nwarning: {warning}\ninfo: {info}")

logger0=logger()
logger0.log('error','no warnings','no info')
print("\n")
logger1=logger()
logger1.log('no error')