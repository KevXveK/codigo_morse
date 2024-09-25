codigo_morse = { #alfabeto,numeros e simbolos em python  
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',    
    'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',    'J': '.---', 
    'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---',  
    'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',    
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',  'Y': '-.--', 
    'Z': '--..',  '0': '-----',  '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-',  '5': '.....', '6': '-....', '7': '--...', '8': '---..', 
    '9': '----.',  ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', 
    '-': '-....-', '(': '-.--.',  ')': '-.--.-', '&': '.-...', ':': '---...', 
    ';': '-.-.-.', '=': '-...-',  '+': '.-.-.',  '_': '..--.-', '"': '.-..-.', 
    '$': '...-..-', '@': '.--.-.'
}
def conversor_morse(): # função que traduz texto para morse e morse para texto
    resposta = int(input("Digite o numero 1 para traduzir texto para morse ou 2 para morse para texto: ")) # pede uma escolha para o usuario
    traducao = []                                                                        # lista que vai ser armazenado a tradução

    if resposta == 1:
        texto = input(f"Digite o texto  que deseja transformar em codigo morse: ").upper()
        for letra in texto:
            if letra in codigo_morse:
                traducao.append(codigo_morse[letra])  #cria um loop que itera sobre cada caracter e devolve o valor da chave desse caracter
        return ' '.join(traducao) # retorna a variavel como uma string
    elif resposta == 2:
        texto = input("digite o codigo morse separado por espaço").split()
        for cod in texto:
            for chave,valor in codigo_morse.items():
                if cod == valor:
                    traducao.append(chave)
                    break
        return ' '.join(traducao)
resultado = conversor_morse()
print(resultado)
			
			



