import pandas as pd
from sklearn.impute import SimpleImputer

#Veri Yükleme 
def load_data(file_path):
    df = pd.read_excel(file_path)
    return df


#Eksik Verilerin Doldurulması
def handle_missing_data(df):
    imputer_numeric = SimpleImputer(strategy='mean')
    df['Kilo'] = imputer_numeric.fit_transform(df[['Kilo']])
    df['Boy'] = imputer_numeric.fit_transform(df[['Boy']])
    
    imputer_categorical = SimpleImputer(strategy='most_frequent')
    df['Cinsiyet'] = imputer_categorical.fit_transform(df[['Cinsiyet']]).ravel()
    df['Il'] = imputer_categorical.fit_transform(df[['Il']]).ravel()
    df['Alerjilerim'] = imputer_categorical.fit_transform(df[['Alerjilerim']]).ravel()

    return df
