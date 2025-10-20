pesos=int(input("Enter the monet left in pesos: "))
soles=int(input("Enter the monry left in soles: "))
reais=int(input("Enter the mony left in reais: "))

total_in_USD=pesos*0.00026+soles*0.29+reais*0.18

print(f"The total amount left = ${total_in_USD:.2f} USD")