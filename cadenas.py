name = "fmoradev"
last_name = "Olea"
print(name)
print(last_name)

# concatenar
full_name = name + " " + last_name
print(full_name)

quote = "I'm fmoradev"
print(quote)
quote2 = 'She said "Hello"'
print(quote2)

# format
template = "Hola, mi nombre es " + name + " y mi apellido es " + last_name
print('v1 =', template)

template2 = "Hola, mi nombre es {} y mi apellido es {}".format(name, last_name)
print('v2 =', template2)

template3 = f"Hola, mi nombre es {name} y mi apellido es {last_name}"
print('v3 =', template3)