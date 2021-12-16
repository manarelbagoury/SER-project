import pickle
count = 3
data = []
data2 = "123456"
data3 = "789101112"
data4 = "jjj"
pickle_out = open("dict.pickle","wb")
pickle.dump(data2, pickle_out)
pickle.dump(data3, pickle_out)
pickle.dump(data4, pickle_out)
pickle_out.close()
pickle_out = open("dict.pickle","rb")
for x in range(count):
    data.append(pickle.load(pickle_out))
print(data)
pickle_out.close()