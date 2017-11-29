class carsales():
    def __init__(self,model,year,price,kiometer):
        self.model = model
        self.year = year
        self.price = price
        self.kilometer = kiometer\




honda = carsales('City',2014,500000,10000)
Suzuki = carsales('swift',2012,200000,8000)
Mitsubishi = carsales('lancer',2010,150000,10000)

print(honda.__dict__)
print(Suzuki.__dict__)
print(Mitsubishi.__dict__)

buyer = ""
Choice = input('Enter')


if honda:
        print('The original amount is',honda.price)
        print('Your discount amount is:',honda.price-10000)
        print(buyer)

elif Suzuki:
        print('Your discount amount is:',Suzuki.price-8000)
        print(buyer)
elif Mitsubishi:
        print('Your discount amount is:',Mitsubishi.price-6500)
        print(buyer)
else:
        print('Thanks For coming')





