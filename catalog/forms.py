from django.core.exceptions import ValidationError
from django.forms import ModelForm

from catalog.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "category", "price", "image", "is_published"]

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields["name"].widget.attrs.update({"class": "form-control", "placeholder": "Введите название продукта"})
        self.fields["description"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите описание продукта"}
        )
        self.fields["category"].widget.attrs.update(
            {"class": "form-check", "placeholder": "Введите категорию продукта"}
        )
        self.fields["price"].widget.attrs.update({"class": "form-control", "placeholder": "Введите цену продукта"})

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        description = cleaned_data.get("description")

        FORBIDDEN_WORDS = [
            "казино",
            "криптовалюта",
            "крипта",
            "биржа",
            "дешево",
            "бесплатно",
            "обман",
            "полиция",
            "радар",
        ]

        if name:
            for word in FORBIDDEN_WORDS:
                if word.lower() in name.lower():
                    self.add_error("name", "Наименование продукта не должно содержать запрещенных слов")

        if description:
            for word in FORBIDDEN_WORDS:
                if word.lower() in description.lower():
                    self.add_error("description", "Описание продукта не должно содержать запрещенных слов")

        return cleaned_data

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price is None or price == "":
            return 0
        elif price < 0:
            raise ValidationError("Стоимость не может быть отрицательной")
        return price


class ProductModeratorForm(ModelForm):
    class Meta:
        model = Product
        fields = ["is_published"]
