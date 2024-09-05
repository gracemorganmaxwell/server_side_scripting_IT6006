from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User



# Create your models here.
class SupermarketChain(models.Model):
    NEW_WORLD = 'Nw'
    COUNTDOWN = 'Cd'
    PAK_N_SAVE = 'Ps'
    FRESH_CHOICE = 'Fc'
    super_market_chain = [
        (NEW_WORLD , 'New World'),
        (COUNTDOWN , 'Coutn down'),
        (PAK_N_SAVE , 'Pak n Save'),
        (FRESH_CHOICE , 'Fresh Choice'),
    ]
   
    #id is autmatically generated by Django.
    chain_id = models.AutoField(primary_key=True)
    chain_name = models.CharField(
        max_length = 2,
        choices = super_market_chain,
        default = COUNTDOWN,
    )


    def __str__(self) -> str:
        return self.chain_name
    def get_absolute_url(self):
        return reverse ("chain_detail", kwargs= {"chain_id": self.pk})

class Store(models.Model):
    store_id = models.AutoField(primary_key=True)
    store_name = models.CharField(max_length=20, help_text="Must be filled in.")
    store_adress = models.TextField()
    store_region = models.CharField(max_length=15, help_text="Where in NZ")
    chain_id= models.ForeignKey(SupermarketChain, on_delete=models.CASCADE, help_text="Id off the super chain.")


    def __str__(self) -> str:
        return self.store_name
    def get_absolute_url(self):
        return reverse ("store_detail", kwargs= {"store_id": self.pk})

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=25)
    product_image = models.ImageField(upload_to='products/', null=True, blank=True)
    unit_type = models.CharField(max_length=10)
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE)
    product_code = models.CharField(max_length=10, unique=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    on_sale = models.BooleanField()

    def __str__(self):
        return str(self.product_name) + ": $" + str(self.unit_price)
    def get_absolute_url(self):
        return reverse ("product_detail", kwargs= {"product_id": self.pk})

class PriceHistory(models.Model):
    price_history_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    on_sale = models.BooleanField()

    def __str__(self):
        return str(self.product_id) + ": $" + str(self.price)
    def get_absolute_url(self):
        return reverse ("price_history_detail", kwargs= {"product_id": self.pk})

class User(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=30, unique=True)
    user_user_name = models.CharField(max_length=30, null=True)
    user_password = models.CharField(max_length=30)
    user_email = models.EmailField(max_length=254)
    user_type = models.CharField(max_length=30)

    def __str__(self):
        return str(self.user_id) + ": $" + str(self.user_name)
    def get_absolute_url(self):
        return reverse ("user_detail", kwargs= {"user_id": self.pk})


class UserStorePreferance(models.Model):
    USP_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.USP_id) 
    def get_absolute_url(self):
        return reverse ("user_id", kwargs= {"USP_id": self.pk})
