import numpy as np
import pandas as pd
import argparse 

class TitanicCleaner:
    """
    Class for cleaning Titanic files
    """
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.load_data()

    def load_data(self) -> None:
        if self.filename.endswith('csv'):
            self.data = pd.read_csv(self.filename)
        else:
            print("Please provide a CSV file, other extension under development - parquet, excel, avro, feather, csv, pdf, e")
    
    def eda(self, number: int = 5) -> None:
        print(f"These are the columns: {self.data.columns}")
        print('---------------------------------')
        print(f"This is the head: {self.data.head(number)}")
        print(self.data.tail(number))
        print(self.data.describe(include='all'))
        print(self.data.groupby(['Pclass', 'Sex'])[['Embarked', 'Survived',]].value_counts())


    def clean(self) -> None:
        self.data.Age.fillna(0, inplace=True)
        self.data.Fare.fillna(1, inplace=True)
        self.data.Cabin.fillna("NA", inplace=True)
        self.data.drop_duplicates
        print("Data has been cleaned")


    def apply_trans(self) -> None:
        pass


if __name__=='__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--filename", required=True, help="filename with respect to its location", type=str)
    ap.add_argument("-n", "--number", required=False, help="number of rows in head/tail", type=int)
    args = ap.parse_args()
    cleaner = TitanicCleaner(args.filename)
    if args.number is None:
        cleaner.eda()
    else:
        cleaner.eda(args.number)
    # cleaner.clean()

