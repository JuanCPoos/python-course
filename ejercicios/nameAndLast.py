def addNameAndLastName(name, lastName):
    c = open('completeName.txt', 'a')
    c.write(name + ' ' + lastName)
    c.close()

addNameAndLastName('Juan', 'Poos')
