palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
vogais = 'aeiou'
for c in palavras:
    print(f'\nNa palavra {c.upper()} temos', end=' ' )
    for p in list(c):
        if p in vogais:
            print(p, end = ' ')
