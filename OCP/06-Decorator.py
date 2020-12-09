class Greeting:
    def __init__(self, username):
        self.username = username

    def greet(self):
        pass


class BaseGreeting(Greeting):
    def __init__(self, username):
        Greeting.__init__(self, username)

    def greet(self):
        return f'Hello, {self.username}'


class GreetingDecorator:
    def __init__(self, wrapper):
        self.wrapper = wrapper

    def greet(self):
        base_greeting = self.wrapper.greet()
        return base_greeting.upper()


decor = GreetingDecorator(BaseGreeting('Masha'))
print(decor.greet())
