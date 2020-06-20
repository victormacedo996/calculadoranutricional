print ('calculadora de gasto energético basal em programação orientada por objeto')


class paciente (object):
    def __init__(self, nome, sexo, peso, estatura, idade):
        self.sexo = sexo.lower()
        self.peso = peso
        self.estatura = estatura
        self.idade = idade

        
    def hb (self):
        if sexo == 'm':
            hb =(10*self.peso)+(6.25*(self.estatura*100))-(5*self.idade)+5
        else:
            hb =(10*self.peso)+(6.25*(seld.estatura*100))-(5*self.idade)-161
        return hb

    
    def imc (self):
        imc = self.peso/(self.estatura*self.estatura)
        return imc


    def class_imc (self):
        valor_imc = self.peso/(self.estatura*self.estatura)
        if self.sexo=='m':
            if valor_imc < 20.7:
                return "Abaixo do peso"
            elif valor_imc >= 20.7 and valor_imc < 26.4:
                return "Peso normal"
            elif valor_imc >= 26.4 and valor_imc < 27.8:
                return "Marginalmente acima do peso"
            elif valor_imc >= 27.8 and valor_imc < 31.1:
                return "Acima do peso ideal"
            elif valor_imc >= 31.1:
                return "Obesidade"
            else:
                return 'erro'

            
        if self.sexo=='f':
            if valor_imc < 19.1:
                return "Abaixo do peso"
            elif valor_imc >= 19.1 and valor_imc < 25.8:
                return "Peso normal"
            elif valor_imc >= 25.8 and valor_imc < 27.3:
                return "Marginalmente acima do peso"
            elif valor_imc >= 27.3 and valor_imc < 32.3:
                return "Acima do peso ideal"
            elif valor_imc >= 32.3:
                return "Obesidade"
            else:
                return 'erro'



nome = input('Digite o nome: ')

valid_sexo = False
while valid_sexo == False:
    sexo = str(input('Digite o sexo: ').lower())
    if sexo != 'm' and sexo != 'f':
        print ('Use M para masculino e F para feminino')
    else:
        valid_sexo = True

valid_peso = False
while valid_peso == False:
    peso = input('Digite o peso: ')
    try:
        peso = float (peso)
        if peso < 0:
            print('O peso não pode ser negativo')
        else:
            valid_peso = True
    except:
        print('Use apenas numeros e separe decimais com ponto')

valid_estatura = False
while valid_estatura == False:
    estatura = input('Digite a estatura: ')
    try:
       estatura = float(estatura)
       if estatura < 0:
           print('A estatura não pode ser negativa')
       else:
            valid_estatura = True
    except:
        print('Use apenas numeros e separe decimais com ponto')

valid_idade = False
while valid_idade == False:
    idade = input('Digite a idade: ')
    try:
        idade = int(idade)
        if idade < 0:
            print('A idade não pode ser negativa')
        else:
            valid_idade = True
    except:
        print('Use apenas numeros')

a = paciente(nome, sexo, peso, estatura, idade)


print (a.hb())
print(a.imc())
print(a.class_imc())
