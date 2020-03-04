from django.db import models

class Profile(models.Model):
    name = models.CharField('adi',max_length=20)
    surname = models.CharField('soyadi',max_length=30)
    image = models.ImageField(upload_to='images/')
    

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name= 'Profil'
        verbose_name_plural= 'Profiller'
        ordering = ('name',)

    def __str__(self):
        return self.name




class Post(models.Model):
    POST_TYPES = (('p','problem'),('s','solution'))

    category = models.CharField(max_length=1,choices=POST_TYPES)
    profiles = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='post')
    text = models.TextField('metn')
    comment = models.TextField('sherh')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




class Book(models.Model):
    title = models.CharField('kitab adi',max_length=25,)
    price = models.DecimalField('qiymet',max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to='images/')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name= 'Kitab'
        verbose_name_plural= 'Kitablar'
        ordering = ('title',)

    def __str__(self):
        return self.title
