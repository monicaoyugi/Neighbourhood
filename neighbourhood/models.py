from django.db import models

# Create your models here.

class Business(models.Model):
    business_name = models.CharField(max_length = 50)
    business_description = models.TextField()
    user = models.ForeignKey('Profile')
    neighborhood = models.ForeignKey('Neighbourhood')
    business_email = models.EmailField()
    
    def __str__(self):
        return self.business_name
    
    @classmethod
    def search_business(cls,search_term):
        business = cls.objects.filter(business_name_icontains=search_term)
        return business
    
    