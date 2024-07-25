from django import forms
from .models import *
from CustomUser.models import *


class TrackRecordModelForm(forms.ModelForm):

    class Meta:
        model = TrackRecord
    
        # fields = ['User_Email', 'Track_Type','Credit_Card', 
        #           'Track_Amount', 'Track_Detail', 'Track_Date']
        fields = ['User_Email', 'Track_Type', 
                  'Track_Amount', 'Track_Detail', 'Track_Date']

        widgets = {
                'User_Email': forms.HiddenInput,
                'Track_Type': forms.Select(attrs={'class': 'form-control'}),
                # 'Credit_Card': forms.Select(attrs={'class': 'form-control'}),
                'Track_Amount': forms.NumberInput(attrs={'class': 'form-control'}),
                'Track_Detail': forms.TextInput(attrs={'class': 'form-control'}),
                'Track_Date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
            }
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(TrackRecordModelForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['User_Email'].initial = user
            self.fields['Track_Type'].queryset = TrackType.objects.filter(User_Email=user)

class TrackTypeModelForm(forms.ModelForm):

    class Meta:
        model = TrackType

        fields = ['User_Email', 'Spend_Type']

        widgets = {
                'User_Email': forms.HiddenInput,

                'Spend_Type': forms.TextInput(attrs={'class': 'form-control'})
            }
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(TrackTypeModelForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['User_Email'].initial = user

