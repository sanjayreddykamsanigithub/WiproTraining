from oopsconcept.agecalc import AgeCalculation
from oopsconcept.myexception import AgeException

age = int(input('Age: '))
aobj = AgeCalculation()
try:
    aobj.voting_age_check(age)
    aobj.pension_age_check(age)

except AgeException as ae:
    print(ae)
else:
    print('Eligible. Contact next step...')

