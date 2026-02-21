class Cache: 
    def __init__(self, max_size=10):
        self.Cache_List = dict()
        if max_size < 0:
            raise Exception("O tamanho máximo não pode ser menor que 0")
        else:
            self.Max_Size = max_size

    # Funções Públicas
    def AddItem(self, value):
        extra_dict = dict()
        i = 1

        extra_dict[0] = value

        for (_, v) in self.Cache_List.items():
            if i >= self.Max_Size:
                break
            
            extra_dict[i] = v

            i += 1


        self.Cache_List = extra_dict
    
    def GetCache(self):
        return self.Cache_List


cache = Cache()

# Teste de Cache
for c in range(15):
    cache.AddItem(c)
    print(f"{len(cache.GetCache())} - {cache.GetCache()}")