from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django.utils.safestring import mark_safe
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

class CustomErrorList(ErrorList):
    def __str__(self):
        if not self:
            return ''
        return mark_safe(''.join([f'<div class="alert alert-danger" role="alert">{e}</div>' for e in self]))

#class CustomUserCreationForm(UserCreationForm):
    #def __init__(self, *args, **kwargs):
        #super(CustomUserCreationForm, self).__init__(*args, **kwargs)
       # for fieldname in ['username', 'password1', 'password2']:
          #  self.fields[fieldname].help_text = None
          #  self.fields[fieldname].widget.attrs.update( {'class': 'form-control'} )

class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 != password2:
            raise ValidationError("The two password fields must match.")

        try:
            validate_password(password1)  # Use Django's built-in password validation
        except ValidationError as e:
            raise ValidationError(f"Password is not secure enough: {', '.join(e.messages)}")

        return password2