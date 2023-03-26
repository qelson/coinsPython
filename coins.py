amount = int(input('Please enter your amount as an integer between 0 and 99: '))
quarterValue = 25
dimeValue = 10
nickelValue = 5
pennyValue = 1

quarters = amount // quarterValue
remainder = amount % quarterValue
dimes = remainder // dimeValue
remainder = remainder % dimeValue
nickels = remainder // nickelValue
remainder = remainder % nickelValue
pennies = remainder // pennyValue

print('Your change is:')
print(quarters, ' quarters')
print(dimes, ' dimes')
print(nickels, ' nickels')
print(pennies, ' pennies')