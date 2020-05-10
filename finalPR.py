import csv
import pandas as pd
import matplotlib.pyplot as plt

def open_file(a, b, c):
    """
    opens the data files and returns a final data frame to be used for analysis
    :param a: File 1.
    :param b: File 2.
    :param c: File 3.
    :return: Returns final data frame to analyse.
    """
    global finaldf
    with open(a, encoding="utf8") as csvfile1:
        readCSV1 = csv.reader(csvfile1, delimiter=',')
        df1 = pd.read_csv(csvfile1, low_memory = False)
        dfnew1 = df1.iloc[:, [0, 7, 8]]
        dfnew1 = dfnew1.astype({'NAME': str})
        #print(dfnew1.head())

    with open(b) as csvfile2:
        readCSV2 = csv.reader(csvfile2, delimiter=',')
        df2 = pd.read_csv(csvfile2)
        df2['chronname']=df2['chronname'].map(lambda x: x.upper())
        dfnew2 = df2.iloc[:, [1, 5, 12]]
        #print(dfnew2.head()

    with open(c, encoding="utf8") as csvfile3:
        readCSV3 = csv.reader(csvfile3, delimiter=',')
        df3 = pd.read_csv(csvfile3, low_memory=False)
        df3['Unnamed: 0'] = df3['Unnamed: 0'].map(lambda x: x.upper())
        dfnew3 = df3.iloc[:, [0, 2, 3, 4, 7, 8, 15, 18]]
        #print(dfnew3.head())

    merge1 = pd.merge(dfnew1, dfnew2, left_on='NAME', right_on='chronname', how='inner')

    merge2 = pd.merge(merge1, dfnew3, left_on='NAME', right_on='Unnamed: 0', how='inner')

    finaldf = merge2.iloc[:, [0, 1, 2, 4, 7, 8, 9, 10, 11, 12, 13]]
    return finaldf


def sector_dataframes(finaldf):
    """
    Returns 3 data frames divided according to sectors.
    :param finaldf: The data frame which needs to be divided in 3 sectors.
    :return public: Public sector data frame.
    :return privateP: Private for-profit sector data frame.
    :return privateNP: private for non-profit sector data frame.
    """
    global public
    global privateP
    global privateNP
    public = finaldf[finaldf['control'] == 'Public']

    privateP = finaldf[finaldf['control'] == 'Private for-profit']

    privateNP = finaldf[finaldf['control'] == 'Private not-for-profit']
    return public, privateP, privateNP


def calc(df, col1, col2):
    """
    Returns a list of column by performing calculations.
    :param df: The data frame whose columns are used for calculations.
    :param col1: First column used for calculation
    :param col2: Second column used for calculaion.
    :return new_col: List created by performing calculations on required columns.
    """
    global new_col
    new_col = []
    for line in df:
        new_col = (100/df[col1])*df[col2]
        return new_col


def calc_mean(df1, df2, df3, col1, col2, col3):
    """
    Calculats the mean of 3 inputs columns.
    :param df1: The first data frame whose column's mean is to be calculated.
    :param df2: The second data frame whose column's mean is to be calculated.
    :param df3: The third data frame whose column's mean is to be calculated.
    :param col1: Column from data frame 1.
    :param col2: Column from data frame 2.
    :param col3: Column from data frame 3.
    :return names: Returns a variable which has 3 names to be used for graph.
    :return values: Returns values of mean to be used in graph.
    """
    global names
    global values
    p1 = df1[col1].mean()
    p2 = df2[col2].mean()
    p3 = df3[col3].mean()
    names = ('Public', 'Private for profit', 'Private for non profit')
    values = (p1, p2, p3)
    return names, values

if '__name__' == '__main__':
    open_file("C:/Users/ssawai2/Desktop/Final/Colleges_and_Universities.csv","C:/Users/ssawai2/Desktop/Final/cc_institution_details.csv", "C:/Users/ssawai2/Desktop/Final/College_Data.csv")
    # Hypothesis1
    # emp_rate
    finaldf = finaldf.astype({'TOT_ENROLL': float, 'TOT_EMP': float})

    calc(finaldf, 'TOT_ENROLL', 'TOT_EMP')
    finaldf.insert(3, 'Emp_Rate', new_col)
    sector_dataframes(finaldf)
    calc_mean(public, privateNP, privateP, 'Emp_Rate', 'Emp_Rate', 'Emp_Rate')
    plt.bar(names, values, color = ['orange', 'red', 'yellow'])
    plt.ylabel('EMPLOYEMENT RATE')
    plt.xlabel('SECTOR OF UNIVERSITY')
    plt.show()


    #Hypothesis2
    #print(finaldf.count())
    calc(finaldf, 'Apps', 'Accept')
    finaldf.insert(10, 'Accept_Rate', new_col)
    sector_dataframes(finaldf)
    calc_mean(public, privateP, privateNP, 'Accept_Rate', 'Accept_Rate', 'Accept_Rate')
    plt.bar(names, values, color = ['navy', 'pink', 'purple'])
    plt.ylabel('ACCEPTANCE RATE')
    plt.xlabel('SECTOR OF UNIVERSITY')
    plt.show()


# #Hypothesis3
# finaldf = finaldf.astype({'F.Undergrad': float, 'P.Undergrad': float})
#
# result = finaldf['F.Undergrad'] > finaldf['P.Undergrad']
#
#
# # plt.pie(result)
# # plt.show()
