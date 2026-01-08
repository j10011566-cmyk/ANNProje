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

**P(y=1) =  1 / (1 + e/*/*-x)**
