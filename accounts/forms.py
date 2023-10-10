from django import forms
from .models import Account
from phonenumber_field.modelfields import PhoneNumberField

#registrationform to register user
class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password',
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password'
    }))

    # phone_number = forms.IntegerField(widget=forms.TextInput(attrs={'id': 'phoneNo'}))
    phone_number = forms.IntegerField(widget=forms.NumberInput(attrs={'id':'phoneNo'}))


    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        phone_number = cleaned_data.get('phone_number')

        if len(str(phone_number)) != 10:
            raise forms.ValidationError(
                "Phone number should be  10 digit!"
            )

        if password != confirm_password:
            raise forms.ValidationError(
                "Password does not match!"
            )
#its a way of providing attribute to forms fields
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter last Name'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter Phone Number'
        self.fields['phone_number'].widget.attrs['type'] = 'Enter Phone Number'

        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email Address'


