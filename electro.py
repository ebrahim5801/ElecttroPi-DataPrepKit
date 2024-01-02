import pandas as pd

class ElectroPi:
    def ___init__(self):
        pass

    def read_csv(self, name):
        return pd.read_csv(name)

    def readExcel(filePath):
        return pd.read_excel(filePath)

    def readJson(filePath):
        return pd.read_json(filePath)

    def printInfo(df):
        return df.describe()

    def convertCatToNum(df):
        # Find categorical columns 
        categoricalColumns = df.select_dtypes(include=['object']).columns.tolist()
        return pd.get_dummies(df[categoricalColumns])  

    # option:
    # 1 = delete missing values
    # 2 = replace with value
    # Values example: {"first column name": first column value, "second column name": second column value, "third column name": third column value} 

    def handleMissingValues(df, option, values=None):
        if option == 1:
            return df.dropna(inplace=True, axis=1)
        elif option == 2:
            if values == None :
                raise ValueError("Values can't be empty")
            else:
                return df.fillna(value=values)
        else:
            raise ValueError('Option can be 1 or 2 only')

ElClass = ElectroPi()
df = ElClass.read_csv("Credit_card.csv")
df.head()