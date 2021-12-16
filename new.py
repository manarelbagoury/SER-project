from ser import train
import os.path
numOfModels = ""
num_models = 0
newline = "\n"
max = 0
index = 0
path = "C:\\Users\\user\\python\\uploads2"
num_files = len([f for f in os.listdir(path)if os.path.isfile(os.path.join(path, f))])
if num_files % 2 == 0:
    print("divisible by 100")
    file1 = open("MyFile.txt","r") 
    f1 = file1.read().splitlines()
    file1.close()
    numOfModels = f1[0]
    num_models = int(numOfModels)      
    print(num_models)
    accuracy =  [None] * (len(f1)-1);
    for f in range(num_models):
        accuracy[f] = f1[f+1]
    #num_models = num_models + 1
    #accuracy.append(train(num_models))
    print(accuracy)
    for f in range(num_models):
        if max < float(accuracy[f]):
            max = float(accuracy[f])
            index = f+1
    print(index)
    print(max)
    file1 = open("MyFile.txt","w")
    file1.write(str(num_models))
    file1.write(newline)
    for f in range(num_models):
        file1.write(str(accuracy[f]))
        file1.write(newline)
    file1.close()
    print("Done")