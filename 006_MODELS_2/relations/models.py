from django.db import models

# Create your models here.

class Account(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    # blank = True # Bos deger olabilir.
    # mull = True # Bir deger icermeyebilir.
    # unique = True # Ayni deger birden fazla yazilamaz.
    email = models.EmailField(blank=True, null=True)


    def __str__(self):
        return f"{self.username}"

class Profile(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    about = models.TextField(blank=True, null=True)


    def __str__(self):
        return f"{self.account} - {self.first_name} - {self.last_name}"
    

'''
on_delete properties:
    #! CASCADE -> if primary deleted, delete foreing too. Ana veri tabaninda ki veri silindiginde burada ki veriyi de sil demek.
    #! SET_NULL -> if primary deleted, set foreign to NULL. (null=True) Ana veri tabaninda ki veri silindiginde burada ki veriyi null yap. Bunu kullanmak icin null=True demek zorundayiz
    #! SET_DEFAULT -> if primary deleted, set foreing to DEFAULT value. (default='Value') Ana veri tabaninda ki veri silindiginde burada ki veriyi default yap. Bunu kullanmak icin default=0 gibi bir deger vermemiz gerekiyor.
    #! DO_NOTHING -> if primary deleted, do nothing. Ana veri tabaninda ki veri silindiginde burada ki veriye hicbirsey yapma.
    #! PROTECT -> if foreign is exist, can not delete primary.  Bir profil bilgisi varsa ana veri tabaninda ki veriyi silmeye izin verme demek.
'''


#! Many to One: ForeignKey()
class Address(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    country = models.CharField(max_length=50)
    phone = models.IntegerField(blank=True, null=True)


#! Many to Many:
class Product(models.Model):
    account = models.ManyToManyField(Account) #! Don't use on_delete; bir user'i sildigimizde onun ürünlerini silemeyiz cünkü bu ürünler diger kisilere de ait olabilirler. Veya tam terside olabilir; bir ürünü silince kullaniciyi silemeyiz cünkü o kullaniciya ait olan baska ürünler de olabilir. Deswegen many to many iliskide on_delete kullanilamaz.
    brand = models.CharField(max_length=50)
    product = models.CharField(max_length=120)


    def __str__(self):
        return f"{self.account} {self.brand} {self.product}"
    

    