from django import forms


TYPE_OF_DISH = [
        ('DIN', 'Dinner'),
        ('LUN', 'Lunch'),
        ('BRK', 'Breakfast'),
    ]

COUNT_OF_PERSONS = [
        ('1', '1 Person'),
        ('2', '2 Person'),
        ('3', '3 Person'),
        ('4', '4 Person')
    ]


class BookATable(forms.Form):
    name = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Your Name'}))
    phone = forms.IntegerField(label='', widget=forms.TextInput(attrs={'placeholder': 'Phone no.'}))
    date = forms.DateField(label='', widget=forms.TextInput(attrs={'placeholder': 'Date'}))
    type_of_dish = forms.ChoiceField(label='', choices=TYPE_OF_DISH)
    count_of_persons = forms.ChoiceField(label='', choices=COUNT_OF_PERSONS)
