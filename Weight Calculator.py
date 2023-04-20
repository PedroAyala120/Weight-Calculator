#This program will ask the user for the mass of an object
#and calculate the weight of that object
#Pedro Ayala

mass = int(input('Enter the object’s mass: '))   #Mass input

weight = mass * 9.8 #weight calculation

#Prints the weight of the object
print ('The weight of the object is: ', (format(weight, '.2f')), 'newtons')

#Determines if the object is too heavy or light
if weight > 500:
    print ('The object is too heavy')
elif weight < 100:
    print ('The object is too light')
else:   #Checks if the object is the right weight
    print ('The object is just right')
