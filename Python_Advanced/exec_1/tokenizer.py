# Falta terminar

import string

class Tokenizer:
    """
        Como funciona um tokenizer
        - O texto está dividido em tokens.
        - O modelo processa esses tokens.
        - A resposta é gerada como uma sequência de tokens e, em seguida, convertida novamente em texto.
    """
    def __init__(self):
        self.word_dict = dict()
        self.word_frequency = dict()
        self.characters = ["?", "!", ",", "."]

    # Transforma a entrada string em token
    def TransformToken(self, entrada_lista: list[str]):

        for entrada in entrada_lista:

            entrada_final = entrada
            for char in self.characters:
                quant = entrada_final.count(char)

                if quant > 0:
                    if char not in self.word_frequency:
                        self.word_frequency[char] = quant
                    else:
                        self.word_frequency[char] += quant

                    entrada_final = entrada_final.replace(char, "")

            wordsList = [word for word in entrada_final.split()]

            for word in wordsList:

                if word not in self.word_frequency:
                    self.word_frequency[word] = {
                        "identifier": string.ascii_lowercase,
                        "frequency": 1
                        }
                else:
                    self.word_frequency[word] += 1
        
            

        return self.word_frequency
    
    # Transforma a entrada token em string
    def TransformString(self, entrada: str):
        return

tokenizer = Tokenizer()
phrases = ["This is soo cool, because with tokenizers, we can generate LLMs!", "Hello World! cool", "Neural Networks are mathematician algorithms that predict something. cool"]

token = tokenizer.TransformToken(phrases)
print(token)