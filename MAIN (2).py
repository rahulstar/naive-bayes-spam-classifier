import csv
import create_training

def list_words(text):
    words=[]
    words_temp=text.lower().split()
    for p in words_temp:
        if p not in words and len(p)>3:
            words.append(p)
    return words

def training(texts):
    c_words={}  #freq of distinct words in each category
    c_categories={} #no of words in each category
    c_texts=0       #no of entries
    c_tot_words=0   #total words
    for t in texts:
        c_texts+=1
        if texts[t] not in c_categories:
            c_categories[texts[t]]=0
        c_categories[texts[t]]+=1
    for t in texts:
        words=list_words(t)
        for p in words:
            if p not in c_words:
                c_tot_words+=1
                c_words[p]={}
                for c in c_categories:
                    c_words[p][c]=0
            c_words[p][texts[t]]+=1
    #print c_texts
    return (c_words,c_categories,c_texts,c_tot_words)

def classifier(subject_line,c_words,c_categories,c_texts,c_tot_words):
    category=""
    category_prob=0
    for c in c_categories:
        prob_c=float(c_categories[c])/float(c_texts)
        words=list_words(subject_line)
        prob_total_c=prob_c
        for p in c_words:
            if p in words:
                prob_p=float(c_words[p][c])/float(c_tot_words)
                prob_cond=prob_p/prob_c
                prob=(prob_cond*prob_p)/prob_c
                prob_total_c=prob_total_c*prob
        if category_prob<prob_total_c:
            category=c
            category_prob=prob_total_c
    return (category,category_prob)

def calculate():
    with open("training.csv") as f:
        subjects=dict(csv.reader(f,delimiter=','))
    return training(subjects)

if __name__=="__main__":

    create_training.build_csv("testdata.csv","testspam","spam",100)
    create_training.build_csv("testdata.csv","testnospam","nospam",100)

    w,c,t,tw=calculate()
    with open("testdata.csv",'r') as f:
        count=0
        subjects=csv.reader(f)
        for i in subjects:
            clase=classifier(i[0],w,c,t,tw)
            if(clase[0]==i[1]):
                count+=1
            print clase[0],i[1],count    
        print("Efficiency : {} out of 200".format(count))
       ## total_efficiency=(count/200)*100
        ##print("total efficeincy:{}".format(total_efficiency))
    clase=classifier("internship oppurtunity",w,c,t,tw)
    print ("Result: {0} ".format(clase))
    
