letter = '''Dear <|NAME|>,
You are selected!
Date: <|DATE|>'''

print(letter.replace("<|NAME|>","zayed").replace("<|DATE|>","20/10/2050"))