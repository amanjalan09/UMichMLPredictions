from model import cleaning
import pandas
import pickle

def main():

    data = [["College of Engineering (CoE)","Early Action / EA",1490.0,35.0,"Top 50%","2 and above","1-3","0","Male","South Asian","International","No","No","No","Yes","Yes","No","Yes","No",""]]

    head = cleaning(data)
    f = open("../model.pkl",'rb')
    model = pickle.load(f)
    print(model.predict(head))

if __name__ == "__main__":
    main()
