from django import forms
from django.core.exceptions import ValidationError
from .models import Product, Version
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

FORBIDDEN_WORDS = [
    'казино', 'криптовалюта', 'крипта', 'биржа',
    'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
]

class FormMixin:
    def __init__(self, *args, **kwargs):
        super(FormMixin, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'

class ProductForm(FormMixin, forms.ModelForm):
    version_number = forms.CharField(required=False, label="Version Number", widget=forms.TextInput(attrs={'class': 'form-control'}))
    version_name = forms.CharField(required=False, label="Version Name", widget=forms.TextInput(attrs={'class': 'form-control'}))
    is_current_version = forms.BooleanField(required=False, label="Is Current Version", widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image', 'category', 'version_number', 'version_name', 'is_current_version']

    def clean_name(self):
        name = self.cleaned_data['name']
        if any(word in name.lower() for word in FORBIDDEN_WORDS):
            raise ValidationError("Название продукта содержит запрещенные слова.")
        return name

    def clean_description(self):
        description = self.cleaned_data['description']
        if any(word in description.lower() for word in FORBIDDEN_WORDS):
            raise ValidationError("Описание продукта содержит запрещенные слова.")
        return description

    def save(self, commit=True):
        instance = super().save(commit=False)

        version_number = self.cleaned_data.get('version_number', None)
        version_name = self.cleaned_data.get('version_name', None)
        is_current_version = self.cleaned_data.get('is_current_version', False)

        if commit:
            instance.save()

            if version_number and version_name:
                Version.objects.update_or_create(
                    product=instance,
                    defaults={
                        'version_number': version_number,
                        'version_name': version_name,
                        'is_current': is_current_version
                    }
                )

        return instance


class VersionForm(FormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = ['version_number', 'version_name', 'is_current']

    def __init__(self, *args, **kwargs):
        super(VersionForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-10'

        self.helper.layout = Layout(
            Row(
                Column('version_number', css_class='col-md-6 mb-3'),
                Column('version_name', css_class='col-md-6 mb-3'),
            ),
            Row(
                Column('is_current', css_class='col-md-6 mb-3'),
            ),
            Submit('submit', 'Сохранить', css_class='btn btn-primary')
        )

        self.fields['version_number'].widget.attrs.update({'class': 'form-control'})
        self.fields['version_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['is_current'].widget.attrs.update({'class': 'form-check-input'})