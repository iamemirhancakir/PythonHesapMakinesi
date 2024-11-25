# Python Hesap Makinesi

Bu proje, **Python** kullanılarak geliştirilmiş kapsamlı bir hesap makinesi uygulamasıdır. Temel matematik işlemlerinden bilimsel hesaplamalara, birim dönüştürmelerden fonksiyon grafiklerine kadar geniş bir özellik yelpazesi sunar.

## Özellikler
- **Temel Hesaplama**:
  - Toplama, çıkarma, çarpma, bölme.
  
- **Bilimsel Hesaplama**:
  - Sinüs, kosinüs, tanjant, logaritma, faktöriyel ve karekök hesaplama.
  - Matematiksel fonksiyonların grafiğini çizme.
  
- **Birim Dönüştürme**:
  - Kilometre ↔ Mil
  - Celsius ↔ Fahrenheit
  - Kilogram ↔ Pound
  - Litre ↔ Galon
  - Santimetre ↔ İnç
  
- **Matris İşlemleri** *(Yeni Eklenen Özellik)*:  
  - Matris Toplama  
  - Matris Çarpma  
  - Determinant Hesaplama  
  - Matris Transpozu

## Kurulum

1. Bu projeyi klonlayın:
   ```bash
   git clone https://github.com/iamemirhancakir/PythonHesapMakinesi.git

2. Gerekli kütüphaneleri yükleyin
   ```bash
   pip install -r requirements.txt
   pip install matplotlib
   pip install numpy

 ## Kullanım
 1. Proje dizinine gidin
  ```bash
  cd hesapmakinesi
  python main.py
```
2. Menü üzerinden istediğiniz işlemi seçin:
- Temel Hesaplama
- Bilimsel Hesaplama
- Birim Dönüştürme
- Matris Hesaplama

 ## Proje Yapısı
  ```plaintext
hesapmakinesi/
├── main.py                   # Ana uygulama dosyası
├── calculator.py             # Temel hesaplama sınıfı
├── scientific_calculator.py  # Bilimsel hesaplama sınıfı
├── converter.py              # Birim dönüştürme sınıfı
├── matrixcalculator.py       # Matrix hesaplama sınıfı
├── requirements.txt          # Gerekli kütüphaneler
└── README.md                 # Proje açıklaması
```
## Örnek Kullanım

### Temel Hesaplama
  ```plaintext
Ana Menü
1. Temel Hesaplama
2. Bilimsel Hesaplama
3. Birim Dönüştürme
4. Matris Hesaplama
0. Çıkış
Bir mod seçin (0-4): 1

Birinci sayıyı girin: 10
İkinci sayıyı girin: 5
İşlem türü seçin (+, -, *, /): +
Sonuç: 15.0
```

### Grafik Çizimi
- Bilimsel hesaplama menüsünde bir fonksiyon seçildiğinde, matplotlib kullanılarak grafiği çizilir.

### Birim Dönüştürme
  ```plaintext
Birim Dönüştürücü
1. Kilometre -> Mil
2. Mil -> Kilometre
Bir dönüşüm seçin (0-10): 1
Kilometre girin: 5
Sonuç: 3.11 mil
```

### Örnek Matris İşlemi 
  ```
Matris satır sayısını girin: 2
Matris sütun sayısını girin: 2
Birinci matris değerlerini girin (satır satır):
1 2
3 4
İkinci matris değerlerini girin (satır satır):
1 2
3 4
Matrix 1: [[1. 2.]
 [3. 4.]]
Matrix 2: [[1. 2.]
 [3. 4.]]
Toplama sonucu:
[[2. 4.]
 [6. 8.]]
```

## Katkıda Bulunma
1. Bu projeyi forklayın.
2. Yeni bir dal (branch) oluşturun
  ```bash
  git checkout -b yeni-ozellik
```
3. Değişikliklerinizi yapın ve commit edin
  ```bash
  git commit -m "Yeni özellik eklendi"
```
4. Dalınızı push edin
  ```bash
  git push origin yeni-ozellik
```
5. Pull Request oluşturun

👨‍💻 Emirhan Çakır
Bu proje, Python becerilerinizi geliştirmek ve kullanışlı bir araç sunmak için tasarlandı. Keyifli kodlamalar! 😊

  



