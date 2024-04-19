from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import unicodedata

from django import forms
from django.contrib.auth import authenticate, get_user_model, password_validation
from django.contrib.auth.hashers import UNUSABLE_PASSWORD_PREFIX, identify_hasher
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ValidationError
from django.core.mail import EmailMultiAlternatives
from django.template import loader
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils.text import capfirst
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _

UserModel = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ('username', 'email','first_name','last_name', 'password1', 'password2')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
            
            
class UsernameField(forms.CharField):
    def to_python(self, value):
        value = super().to_python(value)
        if self.max_length is not None and len(value) > self.max_length:
            # Normalization can increase the string length (e.g.
            # "ﬀ" -> "ff", "½" -> "1⁄2") but cannot reduce it, so there is no
            # point in normalizing invalid data. Moreover, Unicode
            # normalization is very slow on Windows and can be a DoS attack
            # vector.
            return value
        return unicodedata.normalize("NFKC", value)

    def widget_attrs(self, widget):
        return {
            **super().widget_attrs(widget),
            "autocapitalize": "none",
            "autocomplete": "username",
        }
     
class CustomAuthenticationForm(forms.Form):
    """
    Base class for authenticating users. Extend this to get a form that accepts
    username/password logins.
    """

    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )

    error_messages = {
        "invalid_login": _(
            "Please enter a correct %(username)s and password. Note that both "
            "fields may be case-sensitive."
        ),
        "inactive": _("This account is inactive."),
    }

    def __init__(self, request=None, *args, **kwargs):
        """
        The 'request' parameter is set for custom auth use by subclasses.
        The form data comes in via the standard 'data' kwarg.
        """
        self.request = request
        self.user_cache = None
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
        # Set the max length and label for the "username" field.
        self.username_field = UserModel._meta.get_field(UserModel.USERNAME_FIELD)
        username_max_length = self.username_field.max_length or 254
        self.fields["username"].max_length = username_max_length
        self.fields["username"].widget.attrs["maxlength"] = username_max_length
        if self.fields["username"].label is None:
            self.fields["username"].label = capfirst(self.username_field.verbose_name)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username is not None and password:
            self.user_cache = authenticate(
                self.request, username=username, password=password
            )
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

    def confirm_login_allowed(self, user):
        """
        Controls whether the given User may log in. This is a policy setting,
        independent of end-user authentication. This default behavior is to
        allow login by active users, and reject login by inactive users.

        If the given user cannot log in, this method should raise a
        ``ValidationError``.

        If the given user may log in, this method should return None.
        """
        if not user.is_active:
            raise ValidationError(
                self.error_messages["inactive"],
                code="inactive",
            )

    def get_user(self):
        return self.user_cache

    def get_invalid_login_error(self):
        return ValidationError(
            self.error_messages["invalid_login"],
            code="invalid_login",
            params={"username": self.username_field.verbose_name},
        )

from django.forms import inlineformset_factory
from .models import Book, BookImage,Address

class BookForm(forms.ModelForm):
    
    class Meta:
        model = Book
        fields = ['title', 'author', 'publisher', 'category', 'description', 'price', 'stock', 'discount']
                
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'publisher': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control','row':2}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'stock': forms.TextInput(attrs={'class': 'form-control'}),
            'discount': forms.Select(attrs={'class': 'form-control'}),
        }


class BookImageForm(forms.ModelForm):
    
    class Meta:
        model = BookImage
        fields = ['image']
        
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

BookImageFormSet = inlineformset_factory(Book, BookImage, form=BookImageForm, extra=3, max_num=5)

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['street', 'city', 'state', 'country', 'postal_code']
        
        widgets = {
            'street': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control'}),
        }


from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_number', 'dob', 'gender', 'profile_image']
        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'profile_image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class ProfileUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=100, required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Profile
        fields = ['phone_number', 'dob', 'gender', 'profile_image']
        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'type':'date','class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'profile_image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
        labels = {
            'phone_number': 'Phone Number',
            'dob': 'Date of Birth',
            'gender': 'Gender',
            'profile_image': 'Profile Image',
        }
