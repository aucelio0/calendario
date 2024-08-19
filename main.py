# importação de biblioteca
import calendar

try:
    # usuario informa o ano
    ano = int(input('Informe o ano: '))

    # exibe o calendário do ano atual
    for mes in range(12):
        print(calendar.month(ano, mes + 1))
except:
    print('Não foi possível exibir calendário.')