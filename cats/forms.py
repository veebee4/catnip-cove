from django import forms
from .models import Cat

class CatForm(forms.ModelForm):

    class Meta:
        model = Cat
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        cats = Cat.objects.all()

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'