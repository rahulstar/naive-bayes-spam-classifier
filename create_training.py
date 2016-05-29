import os

def build_csv(file_name,directory,category,tot_files):
    files=os.listdir(directory)
    count=0
    with open(file_name,'a') as f:
        for fname in files:
            count+=1
            path=os.path.join(directory,fname)
            with open(path,'r') as file:
                for line in file:
                    if(line.startswith("Subject:")): 
                       line=line.replace(",","")
                       f.write("{0},{1} \n".format(line[8:-1],category))
                       break
            if(count==tot_files):
                return

build_csv("training.csv","spam","spam",100)
build_csv("training.csv","nospam","nospam",100)
