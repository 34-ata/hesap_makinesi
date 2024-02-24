# Hesap Makinesi

![icon](https://github.com/34-ata/hesap_makinesi/assets/111538106/194b8ca8-f638-40ae-871f-35769a63f282)
---
# Sadece bir hesap makinesi değil
Aslına bakılacak olur ise, bu sadece basit bir hesap makinesi oluşturmak için başlanılmış bir proje değil. Bu, C ile yazılan fonksiyonları kütüphane mantığı ile Python'da hazırlanmış bir kullanıcı arayüzü programında nasıl kullanılabileceğini ele alıyor.
# Kütüphaneyi derleme
C ile yazdığımız fonksiyonları kullanabilmek için doğru bir şekilde derleyip ortaya bir ".so" dosyası çıkarmamız ve bu dosyayı Python'daki ctypes kütüphanesini kullanarak projemize dahil etmemiz gerekiyor.
'gcc -c hesap.c -fPIC'
'gcc -shared hesap.o -o hesap.so'
