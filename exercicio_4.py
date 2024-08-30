faturamento = [67836.43, 36678.66, 29229.88, 27165.48, 19849.53]

faturamento_total = sum(faturamento)
print('faturamento total foi: ',faturamento_total)

sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

def percentual(estado):
    calculo = estado / faturamento_total * 100
    return int(calculo)

print('percentual de SP', percentual(sp),'%')
print('percentual de RJ', percentual(rj),'%')
print('percentual de MG', percentual(mg),'%')
print('percentual de ES', percentual(es),'%')
print('percentual de Outros', percentual(outros),'%')