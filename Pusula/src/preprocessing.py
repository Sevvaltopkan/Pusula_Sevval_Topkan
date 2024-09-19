from sklearn.preprocessing import OneHotEncoder, StandardScaler
import pandas as pd


#Kategorik Verilerin Kodlanması (OneHotEncoder)
def encode_categorical_data(df):
    categorical_columns = ['Cinsiyet', 'Il', 'Ilac_Adi']
    encoder = OneHotEncoder(sparse_output=False, drop='first')
    encoded_categorical = encoder.fit_transform(df[categorical_columns])
    df_encoded = pd.DataFrame(encoded_categorical, columns=encoder.get_feature_names_out(categorical_columns))
    
    df = pd.concat([df, df_encoded], axis=1)
    df.drop(columns=categorical_columns, inplace=True)

    return df

#Standardizasyon işlemi
def standardize_data(df):
    numeric_columns = ['Kilo', 'Boy']
    scaler = StandardScaler()

    # Sayısal sütunları ölçeklendirme
    df[numeric_columns] = scaler.fit_transform(df[numeric_columns])
    return df
