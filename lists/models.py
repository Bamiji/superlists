from django.core.urlresolvers import reverse
from django.db import models
from django.conf import settings

class List(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    
    def get_absolute_url(self):
        return reverse('view_list', args=[self.id])
        
<<<<<<< HEAD
    @staticmethod
    def create_new(first_item_text, owner=None):
        list_ = List.objects.create(owner=owner)
        Item.objects.create(text=first_item_text, list=list_)
        return list_
    
=======
>>>>>>> 9ae3dc6ed7a103727e5453a7be6490491a53fac3
    @property
    def name(self):
        return self.item_set.first().text
    
class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None)
    
