from main import Singleton

print("Esse é o teste")
s1 = Singleton()

# Se mantem o mesmo valor do que na main!
print(s1.value)