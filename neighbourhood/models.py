from django.db import models

# Create your models here.

class Business(models.Model):
    businesspic=models.ImageField(upload_to='images/',blank=True)
    businessname=models.CharField(max_length=30)
    businessemail=models.CharField(max_length=30)
    pub_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.businessname
    
    def savebusiness(self):
        self.save()
        
    def deletebusiness(self):
        self.delete()
        
    def get_businesses(cls,name):
        business=cls.objects.filter(businessname=name)
        return business
        
        
    @classmethod
    def search_by_business(cls,name):
        business=cls.objects.filter(businessname=name)
        return business
    