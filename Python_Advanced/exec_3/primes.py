import os, json

class PrimeGen:
    def __init__(self, prime_list :list[int], non_prime_list :list[int]):
        self.prime_list = prime_list
        self.non_prime_list = non_prime_list

        # Pega o maior valor de uma das listas
        if self.prime_list[-1] > self.non_prime_list[-1]:
            self.num = self.prime_list[-1] + 1
        else:
            self.num = self.non_prime_list[-1] + 1
    
    def GetPrimes(self, val :int=10):
        for _ in range(val):
            save = self.num

            for p in range(len(self.prime_list)):
                if self.num % self.prime_list[p] == 0:
                    print(f"NP {self.num} / {self.prime_list[p]}")
                    self.non_prime_list.append(self.num)
                    self.num += 1
                    p = 0
                    continue
                
            for p in self.non_prime_list:
                if self.num % p == 0:
                    print(f"NP {self.num} / {p}")
                    self.non_prime_list.append(self.num)
                    self.num += 1
                    break
            
            if save == self.num:
                self.prime_list.append(self.num)
                print(f"P {self.num}")
                self.num += 1
            else:
                pass

        return self.prime_list, self.non_prime_list
            
            
        

file = "primes.json"
if not os.path.isfile(file):
    with open(file, "w") as f:
        print(f"Created path: {file}")
        json_data = json.dumps({
            "primes": [2, 3, 5],
            "composites": [4]
        })
        f.write(json_data)
        f.close()

# Lê json e converte para dict
f = open(file, "r")
f = json.loads(f.read())

primeGen = PrimeGen(f["primes"], f["composites"])
primes, composites = primeGen.GetPrimes()


data = {
    "primes": primes,
    "composites": composites
}
# Transforma em json
json_data = json.dumps(data)

# Salva no arquivo
with open(file, "w") as f:
    f.write(json_data)
    f.close()