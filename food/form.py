from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name','item_desc','item_price','item_image','item_shopName','item_shopAddress','item_discountOffer','item_userRole']