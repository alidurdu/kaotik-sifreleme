# Python ile Kaotik Sistemler Kullanarak Görüntü Şifreleme

Bu depo, kaotik sistemler kullanarak görsel verilerin nasıl şifreleneceğini gösteren basit bir Python uygulamasını içerir.

## İçerik

- `encrypt_image.py`: Görseli logistic map kullanarak şifreleyen Python kodu
- `example_image.jpg`: Örnek olarak kullanılacak bir görsel 
- `README.md`: Bu dosya

## Kullanım

```bash
python encrypt_image.py
```

Kod, `example_image.jpg` dosyasını okuyarak gri tonlamaya çevirir, logistic map ile bir anahtar üretir ve XOR işlemiyle şifreler. Sonuç olarak `encrypted_image.png` dosyasını üretir.

## Kaotik Sistem Notu

Bu örnekte kullanılan logistic map denklemi:

```
x[n+1] = r * x[n] * (1 - x[n])
```

Başlangıç değeri ve `r` parametresi farklılaştıkça şifreleme çıktısı tamamen değişir.


