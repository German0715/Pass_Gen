import random 

# Este código es un generador de contraseñas aleatorio 

elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890";
print("Soy un programa que genera contraseñas") # Saludo normal 
pass_length = int(input("De cuantos caracteres quieres tu contraseña?: "))
password="";

for i in range(pass_length):
    password+=random.choice(elements)
    
print(password)


