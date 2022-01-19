def run():
    weight =input("Enter your weight in kilograms: ")
    heigh = input("Enter your heigh in meters: ") 

    bmi = float(weight)/float(heigh)**2

    return print(round(bmi,2))

if __name__ == '__main__':
    run()