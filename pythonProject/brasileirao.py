times=('Sao Paulo','Corinthians','Palmeiras','Santos','Flamengo', 'Chapecoense','Fluminense',
       'Gremio','Internacional')

print(times)
print(f"Tres primeiros colocados sao {times[0:3]}")
print(f"Times em ordem alfabetica {sorted(times)}")
print(f"O Chapecoense está na posicao {times.index('Chapecoense')+1} posicao")
for k, valor in enumerate(times):
    print(f"{k+1} - {valor}")