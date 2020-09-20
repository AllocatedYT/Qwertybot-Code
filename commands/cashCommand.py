from commands.base_command import BaseCommand
import random

class Cash(BaseCommand):
    def __init__(self):
        description = "Gives you Qwertycoin."
        params = ["multiplier"]
        super().__init__(description, params)

    async def handle(self, params, message, client):
      multi = params[0]
      gain = random.randint(1,301)*multi
      
