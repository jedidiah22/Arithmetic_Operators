def themepark (height,age):
    height = float(input("Enter your height: "))
    age = int(input("Enter your age: "))

    if(height > 170):
        print('welcome')
    elif(age>17):
        print('welcome')
    else:
        print('you are not qualified')