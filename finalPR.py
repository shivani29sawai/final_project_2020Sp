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
# print(merge1.count())

merge2 = pd.merge(merge1, dfnew3, left_on='NAME', right_on='Unnamed: 0', how='inner')
#print(merge2.count())
# print(merge2)

finaldf = merge2.iloc[:, [0, 1, 2, 4, 7, 8, 9, 10, 11, 12, 13]]
#print(finaldf.count())
#print(finaldf.head())

# writer = pd.ExcelWriter('output2.xlsx')
# finaldf.to_excel(writer)
# writer.save()




def ppp(finaldf):
    global public
    global privateP
    global privateNP
    public = finaldf[finaldf['control'] == 'Public']
    #print(public.count())
    p1 = public['Emp_Rate'].mean()

    privateP = finaldf[finaldf['control'] == 'Private for-profit']
    #print(privateP.count())
    p2 = privateP['Emp_Rate'].mean()

    privateNP = finaldf[finaldf['control'] == 'Private not-for-profit']
    #print(privateNP.count())
    p3 = privateNP['Emp_Rate'].mean()
    return public, privateP, privateNP


def emp_rate(public, privateP, privateNP):
    p1 = public['Emp_Rate'].mean()
    p2 = privateP['Emp_Rate'].mean()
    p3 = privateNP['Emp_Rate'].mean()
    names = ('Public', 'Private for profit', 'Private for non profit')
    values = (p1, p2, p3)

    plt.bar(names, values)
    plt.ylabel('Employement Rate')
    plt.xlabel('Sector of University')
    plt.show()
    return 0



 # Hypothesis1
# emp_rate
finaldf = finaldf.astype({'TOT_ENROLL': float, 'TOT_EMP': float})
a = []
for line in finaldf:
    a = ((100 / finaldf['TOT_ENROLL']) * finaldf['TOT_EMP'])
    # print(a)
# print(len(a))
finaldf.insert(3, "Emp_Rate", a)
# print(finaldf.head())
ppp(finaldf)
emp_rate(public, privateNP, privateP)






#Hypothesis3
# finaldf = finaldf.astype({'F.Undergrad': float, 'P.Undergrad': float})
#
# result = finaldf['F.Undergrad'] > finaldf['P.Undergrad']

#print(bool.count('True'))
# plt.pie(result)
# plt.show()


def accpt_rate(public, privateP, privateNP):
    p1 = public['Accept_Rate'].mean()
    p2 = privateP['Accept_Rate'].mean()
    p3 = privateNP['Accept_Rate'].mean()
    names = ('Public', 'Private for profit', 'Private for non profit')
    values = (p1, p2, p3)

    plt.bar(names, values)
    plt.ylabel('Acceptace Rate')
    plt.xlabel('Sector of University')
    plt.show()
    return 0

#Hypothesis2
#print(finaldf.count())
b = []
for line in finaldf:
    b = (100/finaldf['Apps'])*finaldf['Accept']
finaldf.insert(10, 'Accept_Rate', b)
ppp(finaldf)
accpt_rate(public, privateP, privateNP)
