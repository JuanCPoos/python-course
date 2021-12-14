def isMayor(users):
    return users.edad > 17

class Usuario:

    def __init__(self, edad):
        self.edad = edad
        
users = Usuario(15)
usersTwo = Usuario(21)

result_1 = isMayor(users)
result_2 = isMayor(usersTwo)

print(result_1, ' ', result_2)