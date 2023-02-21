from itertools import *

counter = 0
for element in product('ВЕРОНИКА', repeat = 6):
    if element.count('Е') + element.count('О') + element.count('И') + element.count('А') > element.count('В') + element.count('Р') + element.count('Н') + element.count('К'):
        counter += 1
print(counter)