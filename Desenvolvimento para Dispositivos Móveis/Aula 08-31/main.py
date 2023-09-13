if __name__ == '__main__':
    try:
        divisor = int(input("Type an integer number "))
        a = 4 / divisor
    except ZeroDivisionError:
        print("Division by zero not possible")
    except Exception as inst:
        print(type(inst).__name__)
    else:
        print("Result:", a)
