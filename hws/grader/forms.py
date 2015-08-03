from django import forms

from .models import *


class Hw1Form(forms.ModelForm):

    q1 = forms.ChoiceField(widget=forms.RadioSelect,
                           choices=(
                               ('1', '1'),
                               ('2', '2'),
                               ('3', '3'),
                               ('4', '4'),
                           ))

    class Meta:
        model = Hw1_submit
        fields = ['q1', 'q2', 'q3', 'q4', 'q5', 'email']


class Hw2Form(forms.ModelForm):

    q2 = forms.ChoiceField(required=False,
                           widget=forms.RadioSelect,
                           choices=(
                               ('Stable', 'Stable'),
                               ('Unstable', 'Unstable'),
                           ))
    
    q3 = forms.ChoiceField(required=False,
                           widget=forms.RadioSelect,
                           choices=(
                               ('-2', '-2'),
                               ('-1', '-1'),
                               ('0', '0'),
                               ('1', '1'),
                               ('2', '2'),
                           ))

    q5 = forms.ChoiceField(required=False,
                           widget=forms.RadioSelect,
                           choices=(
                               ('Pink', 'Pink'),
                               ('Black', 'Black'),
                               ('Red', 'Red'),
                               ('Green', 'Green'),
                               ('Yellow', 'Yellow'),
                           ))

    class Meta:
        model = Hw2_submit
        fields = ['q1', 'q2', 'q3', 'q4', 'q5', 'email']

    
