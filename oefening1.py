flag = True

while flag:
    try:
        number1 = float(input("Wat is het eerste getal?"))
        number2 = float(input("Door welk getal wil je " + str(number1) + " delen?"))
        uitkomst = number1 / number2

        print("De uitkomst van " + str(number1) + " gedeeld door " + str(number2) + " is " + str(uitkomst))
        flag = False
    except ValueError:
        print("Je hebt geen geldig getal ingevoerd, probeer het nog een keer.")
        flag = True
    except ZeroDivisionError:
        print("Je kunt een getal niet door 0 delen, probeer het nog een keer met een ander getal.")
        flag = True
