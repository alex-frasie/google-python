from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]


class RawProductForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField(
        required=False,
        label="",
        widget=forms.Textarea(
            attrs={"placeholder": "Your description"}
        )
    )
    price = forms.DecimalField(initial=0.0)


class ReviewForm(forms.Form):
    review = forms.CharField(
        label="",
        widget=forms.Textarea(
            attrs={"placeholder": "Write your review here",
                   "size" : 80}
        )
    )
