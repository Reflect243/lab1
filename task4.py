# Задача 
# 
 
def f():
    pass

inputFile = open("input.txt", "r")

testCount = int(inputFile.readline())

inputFile.readline()
 
for i in range(testCount):
    print ("Тест {}:".format(i + 1))

    
    
    print("--------------------------------------------------")

    inputFile.readline()

inputFile.close()