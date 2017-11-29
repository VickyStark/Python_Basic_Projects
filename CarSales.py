class carsales():
    def __init__(self,model,year,price,kiometer):
        self.model = model
        self.year = year
        self.price = price
        self.kilometer = kiometer\




honda = carsales('City',2014,500000,10000)
suzuki = carsales('swift',2012,200000,8000)
mitsubishi = carsales('lancer',2010,150000,10000)

print(honda.__dict__)
print(Suzuki.__dict__)
print(Mitsubishi.__dict__)


choice = input('Which car You want:')


if 'honda'==choice:
        print('The original amount is',honda.price)
        print('Your discount amount is:',honda.price-10000)


elif 'suzuki'==choice:
        print('Your discount amount is:',suzuki.price-8000)
        print
elif 'mitsubishi'==choice:
        print('Your discount amount is:',mitsubishi.price-6500)
        print
else:
        print('Thanks For coming')





