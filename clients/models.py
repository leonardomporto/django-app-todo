from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.text import slugify
import random
import string
from django.contrib.auth import get_user_model
from servers.models import Server



# class Server(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name




def random_string(length=4):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


class Client(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=255, verbose_name='Sobrenome')
    phone = PhoneNumberField()
    email = models.EmailField(max_length=254)
    nikname = models.CharField(max_length=255, verbose_name='Nome de Usuário')
    password = models.CharField(max_length=255, verbose_name='Senha')
    birthday = models.DateField(verbose_name="Birthday")
    date_payment = models.DateField()
    server = models.ForeignKey(Server, on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(unique=True)

    # for user manager #
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

    def save(self, *args, **kwargs):
        if not self.slug:
            # self.slug = slugify(self.name) + random_string()
            self.slug = f"{slugify(self.name)}-{slugify(self.lastname)}-{random_string()}"
        super(Client, self).save(*args, **kwargs)