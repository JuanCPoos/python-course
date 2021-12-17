def addNameAndLastName(name, lastName):
    c = open('completeName_1.txt', 'a')
    c.write(name + ' ' + lastName + '\n')
    c.close()

addNameAndLastName('Juan', 'Perez')
