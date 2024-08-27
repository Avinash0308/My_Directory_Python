letter = "Hey my name is {1} and i am very rich and {0}"
country = "India"
name = "Avinash Agrawal"

print(letter.format(country,name))
print(f"Hey my name is {{name}} && I am from {{country}}")
print(f"Hey my name is {name} && I am from {country}")

price = 49.9999
print(f"the cost is {price: .2f}")
print(type(f"print {2*30}"))