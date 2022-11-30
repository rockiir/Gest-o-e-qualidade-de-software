class Peso_ideal:
    def __init__(self, nome, sexo, idade, peso, altura):
        self.nome = nome
        self.sexo = sexo
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def peso_crianca(self):
        if self.idade >= 3 and self.idade <= 10:
            p = (self.idade*2)+9
            print('O peso ideal é: ', '%.2f' % p)
        else:
            print('Não é possível calcular o peso ideal aproximado. [Idade abaixo de 3 anos]')

    def peso_adulto(self):
        if self.sexo == '':
            print('Não é possível calcular o peso ideal aproximado. [Sexo não informado.]')
        elif self.idade >= 18 and self.idade <= 64:
            if self.sexo == 'm':
                imc_h = '%.2f' % (22 * (self.altura**2))
                print('O peso ideal é: ', imc_h)
            elif self.sexo == 'f':
                imc_m = '%.2f' % (21 * (self.altura**2))
                print('O peso ideal é: ', imc_m)
        else:
            print('Não é possível calcular o peso ideal aproximado. [Faixa etária entre 11 e 17 anos]')

    def peso_idoso(self):
        if self.idade >= 65:
            if self.idade <= 69:
                if self.sexo == 'm':
                    print('O peso ideal é: ', '%.2f' %
                          (24.3 * (self.altura**2)))
                elif self.sexo == 'f':
                    print('O peso ideal é: ', '%.2f' %
                          (26.5 * (self.altura**2)))
            elif self.idade <= 74:
                if self.sexo == 'm':
                    print('O peso ideal é: ', '%.2f' %
                          (25.1 * (self.altura**2)))
                elif self.sexo == 'f':
                    print('O peso ideal é: ', '%.2f' %
                          (26.3 * (self.altura**2)))
            elif self.idade <= 79:
                if self.sexo == 'm':
                    print('O peso ideal é: ', '%.2f' %
                          (23.9 * (self.altura**2)))
                elif self.sexo == 'f':
                    print('O peso ideal é: ', '%.2f' %
                          (26.1 * (self.altura**2)))
            elif self.idade <= 84:
                if self.sexo == 'm':
                    print('O peso ideal é: ', '%.2f' %
                          (23.7 * (self.altura**2)))
                elif self.sexo == 'f':
                    print('O peso ideal é: ', '%.2f' %
                          (25.5 * (self.altura**2)))
            else:
                if self.sexo == 'm':
                    print('O peso ideal é: ', '%.2f' %
                          (23.7 * (self.altura**2)))
                elif self.sexo == 'f':
                    print('O peso ideal é: ', '%.2f' %
                          (25.5 * (self.altura**2)))

    def imc(self):
        i = self.peso/(self.altura**2)
        print('Taxa de IMC: ', "%.2f" % i)
        if i < 20:
            print('Situação: Abaixo do peso')
        elif i <= 25:
            print('Situação: Peso Normal')
        elif i <= 30:
            print('Situação: Sobre Peso')
        elif i <= 40:
            print('Situação: Obeso')
        else:
            print('Situação: Obeso Mórbido')
            
    def x(self):
        print('INFORME UMA OPÇÃO:')
        print(f"[ 1 ] Fica a maior parte do tempo sentada e não pratica atividades físicas programadas.")
        print(f"[ 2 ] Dia-a-dia movimentado – dirige, cozinha, caminha até o ponto de ônibus, mas sem atividades físicas programadas OU dia-a-dia sedentário e exercícios físicos três vezes por semana, cerca de 30 minutos por dia.")
        print(f"[ 3 ] Dia-a-dia movimentado e atividades físicas três vezes por semana, cerca de 30 minutos por dia.")
        print(f"[ 4 ] De uma a duas horas e meia de atividades físicas diárias.")
        print(f"[ 5 ] Atividade física diária por mais de três horas.")
        op = int(input('Informe um opção: '))
        if self.idade < 10:
            print('Não é possível calcular Necessidade diária de energia [idade abaixo de 10 anos]')
        elif op == 2 or op == 3 or op == 4 or op == 5 and self.sexo == '':
            print('Não é possível calcular Necessidade diária de energia [Sexo não informado]')
        # Mulheres
        elif self.sexo == 'f' and  op == 2:
            if self.idade >=10 and self.idade <=18:
                a1 = (12.2 * self.peso + 746)*1.3
                print("Necessidade diária de energia: ", '%.2f' % a1, 'cal')
            elif self.idade <=30:
                b1 = (14.7 * self.peso + 496)*1.3
                print("Necessidade diária de energia: ", '%.2f' % b1, 'cal')
            elif self.idade <=60:
                c1 = (8.7 * self.peso + 829)*1.3
                print("Necessidade diária de energia: ", '%.2f' % c1, 'cal')
            else:
                d1 = (10.5 * self.peso + 596)*1.3
                print("Necessidade diária de energia: ", '%.2f' % d1, 'cal')
        elif self.sexo == 'f' and  op == 3:
            if self.idade >=10 and self.idade <=18:
                a1 = (12.2 * self.peso + 746)*1.45
                print("Necessidade diária de energia: ", '%.2f' % a1, 'cal')
            elif self.idade <=30:
                b1 = (14.7 * self.peso + 496)*1.45
                print("Necessidade diária de energia: ", '%.2f' % b1, 'cal')
            elif self.idade <=60:
                c1 = (8.7 * self.peso + 829)*1.45
                print("Necessidade diária de energia: ", '%.2f' % c1, 'cal')
            else:
                d1 = (10.5 * self.peso + 596)*1.45
                print("Necessidade diária de energia: ", '%.2f' % d1, 'cal')
        elif self.sexo == 'f' and  op == 4:
            if self.idade >=10 and self.idade <=18:
                a1 = (12.2 * self.peso + 746)*1.5
                print("Necessidade diária de energia: ", '%.2f' % a1, 'cal')
            elif self.idade <=30:
                b1 = (14.7 * self.peso + 496)*1.5
                print("Necessidade diária de energia: ", '%.2f' % b1, 'cal')
            elif self.idade <=60:
                c1 = (8.7 * self.peso + 829)*1.5
                print("Necessidade diária de energia: ", '%.2f' % c1, 'cal')
            else:
                d1 = (10.5 * self.peso + 596)*1.5
                print("Necessidade diária de energia: ", '%.2f' % d1, 'cal')
        elif self.sexo == 'f' and  op == 5:
            if self.idade >=10 and self.idade <=18:
                a1 = (12.2 * self.peso + 746)*1.7
                print("Necessidade diária de energia: ", '%.2f' % a1, 'cal')
            elif self.idade <=30:
                b1 = (14.7 * self.peso + 496)*1.7
                print("Necessidade diária de energia: ", '%.2f' % b1, 'cal')
            elif self.idade <=60:
                c1 = (8.7 * self.peso + 829)*1.7
                print("Necessidade diária de energia: ", '%.2f' % c1, 'cal')
            else:
                d1 = (10.5 * self.peso + 596)*1.7
                print("Necessidade diária de energia: ", '%.2f' % d1, 'cal')
        # Homens
        elif self.sexo == 'm' and  op == 2:
            if self.idade >=10 and self.idade <=18:
                a1 = (17.5 * self.peso + 651)*1.4
                print("Necessidade diária de energia: ", '%.2f' % a1, 'cal')
            elif self.idade <=30:
                b1 = (15.3 * self.peso + 679)*1.4
                print("Necessidade diária de energia: ", '%.2f' % b1, 'cal')
            elif self.idade <=60:
                c1 = (8.7 * self.peso + 879)*1.4
                print("Necessidade diária de energia: ", '%.2f' % c1, 'cal')
            else:
                d1 = (13.5 * self.peso + 487)*1.4
                print("Necessidade diária de energia: ", '%.2f' % d1, 'cal')
        elif self.sexo == 'm' and  op == 3:
            if self.idade >=10 and self.idade <=18:
                a1 = (17.5 * self.peso + 651)*1.5
                print("Necessidade diária de energia: ", '%.2f' % a1, 'cal')
            elif self.idade <=30:
                b1 = (15.3 * self.peso + 679)*1.5
                print("Necessidade diária de energia: ", '%.2f' % b1, 'cal')
            elif self.idade <=60:
                c1 = (8.7 * self.peso + 879)*1.5
                print("Necessidade diária de energia: ", '%.2f' % c1, 'cal')
            else:
                d1 = (13.5 * self.peso + 487)*1.5
                print("Necessidade diária de energia: ", '%.2f' % d1, 'cal')
        elif self.sexo == 'm' and  op == 4:
            if self.idade >=10 and self.idade <=18:
                a1 = (17.5 * self.peso + 651)*1.6
                print("Necessidade diária de energia: ", '%.2f' % a1, 'cal')
            elif self.idade <=30:
                b1 = (15.3 * self.peso + 679)*1.6
                print("Necessidade diária de energia: ", '%.2f' % b1, 'cal')
            elif self.idade <=60:
                c1 = (8.7 * self.peso + 879)*1.6
                print("Necessidade diária de energia: ", '%.2f' % c1, 'cal')
            else:
                d1 = (13.5 * self.peso + 487)*1.6
                print("Necessidade diária de energia: ", '%.2f' % d1, 'cal')
        elif self.sexo == 'm' and  op == 2:
            if self.idade >=10 and self.idade <=18:
                a1 = (17.5 * self.peso + 651)*1.8
                print("Necessidade diária de energia: ", '%.2f' % a1, 'cal')
            elif self.idade <=30:
                b1 = (15.3 * self.peso + 679)*1.8
                print("Necessidade diária de energia: ", '%.2f' % b1, 'cal')
            elif self.idade <=60:
                c1 = (8.7 * self.peso + 879)*1.8
                print("Necessidade diária de energia: ", '%.2f' % c1, 'cal')
            else:
                d1 = (13.5 * self.peso + 487)*1.8
                print("Necessidade diária de energia: ", '%.2f' % d1, 'cal')
        
        elif self.sexo == 'm' or self.sexo == 'f' or self.sexo == '' and  op == 1:
            if self.idade >=10 and self.idade <=18:
                a1 = (17.5 * self.peso + 651)*1.2
                print("Necessidade diária de energia: ", '%.2f' % a1, 'cal')
            elif self.idade <=30:
                b1 = (15.3 * self.peso + 679)*1.2
                print("Necessidade diária de energia: ", '%.2f' % b1, 'cal')
            elif self.idade <=60:
                c1 = (8.7 * self.peso + 879)*1.2
                print("Necessidade diária de energia: ", '%.2f' % c1, 'cal')
            else:
                d1 = (13.5 * self.peso + 487)*1.2
                print("Necessidade diária de energia: ", '%.2f' % d1, 'cal')



while True:
    p1 = Peso_ideal(input('Informe seu nome: '), str(input('Informe o sexo - [f/m]: ')), int(input(
        'Informe sua idade: ')), float(input('Informe seu peso: ')), float(input('Informe sua altura: ')))
    p1.x()
    print(f'Nome: {p1.nome} - Sexo({p1.sexo.upper()}) \nIdade: {p1.idade} \nPeso atual: {(p1.peso)} kg \nAltura: {p1.altura} ')
    if p1.idade <= 10:
        p1.peso_crianca()
    elif p1.idade <= 64:
        p1.peso_adulto()
    else:
        p1.peso_idoso()
        if p1.sexo == '':
            print('Não é possível calcular o peso ideal aproximado. [Sexo não informado.]')
    p1.imc()
    sai = str(input('Deseja continuar[S/N]? ').lower())
    if sai in 'n':
        print("Finalizando...")
        print("=-==-=-==-=-==-=-==-=-==-=-==-=")
        print('FIM DO PROGRAMA!!!')
        break




