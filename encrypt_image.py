import cv2
import numpy as np

def logistic_map(x, r=3.99, size=256*256):
    seq = []
    for _ in range(size):
        x = r * x * (1 - x)
        seq.append(int(x * 255) % 256)
    return np.array(seq, dtype=np.uint8)

# Görseli oku ve gri tona çevir
img = cv2.imread('example_image.jpg', 0)  # Gri okuma
img = cv2.resize(img, (256, 256))
flat_img = img.flatten()

# Kaotik anahtar oluştur
key = logistic_map(x=0.678, size=flat_img.size)

# XOR işlemi ile şifreleme
encrypted = np.bitwise_xor(flat_img, key)
encrypted_img = encrypted.reshape(img.shape)

# Şifreli görseli kaydet
cv2.imwrite('encrypted_image.png', encrypted_img)
