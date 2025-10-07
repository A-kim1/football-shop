from django.forms import ModelForm
from main.models import Product
from django import forms
from django.utils.html import strip_tags

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "stock", "description", "category", "thumbnail", "is_featured"]

        # ini tambahin kyk bayangan teks sblm ada input pake library form dari django nya
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Nama produk"}),
            "price": forms.NumberInput(attrs={"placeholder": "Harga produk"}),
            "stock": forms.NumberInput(attrs={"placeholder": "Jumlah stok"}),
            "description": forms.Textarea(attrs={"rows": 3, "placeholder": "Deskripsi produk"}),
            "category": forms.TextInput(attrs={"placeholder": "Kategori produk"}),
            "thumbnail": forms.URLInput(attrs={"placeholder": "Link gambar produk (https://...)"})
        }

    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)