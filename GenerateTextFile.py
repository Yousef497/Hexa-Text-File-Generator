import random
import time
import math

hexa = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]

name = input("Please input the Generated File Name: ")
numOfChar = int((float(input("Please input size of generated hexa text file in GB: ")) * pow(2, 30)))
#print(numOfChar)

start = time.process_time()
with open(name, 'w') as file:
    # i is counter for num of characters start from zero to end
    for i in range(0, numOfChar):
        val = random.randint(0, 15)
        file.write(hexa[val])

print("The File is ready")   
print("Time taken is: " + str(time.process_time() - start))