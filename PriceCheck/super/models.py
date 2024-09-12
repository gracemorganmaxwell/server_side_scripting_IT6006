from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import render, get_object_or_404


class SupermarketChain(models.Model):
    NEW_WORLD = 'Nw'
    COUNTDOWN = 'Cd'
    PAK_N_SAVE = 'Ps'
    FRESH_CHOICE = 'Fc'
    WAREHOUSE = 'Wh'
    super_market_chain = [
        (NEW_WORLD , 'New World'),
        (COUNTDOWN , 'Countdown'),
        (PAK_N_SAVE , 'Pak n Save'),
        (FRESH_CHOICE , 'Fresh Choice'),
        (WAREHOUSE , 'Warehouse'),
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
    store_address = models.TextField()
    store_region = models.CharField(max_length=15, help_text="Where in NZ")
    chain_id= models.ForeignKey(SupermarketChain, on_delete=models.CASCADE, help_text="Id off the super chain.")


    def __str__(self) -> str:
        return self.store_name
    def get_absolute_url(self):
        return reverse ("store_detail", kwargs= {"store_id": self.pk})

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    product_size = models.CharField(max_length=10)
    product_image = models.ImageField(upload_to='products/', null=True, blank=True)
    product_category = models.CharField(max_length=100)
    product_source_site = models.TextField()
    unit_type = models.CharField(max_length=10)
    product_code = models.CharField(max_length=10, unique=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=None)
    on_sale = models.BooleanField(null=True, default=None)
    last_updated = models.DateField(auto_now=True)
    last_checked = models.DateField(auto_now=True)
    original_unit_quantity = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=None)

    def __str__(self):
        return str(self.product_name) + ": $" + str(self.unit_price)
    def get_absolute_url(self):
        return reverse ("product_detail", kwargs= {"product_id": self.pk})

class PriceHistory(models.Model):
    price_history_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    on_sale = models.BooleanField(null=True, default=None)
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.product_id) + ": $" + str(self.price)
    def get_absolute_url(self):
        return reverse ("price_history_detail", kwargs= {"product_id": self.pk})

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=30, blank=True)
    # Add any other fields you want in the profile

    def __str__(self):
        return f'{self.user.username} Profile'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class UserStorePreference(models.Model):
    USP_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    store = models.ForeignKey('Store', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s preference for {self.store.store_name}"

    def get_absolute_url(self):
        return reverse("user_store_preference_detail", kwargs={"USP_id": self.pk})



class FavoriteProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s favorite products: {self.product.product_name}"


