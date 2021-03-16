from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE,default='')
    product=models.CharField(default='', max_length = 40, verbose_name='Product Name')
    company=models.CharField(default='', max_length = 40, verbose_name='Company Name')
    capacity = models.IntegerField(default=0, verbose_name="Inventory's Capacity (Number of Units)")
    def __str__(self):
        return f"{self.user.username}"


class Order(models.Model):
    client=models.ForeignKey(Client, on_delete=models.CASCADE, default='')
    seller_name = models.CharField(max_length=40, default='', verbose_name="Seller's name")
    message = models.TextField(verbose_name='Message to the seller (optional)', null='True', blank='true')
    quantity=models.IntegerField(default=0)
    date_posted =models.DateTimeField(default=timezone.now)

    # ngo = models.ForeignKey(Ngo, on_delete=models.CASCADE, default='')
    # category = models.ForeignKey(Help_category,on_delete=models.CASCADE, default='')
    #quantity=models.Field(max_length=300,default='')
    # amount=models.IntegerField(max_length=999999,null=True)
    # requirement_fulfilled=models.IntegerField(max_length=255,default=0)
    # fulfilled_by=models.ManyToManyField(Donor,related_name='fulfillers')
    # from_ngo=models.ForeignKey(Student,on_delete=models.CASCADE)
    # college=models.CharField(max_length=300,default='',choices=college_choices)
    # branch=models.CharField(max_length=300,blank='true', null='true',choices=branch_choices)
    # date_resolved = models.CharField(default='', max_length = 40)
    # status = models.CharField(choices = status_choices, default='Pending', max_length = 20)
    # response = models.TextField(default='')
    # related_to = models.CharField(choices = related_to_choices, default='', max_length = 20, verbose_name = 'Complain Related to')
    # transfer = models.BooleanField(default=False)
    # likes=models.ManyToManyField(User,related_name='complain')

    # def total_likes(self):
    #     return self.likes.count()

    # def __str__(self):
    #     return f"{self.college} : {self.branch}"


    class Meta:
        ordering=['-date_posted']

class Count_table(models.Model):


    count = models.IntegerField()
    accuracy = models.IntegerField()
    def __str__(self):
        return f"{self.count}"