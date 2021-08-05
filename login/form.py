from django import forms
from django.forms import ModelForm
from user.models import Details

class detailForm(ModelForm):
    class Meta:
        model = Details
        fields = ('username','personName','jobTitle','email','website','linkedIn','phoneNumber','personalProfile','company1','role1','company1startdate','company1enddate','jobDescription1','company2','role2','company2startdate','company2enddate','jobDescription2','skill1','skill2','skill3','skill4','skill5','skill6','collegeName1','degree1','college1startdate','college1enddate','collegeName2','cgpa1','degree2','college2startdate','college2enddate','cgpa2','project1','projectDescription1','project2','projectDescription2')
        widgets={
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'personName':forms.TextInput(attrs={'class':'form-control'}),
            'jobTitle':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'website':forms.URLInput(attrs={'class':'form-control'}),
            'linkedIn':forms.TextInput(attrs={'class':'form-control'}),
            'phoneNumber':forms.NumberInput(attrs={'class':'form-control'}),
            'personalProfile':forms.TextInput(attrs={'class':'form-control'}),

            'company1':forms.TextInput(attrs={'class':'form-control'}),
            'role1':forms.TextInput(attrs={'class':'form-control'}),
            'company1startdate':forms.TextInput(attrs={'class':'form-control'}),
            'company1enddate':forms.TextInput(attrs={'class':'form-control'}),
            'jobDecription1':forms.TextInput(attrs={'class':'form-control'}),

            'company2':forms.TextInput(attrs={'class':'form-control'}),
            'role2':forms.TextInput(attrs={'class':'form-control'}),
            'company2startdate':forms.TextInput(attrs={'class':'form-control'}),
            'company2enddate':forms.TextInput(attrs={'class':'form-control'}),
            'jobDecription2':forms.TextInput(attrs={'class':'form-control'}),

            'skill1':forms.TextInput(attrs={'class':'form-control'}),
            'skill2':forms.TextInput(attrs={'class':'form-control'}),
            'skill3':forms.TextInput(attrs={'class':'form-control'}),
            'skill4':forms.TextInput(attrs={'class':'form-control'}),
            'skill5':forms.TextInput(attrs={'class':'form-control'}),
            'skill6':forms.TextInput(attrs={'class':'form-control'}),

            'collegeName1':forms.TextInput(attrs={'class':'form-control'}),
            'degree1':forms.TextInput(attrs={'class':'form-control'}),
            'college1startdate': forms.TextInput(attrs={'class': 'form-control'}),
            'college1enddate': forms.TextInput(attrs={'class': 'form-control'}),
            'cgpa1': forms.NumberInput(attrs={'class': 'form-control'}),

            'collegeName2': forms.TextInput(attrs={'class': 'form-control'}),
            'degree2':forms.TextInput(attrs={'class':'form-control'}),
            'college2startdate':forms.TextInput(attrs={'class':'form-control'}),
            'college2enddate':forms.TextInput(attrs={'class':'form-control'}),
            'cgpa2':forms.NumberInput(attrs={'class':'form-control'}),

            'project1':forms.TextInput(attrs={'class':'form-control'}),
            'projectDescription1':forms.TextInput(attrs={'class':'form-control'}),
            'project2':forms.TextInput(attrs={'class':'form-control'}),
            'projectDescription2':forms.TextInput(attrs={'class':'form-control'}),
        }