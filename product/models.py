from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    """ Product Category Model
    
        Note:
            In this model we have nested category model

    """
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, related_name='scategory', null=True, blank=True)
    is_sub = models.BooleanField(default=False)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

	# def get_absolute_url(self):
	# 	return reverse('shop:category_filter', args=[self.slug,])

    class Meta:
        ordering = ['-pk']
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Brand(models.Model):
    """ Product brands """
    category = models.ManyToManyField(Category, related_name='brands') # find product category
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, unique=True)
    image   = models.ImageField(upload_to="brand")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-pk']


    # def get_absolute_url(self):
    #     return reverse('brand:brand_detail', args=[self.slug,])


class Product(models.Model):
    """ product class """
    category = models.ManyToManyField(Category, related_name='products')
    name =  models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='products/')
    description = models.TextField()
    price = models.IntegerField()
    stock = models.IntegerField() # product remain stock
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('shop:product_detail', args=[self.slug,])



class ProductImage(models.Model):
    """ Product images / each product can have many image """
    product = models.ForeignKey('Product', related_name='images', on_delete=models.CASCADE)
    image   = models.ImageField(upload_to="product")
    
    def __str__(self):
        return self.product.name

    class Meta:
        ordering = ['-pk']