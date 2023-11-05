from django.contrib import admin

# Register your models here.
from .models import Customer
from .models import Invoice
from .models import Product
from .models import UserProfile
from .models import BillingProfile
from .models import Inventory
from .models import InventoryLog
from .models import BookLog
from .models import Book, Department, Item_description, ARC_number, Item_number, SAC_number, Service_description, UOM, Service_number

admin.site.register(UserProfile)
admin.site.register(BillingProfile)

admin.site.register(Customer)
admin.site.register(Invoice)
admin.site.register(Product)
admin.site.register(Department)
admin.site.register(Item_description)
admin.site.register(ARC_number)
admin.site.register(Item_number)
admin.site.register(SAC_number)
admin.site.register(Service_description)
admin.site.register(UOM)
admin.site.register(Service_number)
admin.site.register(Inventory)
admin.site.register(InventoryLog)
admin.site.register(Book)
admin.site.register(BookLog)