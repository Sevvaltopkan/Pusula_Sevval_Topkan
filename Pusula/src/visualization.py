import matplotlib.pyplot as plt
import seaborn as sns

#Cinsiyet Dağılımı Grafiği
def plot_gender_distribution(df):
    plt.figure(figsize=(6, 4))
    sns.countplot(x='Cinsiyet', data=df)
    plt.title('Cinsiyet Dağılımı')
    plt.show()

#İlaç Adı Dağılımı Grafiği
def plot_drug_distribution(df):
    plt.figure(figsize=(10, 8))
    sns.countplot(y='Ilac_Adi', data=df, order=df['Ilac_Adi'].value_counts().index)
    plt.title('İlaç Adı Dağılımı')

    #Grafik için Yazı Tipi ve Boyut Ayarları Yapılması
    plt.yticks(fontsize=8)
    plt.tight_layout()
    plt.show()

#orelasyon Isı Haritası
def plot_correlation_heatmap(df):
    numeric_columns = ['Kilo', 'Boy']
    corr_matrix = df[numeric_columns].corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Korelasyon Isı Haritası')
    plt.show()

#Scatter Plot (Kilo ve Boy Arasındaki İlişki)
def plot_scatter(df):
    plt.figure(figsize=(6, 4))
    sns.scatterplot(x='Kilo', y='Boy', data=df)
    plt.title('Kilo ve Boy Arasındaki İlişki')
    plt.show()

#Tüm Görselleştirme Fonksiyonlarının Sırayla Çalıştırılması
def visualize_data(df):
    plot_gender_distribution(df)
    plot_drug_distribution(df)
    plot_correlation_heatmap(df)
    plot_scatter(df)
