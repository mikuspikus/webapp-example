import django.forms as forms

from . import models

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = models.Application

        exclude = ('applied_at', )

        widgets = {
            'name' : forms.TextInput(attrs = {'class': 'input100', 'placeholder' : 'Имя', 'data-validate' : 'Это поле обязательно'}),
            'surname' : forms.TextInput(attrs = {'class': 'input100', 'placeholder' : 'Фамилия', 'data-validate' : 'Это поле обязательно'}),
            'phone' : forms.TextInput(attrs = {'class': 'input100', 'placeholder' : 'Контактный телефон', 'data-validate' : 'Это поле обязательно'}),
        }

        labels = {
            'name' : 'Имя',
            'surname' : 'Фамилия',
            'phone' : 'Контактный телефон',
        }

        # help_texts = {
        #     '' : '',
        # }

        error_messages = {
            'name' : {'max_length': 'Слишком много символов в поле \'Имя\''},
            'surname' : {'max_length': 'Слишком много символов в поле \'Фамилия\''},
            'phone' : {'max_length': 'Слишком много символов в поле \'Контактный телефон\''},
        }