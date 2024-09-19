# Şevval Topkan topkansevval@gmail.com

# Pusula Talent Academy - Veri Bilimi Görevi


## Proje Açıklaması
Bu proje, ilaç yan etkileriyle ilgili bir veri setini analiz etmek, eksik verileri doldurmak, kategorik verileri kodlamak ve modelleme için veriyi standardize etmek amacıyla yapılmıştır. Proje boyunca veri yükleme, veri ön işleme, veri görselleştirme ve veriyi modellemeye uygun hale getirme adımları gerçekleştirilmiştir.

## Proje Yapısı
Proje, modüler bir yapı ile geliştirilmiştir. Her bir veri işleme adımı ayrı dosyalar halinde organize edilmiştir.

main.py: Veri işleme pipeline'ını başlatan ana program dosyasıdır.
src/data_loading.py: Verinin yüklenmesi ve eksik verilerin doldurulması işlemlerini içerir.
src/preprocessing.py: Kategorik verilerin kodlanması ve verilerin standardize edilmesini sağlar.
src/visualization.py: Verilerin farklı grafiklerle görselleştirilmesi için kullanılır.
requirements.txt: Projede kullanılan tüm Python kütüphanelerini içerir.


## Adım Adım Kurulum ve Çalıştırma

### 1. Gerekli Python Kütüphanelerinin Yüklenmesi
Proje için gerekli olan Python kütüphanelerini yüklemek için `requirements.txt` dosyasını kullanabilirsiniz.

```bash
pip install -r requirements.txt
```

### 2. Projenin Çalıştırılması
Ana program dosyasını çalıştırarak veri işleme sürecini başlatabilirsiniz. Bu dosya, tüm veri işleme adımlarını sırasıyla gerçekleştirecektir.

```bash
python main.py
```

### 3. Veri İşleme Adımları
Proje boyunca şu adımlar gerçekleştirilir:

Veri Yükleme: Excel formatındaki veri seti data_loading.py dosyasıyla yüklenir.
Eksik Veri Doldurma: Sayısal sütunlar için ortalama, kategorik sütunlar için en sık görülen değer ile eksik veriler doldurulur.
Kategorik Veri Kodlama: Kategorik veriler OneHotEncoder kullanılarak kodlanır.
Veri Standardizasyonu: Sayısal sütunlar (kilo ve boy) StandardScaler kullanılarak standardize edilir.
Veri Görselleştirme: Cinsiyet dağılımı, ilaç adı dağılımı, korelasyon ısı haritası ve scatter plot grafiklerini içerir.


### 4. Kullanılan Kütüphaneler
Bu projede kullanılan temel Python kütüphaneleri şunlardır:

pandas: Veri yükleme ve veri manipülasyonu.
scikit-learn: Eksik veri doldurma, kategorik veri kodlama ve standardizasyon işlemleri.
matplotlib: Verilerin görselleştirilmesi.
seaborn: Grafiksel analizler ve korelasyon ısı haritası.

### 5. Proje İçeriği
Projenin her adımında veri ön işleme ve veri analizi gerçekleştirilmiştir:

Keşifsel Veri Analizi (EDA): Verilerin yapısını anlamak ve dağılımlarını incelemek için grafikler oluşturulmuştur.
Eksik Veri Doldurma: Verilerin eksik değerleri ortalama ve en sık kullanılan değerlerle doldurulmuştur.
Veri Ön İşleme: Kategorik veriler OneHotEncoder ile kodlanmış ve sayısal veriler standardize edilmiştir.
Görselleştirme: Cinsiyet dağılımı, ilaç adı dağılımı, kilo-boy scatter plot ve korelasyon ısı haritası grafiklerle gösterilmiştir.