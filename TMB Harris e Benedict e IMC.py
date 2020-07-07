## Creation of the patient
class patient (object):
    def __init__ (self, sex, weight, height, age):
        self.sex = sex.lower ()
        self.weight = weight
        self.height = height
        self.age = age

    ## Function to calculate by Harris and Benedict formula for the patient
    def hb (self):
        if sex == 'm':
            hb = (((((10*self.weight)+(6.25*(self.height*100))-(5*self.age)+5)*af)*fi)*tf)
        else:
            hb = (((((10*self.weight)+ (6.25*(self.height*100))-(5*self.age)-161)*fa)*fi)*ft)
        return hb

    ## BMI calculation
    def bmi (self):
        bmi = self.weight / (self.height * self.height)
        return bmi

    ## BMI classification
    def class_bmi (self):
        bmi_value = self.weight / (self.height * self.height)
        if self.sex == 'm':
            if bmi_value <20.7:
                return "Underweight"
            elif bmi_value>= 20.7 and bmi_value <26.4:
                return "Normal weight"
            elif bmi_value>= 26.4 and bmi_value <27.8:
                return "Marginally overweight"
            elif bmi_value>= 27.8 and bmi_value <31.1:
                return "Above ideal weight"
            elif bmi_value>= 31.1:
                return "Obesity"
            else:
                return 'error'

            
        if self.sex == 'f':
            if imc_value <19.1:
                return "Underweight"
            elif bmi_value >= 19.1 and bmi_value <25.8:
                return "Normal weight"
            elif bmi_value >= 25.8 and bmi_value <27.3:
                return "Marginally overweight"
            elif bmi_value >= 27.3 and bmi_value <32.3:
                return "Above ideal weight"
            elif bmi_value >= 32.3:
                return "Obesity"
            else:
                return 'error'




## Entering and validation of the variables
valid_sex = False
while valid_sex == False:
    sex = str (input ('Enter gender:') .lower ())
    if sex != 'm' and sex != 'f':
        print ('Use M for male and F for female')
    else:
        valid_sex = True

valid_weight = False
while valid_weight == False:
    weight = input ('Enter weight:')
    try:
        weight = float (weight)
        if weight <0:
            print ('Weight cannot be negative')
        else:
            valid_weight = True
    except:
        print ('Use only numbers and separate decimals with a period')

valid_height = False
while valid_height == False:
    height = input ('Enter stature:')
    try:
       height = float (height)
       if height <0:
           print ('Stature cannot be negative')
       else:
            valid_height= True
    except:
        print ('Use only numbers and separate decimals with a period')

validity = False
while validity == False:
    age = input ('Enter age:')
    try:
        age = int (age)
        if age <0:
            print ('Age cannot be negative')
        else:
            validity = True
    except:
        print ('Use only numbers')


valid_af = False
while valid_af == False:
    af = input ('Enter the activity factor:')
    try:
        af = float (af)
        if af <0:
            print ('Activity factor cannot be negative')
        else:
            valid_af = True
    except:
        print ('Use only numbers and separate decimals with a period')

    
valid_fi = False
while valid_fi == False:
    fi = input ('Enter the injury factor:')
    try:
        fi = float (fi)
        if fi <0:
            print ('The injury factor cannot be negative')
        else:
            valid_fi = True
    except:
        print ('Use only numbers and separate decimals with a period')


valid_tf = False
while valid_tf == False:
    tf = input ('Enter the thermal factor:')
    try:
        tf = float (tf)
        if tf <0:
            print ('The thermal factor cannot be negative')
        else:
            valid_tf = True
    except:
        print ('Use only numbers and separate decimals with a period')


## Creating the patient
patient = patient (sex, weight, height, age)

## Creating variables with the functions values
tee = round (patient.hb (), 2)
bmi = round (patient.bmi (), 2)
class_bmi = patient.class_bmi ()

## Final print
print (str (tee) + ' kcal/day')
print (str (bmi) + ' kg/m²')
print ('BMI classification: ' + str (class_bmi))
