letter = '''Dear <|Name|> , 
            You are selected !
            <|Date|>'''

print(letter.replace("<|Name|>", "Manish" ).replace("<|Date|>", "20-sept-2026"))
