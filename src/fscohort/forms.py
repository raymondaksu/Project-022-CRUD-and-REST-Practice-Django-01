from django import forms
from .models import Student

# class StudentForm(forms.Form):
#     first_name = forms.CharField(max_length=50, label="Your Name")
#     last_name = forms.CharField(max_length=50, label="Your Surname")
#     number = forms.IntegerField()

class StudentForm(forms.ModelForm):

    first_name = forms.CharField(label='YourName')

    class Meta:
        model = Student
        fields = ("first_name", "last_name", "number") # '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].label = 'My Name'