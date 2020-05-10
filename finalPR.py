import csv
import pandas as pd
import matplotlib.pyplot as plt


with open("C:/Users/ssawai2/Desktop/Final/Colleges_and_Universities.csv", encoding="utf8") as csvfile1:
    readCSV1 = csv.reader(csvfile1, delimiter=',')
    df1 = pd.read_csv(csvfile1, low_memory = False)
    dfnew1 = df1.iloc[:, [0, 7, 8]]
    dfnew1 = dfnew1.astype({'NAME': str})
    #'TOT_ENROLL': int, 'TOT_EMP': int, 'S.F.Ratio': float, 'Grad.Rate': float})
    #print(dfnew1.head())

with open("C:/Users/ssawai2/Desktop/Final/cc_institution_details.csv") as csvfile2:
    readCSV2 = csv.reader(csvfile2, delimiter=',')
    df2 = pd.read_csv(csvfile2)
    df2['chronname']=df2['chronname'].map(lambda x: x.upper())
    dfnew2 = df2.iloc[:, [1, 5, 12]]
    #print(dfnew2.head()

with open("C:/Users/ssawai2/Desktop/Final/College_Data.csv", encoding="utf8") as csvfile3:
    readCSV3 = csv.reader(csvfile3, delimiter=',')
    df3 = pd.read_csv(csvfile3, low_memory=False)
    df3['Unnamed: 0'] = df3['Unnamed: 0'].map(lambda x: x.upper())
    dfnew3 = df3.iloc[:, [0, 2, 3, 4, 7, 8, 15, 18]]
    #print(dfnew3.head())

merge1 = pd.merge(dfnew1, dfnew2, left_on='NAME', right_on='chronname', how='inner')

merge2 = pd.merge(merge1, dfnew3, left_on='NAME', right_on='Unnamed: 0', how='inner')

finaldf = merge2.iloc[:, [0, 1, 2, 4, 7, 8, 9, 10, 11, 12, 13]]


def sector_dataframes(finaldf):
    global public
    global privateP
    global privateNP
    public = finaldf[finaldf['control'] == 'Public']
    #print(public.count())

    privateP = finaldf[finaldf['control'] == 'Private for-profit']
    #print(privateP.count())

    privateNP = finaldf[finaldf['control'] == 'Private not-for-profit']
    #print(privateNP.count())
    return public, privateP, privateNP


def emp_rate(public, privateP, privateNP):
    p1 = public['Emp_Rate'].mean()
    p2 = privateP['Emp_Rate'].mean()
    p3 = privateNP['Emp_Rate'].mean()
    names = ('Public', 'Private for profit', 'Private for non profit')
    values = (p1, p2, p3)

    plt.bar(names, values, color = ['orange', 'red', 'yellow'])
    plt.ylabel('EMPLOYEMENT RATE')
    plt.xlabel('SECTOR OF UNIVERSITY')
    plt.show()
    return 0

def calc(df, col1, col2):
    global a
    a = []
    for line in df:
        a = (100/df[col1])*df[col2]
        return a

 # Hypothesis1
# emp_rate
finaldf = finaldf.astype({'TOT_ENROLL': float, 'TOT_EMP': float})

calc(finaldf, 'TOT_ENROLL', 'TOT_EMP')
finaldf.insert(3, 'Emp_Rate', a)
sector_dataframes(finaldf)
emp_rate(public, privateNP, privateP)


def accept_rate(public, privateP, privateNP):
    p1 = public['Accept_Rate'].mean()
    p2 = privateP['Accept_Rate'].mean()
    p3 = privateNP['Accept_Rate'].mean()
    names = ('Public', 'Private for profit', 'Private for non profit')
    values = (p1, p2, p3)

    plt.bar(names, values, color = ['navy', 'pink', 'purple'])
    plt.ylabel('ACCEPTANCE RATE')
    plt.xlabel('SECTOR OF UNIVERSITY')
    plt.show()
    return 0

#Hypothesis2
#print(finaldf.count())
calc(finaldf, 'Apps', 'Accept')
finaldf.insert(10, 'Accept_Rate', a)
sector_dataframes(finaldf)
accept_rate(public, privateP, privateNP)


#Hypothesis3
finaldf = finaldf.astype({'F.Undergrad': float, 'P.Undergrad': float})

result = finaldf['F.Undergrad'] > finaldf['P.Undergrad']


# plt.pie(result)
# plt.show()
