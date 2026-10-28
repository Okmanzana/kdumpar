import random

caracters = ("+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")

longitud = int(input("introduzca el largo"))

contra = ""
for i in range (longitud):
    contra += random.choice(caracters)

print("tu contraseña es ", contra)
