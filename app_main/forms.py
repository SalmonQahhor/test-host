from django.forms import ModelForm

from app_main.models import Product



class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'image']



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
         
        for c in self.fields.values():
            c.widget.attrs.update({'class': 'form-control'})