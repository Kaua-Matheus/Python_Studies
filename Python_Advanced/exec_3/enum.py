from enum import Enum

# With enum, you can insert exclusive params in your code
class Type(Enum):
    FORMAL = "formal"
    INFORMAL = "informal"

def hello_word(type: Type):
    if type == Type.FORMAL:
        print("Hello world!")
    if type == Type.INFORMAL:
        print("What's up world!")


hello_word(Type.FORMAL)
hello_word(Type.INFORMAL)