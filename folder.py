import os 
for i in range(1000):
	path=os.path.join("./",f"{i}-Folder")
	os.mkdir(path)
print("Finished")
