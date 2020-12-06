from django import forms

DELIVERY = (
    ('Pick Up','Pick Up'),
    ('Delivery','Delivery'),
)

class DeliveryForm(forms.Form):
    deliver = forms.ChoiceField(label='Delivery',choices=DELIVERY)
