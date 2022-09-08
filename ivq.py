import regex as re
import csv
import pandas as pandasForSortingCSV

file = open("content1.txt","r")

def cleaning(text):
    text = re.sub(r'(?!(([^"]*"){2})*[^"]*$),', '', text)
    # text = re.sub(r'(?!(([^\{]*\}){2})*[^\{"]*$),', '', text)
    text = re.sub(r'\"', '', text)
    print(text)
    text = text.split(",")
    
    text = [string.lstrip() for string in text]
    return text

text = []

[text.append(cleaning(x.strip())) if x.rsplit() else "" for x in file]
    
try:
    with open('cleancontent2.csv','w') as f:
        writer = csv.writer(f)
        for i in range(0,len(text)):
            writer.writerow(text[i])
except IOError:
    print("Fail write to CSV")
    
try:
    df = pandasForSortingCSV.read_csv('cleancontent2.csv')
    df.sort_values(["Age"],ascending=[False], inplace=True)
    print(df)
except Exception as e:
    print("Something wrong in content1.txt file")
    
    