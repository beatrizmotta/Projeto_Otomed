from turtle import clear
import slate3k
import re 
from datetime import datetime
import pywhatkit
import os

def starts_with_0_or_1(strng):
    if (strng.startswith('8') or strng.startswith('9')):
        return True
    else:
        return False

def del_hifens(char):
    if (char != '-' or char != ' '):
        return True
    else:
        return False

def clear_duplicates(number):
    appearances = 0
    for i in range(0, len(treated_numbers)):
        treated_numbers[i] == number
        appearances += 1
    if (appearances == 1):
        return True
    elif (appearances > 1):
        return False


def extract(archive):
    file = open(archive, 'rb')
    doc = slate3k.PDF(file)

    telefones = list()

    for i in doc:
        tels_current_page = re.findall("(?<![0-9])[0-9]{4,5}[0-9]{4}(?![0-9]{2,5})|[0-9]{2} [0-9]{4,5}[0-9]{4}|[0-9]{2} [0-9]{4,5}-[0-9]{4}|[0-9]{4,5}-[0-9]{4}|[0-9]{2} [0-9]{4,5}-[0-9]{4}|9 [0-9]{4,5}-[0-9]{4}|9-[0-9]{4,5}-[0-9]{4}|9.[0-9]{4,5}-[0-9]{4}|[0-9]{2} 9 [0-9]{4,5}-[0-9]{4}|[0-9]{2} 9-[0-9]{4,5}-[0-9]{4}|[0-9]{2} 9.[0-9]{4,5}-[0-9]{4}", i)
        tels_current_page = list(filter(starts_with_0_or_1, tels_current_page))   
        for k in tels_current_page:
            telefones.append(k)

    file.close()
    return telefones

disallowed_chars = ["-", " ", "."]

nome_arquivo = input("Diga o nome do arquivo: ")

not_treated_numbers = extract(nome_arquivo)
numbers_without_char = list()
treated_numbers = list()


for i in not_treated_numbers:
    for k in disallowed_chars:
        i = i.replace(k, "")
    numbers_without_char.append(i)

# Complementa os números estão sem 9 no começo ou sem DDD (assumimos que é 82 se não tiver)
for i in numbers_without_char:
    if (len(i) == 8):
        new_number = f'55829{i}'
    elif (len(i) == 9):
        new_number = f'5582{i}'
    elif (len(i) == 1):
        new_number = f'55{i}'
    treated_numbers.append(new_number)

# Remove números iguais
treated_numbers = list(dict.fromkeys(treated_numbers))

## EXPLICAÇÃO ## 


# --> Loop para mandar as mensagens pelo pywhatkit (OPÇÃO 1)

# for i in treated_numbers:
#     now = datetime.now()
#     hour = now.hour
#     minute = now.minute+1
#     print('xinxa')
#     pywhatkit.sendwhatmsg(f'+{i}', "Gostaríamos de saber como foi seu atendimento na Otomed. \nResponda nossa pesquisa de satisfação, sua avaliação é muito importante para o aprimoramento dos nossos serviços.\nÉ rápido e fácil, basta clicar no link abaixo👇🏻\n\nhttps://forms.gle/XYVqhWg4pmpJJvq56\n\nDesde já agradecemos,\nOtomed-Al", hour, minute)    



# --> Loop para ir mandando manualmente (vai mostrando os números/links de um por um e a própria pessoa vai mandando)

# clear = lambda: os.system('cls')
# quantity = 1
# for i in treated_numbers:
#     print('\n')
#     print(f'https://api.whatsapp.com/send?phone={i}&text=Gostar%C3%ADamos%20de%20saber%20como%20foi%20seu%20atendimento%20na%20Otomed.%20%0aResponda%20nossa%20pesquisa%20de%20satisfa%C3%A7%C3%A3o,%20sua%20avalia%C3%A7%C3%A3o%20%C3%A9%20muito%20importante%20para%20o%20aprimoramento%20dos%20nossos%20servi%C3%A7os.%0a%C3%89%20r%C3%A1pido%20e%20f%C3%A1cil,%20basta%20clicar%20no%20link%20abaixo%F0%9F%91%87%F0%9F%8F%BB%0a%0ahttps%3A%2F%2Fforms.gle%2FXYVqhWg4pmpJJvq56%0a%0aDesde%20j%C3%A1%20agradecemos,%0aOtomed-Al')
#     print('\n')
#     print(f'{quantity} of {len(treated_numbers)}')
#     quantity += 1
#     pause = input("> ")
#     clear()






