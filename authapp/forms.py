from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import PlayerUser

class PlayerRegisterForm(UserCreationForm):
    class Meta:
        model = PlayerUser
        fields = ['username', 'email', 'last_name' ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fields_name, field in self.fields.items():
            print(dir(field.widget))
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
