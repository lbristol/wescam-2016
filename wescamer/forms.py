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
        
        email = self.cleaned_data['email'] #+ "@wesleyan.edu" 

        if (Student.objects.filter(email=email, isRegistered=False).count() == 1):
            user = super(StudentCreateForm, self).save(commit=False)
            user.email = email
            username = self.cleaned_data["email"].split("@wesleyan.edu")[0]
            user.username = username
            print email
            student = Student.objects.get(email=email, isRegistered=False)
            student.isRegistered = True

            if commit:
                user.save()
                student.user_id = user.id
                print user.id

                student.save()
            return user
        return

class AddCrush(forms.Form):
    crush_username = forms.CharField(label="crush_username", max_length=100)