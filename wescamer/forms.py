from django import forms
from django.contrib.auth.forms import UserCreationForm
from models import Student
from django.contrib.auth.models import User

class StudentCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("email", "password1", "password2")

    def save(self, commit=True):
        user = super(StudentCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        username = self.cleaned_data["email"].split("@wesleyan.edu")[0]
        user.username = username
        user.student.username = username

        if commit:
            user.save()
            user.student.save()

        return user