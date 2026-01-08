# SİNİR AĞLARİ FİNAL ÖDEVİ TESLİMİ - TITANIC SURVIVAL PREDICTION

Projem Titanic veri seti kullanılarak yolcuların hayatta kalıp kalmadığını tahmin eden bir basit logistik regresyon modeli ve yapay sinir ağı (ANN) modeli içerir.

## Proje Amacı:
- Titanic yolcularına ait demografik ve sosyo-ekonomik verileri analiz etmek.
- Bir yolcunun hayatta kalma durumunu (Survived) tahmin eden bir model geliştirmek.
- Basit bir derin öğrenme (ANN) modeli geliştirmek.
- Logistic Regression ile karşılaştırma yapmak. 
- Eğitim grafikleri ve performans metriklerini yorumlamak.

## Proje Dosya Yapısı:
- Proje.py: Tüm kodların bulunduğu ana Python dosyası.
- README.md: Proje açıklaması.
- titanic.csv: Veri seti.
## Kullanılan Değişkenler:

| Değişken   | Açıklama                              |
|------------|--------------------------------------|
| Survived   | Hayatta kalma durumu (0 = Hayır, 1 = Evet) |
| Pclass     | Yolcu sınıfı                          |
| Sex        | Cinsiyet                              |
| Age        | Yaş                                   |
| SibSp      | Kardeş / Eş sayısı                    |
| Parch      | Ebeveyn / Çocuk sayısı                |
| Fare       | Bilet ücreti                          |
| Embarked   | Biniş limanı                          |

## Kullanılan Model ve Model Mimarileri:
**Logistic Regression:**

Logistic Regression da kullandım çünkü basit ve yorumlanabilir, ikili sınıflandırma problemleri için idealdir ve küçük veri setlerinde etkilidir ve Yapay Sinir Ağı(ANN) ile karşılaştırmanın iyi olacağını düşündüm.

Model aşağıdaki sigmoid fonksiyonunu kullanır:

$$
P(y = 1) = \frac{1}{1 + e^{-x}}
$$

## Yapay Sinir Ağı (ANN) Yapısı ve Hiperparametreler
## Ağ Mimarisi
- **Input layer:** Özellik sayısı kadar nöron  
- **Hidden layers:** 16 → 8 nöron, **ReLU** aktivasyon  
- **Output layer:** 1 nöron, **Sigmoid** aktivasyon  
## Hiperparametreler
- **Optimizer:** Adam  
- **Loss:** Binary Crossentropy  
- **Epoch:** 100  
- **Batch Size:** 16  
- **Validation Split:** 0.2

Nonlinear ilişkileri yakalayabilir ve özellikler arası karmaşık etkileşimleri öğrenebilir

## Kullandığım Kütüphaneler ve Sürümleri

- **matplotlib:** 3.10.8  
- **numpy:** 2.4.0  
- **pandas:** 2.3.3  
- **scikit-learn:** 1.8.0  
- **seaborn:** 0.13.2  
- **tensorflow:** 2.20.0

## Sonuçlar ve Yorumum
**Logistic Regression Test Accuracy:** 0.81  
  Bu sonuç, modelin test verisinin %81'ini doğru sınıflandırdığını gösterir. Titanic veri seti için oldukça başarılı bir sonuç.

**ANN Test Accuracy:** 0.788 (yaklaşık)  
  Logistic Regression’a göre biraz daha düşük performans göstermiştir.

