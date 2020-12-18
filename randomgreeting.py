# Print random greeting

from random import randint

messages = ["Hello World", "Hi", "What's up doc?"]
print(messages[randint(0,len(messages)-1)])
