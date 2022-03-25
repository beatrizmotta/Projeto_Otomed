import slate3k
import re 

def extract():
    file = open('agenda.pdf', 'rb')
    doc = slate3k.PDF(file)

    print(type(doc))

    telefones = list()

    page = 0
    for i in doc:
        print("Pagina:", page)
        

        #Primeiro
        #telefones_page = re.findall("[0-9]{4,5}-[0-9]{4}|9[0-9]{3}[0-9]{4}|9[0-9]{3}[0-9]{4}|9 [0-9]{4}-[0-9]{4}|9 [0-9]{4,5}[0-9]{4}|^9[0-9]{4,5}[0-9]{4}|[0-9]{2}-[0-9]{4,5}[0-9]{4}|[0-9]{2}-[0-9]{4,5}-[0-9]{4}|9[0-9]{4}[0-9]{4}", i)
        # Todos que: 
        # (?<![0-9])[0-9]{4,5}[0-9]{4}(?![0-9]{2,5})
        # [0-9]{4,5}-[0-9]{4} 
        # 9[0-9]{3}[0-9]{4}
        # 9[0-9]{3}[0-9]{4}
        # 9 [0-9]{4}-[0-9]{4}
        # 9 [0-9]{4,5}[0-9]{4}
        # ^9[0-9]{4,5}[0-9]{4}
        # [0-9]{2}-[0-9]{4,5}[0-9]{4}
        # [0-9]{2}-[0-9]{4,5}-[0-9]{4}
        # 9[0-9]{4}[0-9]{4}
        # [0-9]{2} 9 [0-9]{4,5}-[0-9]{4}
        # [0-9]{2} 9-[0-9]{4,5}-[0-9]{4}
        # [0-9]{2} 9.[0-9]{4,5}-[0-9]{4}
        # 9 [0-9]{4,5}-[0-9]{4}
        # 9-[0-9]{4,5}-[0-9]{4}
        # 9.[0-9]{4,5}-[0-9]{4}
        #
        #Segundo
        # (?<![0-9])[0-9]{4,5}[0-9]{4}(?![0-9]{2,5})
        # [0-9]{2} [0-9]{4,5}[0-9]{4}
        # [0-9]{2} [0-9]{4,5}-[0-9]{4}
        # [0-9]{4,5}-[0-9]{4}
        # [0-9]{2} [0-9]{4,5}-[0-9]{4}
        # 9 [0-9]{4,5}-[0-9]{4}
        # 9-[0-9]{4,5}-[0-9]{4}
        # 9.[0-9]{4,5}-[0-9]{4}
        # 9[0-9]{3}[0-9]{4}
        # 9[0-9]{3}[0-9]{4}
        # 8[0-9]{3}[0-9]{4}
        # 8[0-9]{3}[0-9]{4}
        # [0-9]{2} 9 [0-9]{4,5}-[0-9]{4}
        # [0-9]{2} 9-[0-9]{4,5}-[0-9]{4}
        # [0-9]{2} 9.[0-9]{4,5}-[0-9]{4}
        #
        #
        #
        
        def starts_with_0_or_1(strng):
            if (strng.startswith('8') or strng.startswith('9')):
                return True
            else:
                return False
        
        # telefones_page = re.findall("(?<![0-9])[0-9]{4,5}[0-9]{4}(?![0-9]{2,5})|[0-9]{2} [0-9]{4,5}[0-9]{4}|[0-9]{2} [0-9]{4,5}-[0-9]{4}|[0-9]{4,5}-[0-9]{4}|[0-9]{2} [0-9]{4,5}-[0-9]{4}|9 [0-9]{4,5}-[0-9]{4}|9-[0-9]{4,5}-[0-9]{4}|9.[0-9]{4,5}-[0-9]{4}|[0-9]{2} 9 [0-9]{4,5}-[0-9]{4}|[0-9]{2} 9-[0-9]{4,5}-[0-9]{4}|[0-9]{2} 9.[0-9]{4,5}-[0-9]{4}", i)
        telefones_page = re.findall("(?<![0-9])[0-9]{4,5}[0-9]{4}(?![0-9]{2,5})|[0-9]{2} [0-9]{4,5}[0-9]{4}|[0-9]{2} [0-9]{4,5}-[0-9]{4}|[0-9]{4,5}-[0-9]{4}|[0-9]{2} [0-9]{4,5}-[0-9]{4}|9 [0-9]{4,5}-[0-9]{4}|9-[0-9]{4,5}-[0-9]{4}|9.[0-9]{4,5}-[0-9]{4}|[0-9]{2} 9 [0-9]{4,5}-[0-9]{4}|[0-9]{2} 9-[0-9]{4,5}-[0-9]{4}|[0-9]{2} 9.[0-9]{4,5}-[0-9]{4}", i)
        telefones_page = list(filter(starts_with_0_or_1, telefones_page))   
        for m in telefones_page:
            print(m)
        print(f'Números: {len(telefones_page)}')
        telefones.append(telefones_page)
        print('----------')
        page += 1

    file.close()