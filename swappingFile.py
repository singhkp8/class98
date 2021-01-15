def SwapFileData():
    fileOneData     =   input("Enter your file name :  ")
    fileTwoData     =   input("Enter your file name :  ")
    with open(fileOneData,'r') as sampleA:
        sampleA    =   sampleA.read()

    with open(fileTwoData, 'r') as sampleB:
        sampleB = sampleB.read()
    print("Before changing data")
    print(sampleA)
    print(sampleB)

    with open(fileTwoData, 'w') as sampleB:
        sampleB.write(sampleA)
    
    with open(fileOneData, 'w') as sampleA:
        sampleA.write(sampleB)

    print("After changing data")
    print(sampleA)  
    print(sampleB)
      
SwapFileData()