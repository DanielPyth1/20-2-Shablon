from django import forms
from .models import Product

FORBIDDEN_WORDS = [
    'казино', 'криптовалюта', 'крипта', 'биржа',
    'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
]

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image', 'category']

    def clean_name(self):
        name = self.cleaned_data.get('name', '')
        print("Checking name:", name)  # Для отладки
        if any(word in name.lower() for word in FORBIDDEN_WORDS):
            raise forms.ValidationError("Название продукта содержит запрещенные слова.")
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description', '')
        print("Checking description:", description)  # Для отладки
        if any(word in description.lower() for word in FORBIDDEN_WORDS):
            raise forms.ValidationError("Описание продукта содержит запрещенные слова.")
        return description

