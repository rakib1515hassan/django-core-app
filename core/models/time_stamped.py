from django.db import models
from django.conf import settings

from django.utils.translation import gettext_lazy as _

class TimestampedModel(models.Model):
    created_at  = models.DateTimeField(auto_now_add=True, verbose_name=_("Created Time"))
    created_by  = models.ForeignKey(
            settings.AUTH_USER_MODEL,       ##? Lazy reference to User Model
            on_delete    = models.PROTECT, 
            null         = True, 
            blank        = True, 
            related_name = '%(class)s_created_by',
            verbose_name = _("Created Person")
        )
    
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Last Updated Time"), null=True, blank=True)
    updated_by = models.ForeignKey(
            settings.AUTH_USER_MODEL,       ##? Lazy reference to User Model
            on_delete    = models.PROTECT, 
            null         = True, 
            blank        = True, 
            related_name = '%(class)s_updated_by',
            verbose_name = _("Last Updated Person")
        )
    
    is_active   = models.BooleanField(default=True, verbose_name=_("Active"))
    is_deleted  = models.BooleanField(default=False, verbose_name=_("Deleted"))

    class Meta:
        abstract = True
        ordering = ['-created_at', '-updated_at']

"""
##? Example 1:-
যেহেতু আপনার InboundCourier মডেল TimestampedModel অ্যাবস্ট্রাক্ট ক্লাস থেকে ইনহেরিট করছে, 
এবং TimestampedModel-এ আমরা related_name='%(class)s_created_by' এবং 
related_name='%(class)s_updated_by' ব্যবহার করেছি, তাই InboundCourier মডেলের জন্য 
Django অটোমেটিক্যালি নিচের related_name গুলো জেনারেট করবে:

created_by ফিল্ডের জন্য related_name হবে: inboundcourier_created_by

updated_by ফিল্ডের জন্য related_name হবে: inboundcourier_updated_by

Example:-

# যে ইউজার created_by হিসেবে আছে এমন সব InboundCourier পেতে
user.inboundcourier_created_by.all()

# যে ইউজার updated_by হিসেবে আছে এমন সব InboundCourier পেতে
user.inboundcourier_updated_by.all()

##? Example 2:-
Model Name: Product


created_by ফিল্ডের জন্য related_name হবে: product_created_by
# এই user কোন products create করেছে
created_products = user.product_created_by.all()

updated_by ফিল্ডের জন্য related_name হবে: product_updated_by
# এই user কোন products update করেছে  
updated_products = user.product_updated_by.all()
"""


