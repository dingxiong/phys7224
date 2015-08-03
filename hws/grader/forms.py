from django import forms

from .models import *


class Hw1Form(forms.ModelForm):

    q1 = forms.ChoiceField(widget=forms.RadioSelect,
                           choices=(
                               ('1st', '1'),
                               ('2nd', '2'),
                               ('3rd', '3'),
                               ('4th', '4'),
                           ))

    class Meta:
        model = Hw1_submit
        fields = ['q1', 'q2', 'q3', 'q4', 'q5', 'email']


class Hw2Form(forms.ModelForm):

    q2 = forms.ChoiceField(required=False,
                           widget=forms.RadioSelect,
                           choices=(
                               ('1st', 'Stable'),
                               ('2nd', 'Unstable'),
                           ))

    q3 = forms.ChoiceField(required=False,
                           widget=forms.RadioSelect,
                           choices=(
                               ('1st', '-2'),
                               ('2nd', '-1'),
                               ('3rd', '0'),
                               ('4th', '1'),
                               ('5th', '2'),
                           ))

    q5 = forms.ChoiceField(required=False,
                           widget=forms.RadioSelect,
                           choices=(
                               ('1st', 'Pink'),
                               ('2nd', 'Black'),
                               ('3rd', 'Red'),
                               ('4th', 'Green'),
                               ('5th', 'Yellow'),
                           ))

    class Meta:
        model = Hw2_submit
        fields = ['q1', 'q2', 'q3', 'q4', 'q5', 'email']


class Hw4Form(forms.ModelForm):

    q1 = forms.ChoiceField(required=False,
                           widget=forms.RadioSelect,
                           choices=(
                               ('1st',
                                r'\(\{ e\}\)'),
                               ('2nd',
                                r'\(\{ e, \sigma_{12}, \sigma_{23}, \sigma_{31}, C^{1/3}, C^{2/3}\}\)'),
                               ('3rd',
                                r'\( \{\sigma_{12}, \sigma_{23}, \sigma_{31} \} \)'),
                               ('4rd',
                                r'\( \{C^{1/3}, C^{2/3} \} \)'),
                           ))
    
    q2 = forms.ChoiceField(required=False,
                           widget=forms.RadioSelect,
                           choices=(
                               ('1st', r'\( T_p \)'),
                               ('2nd', r'\( 2T_p\)'),
                               ('3rd', r'\( 3T_p \)'),
                               ('4rd', r'\( 6T_p \)'),
                           ))

    q5 = forms.ChoiceField(required=False,
                           widget=forms.RadioSelect,
                           choices=(
                               ('1st',
                                r'\( J^{nT_p}(x(0)) = \left( J^{T_p}(x(0)) \right)^n \)'),
                               ('2nd',
                                r'\( J^{nT_p}(x(0)) = C_n^1 \cdot \left( J^{T_p}(x(0)) \right)^n \)'),
                               ('3rd',
                                r'\( J^{nT_p}(x(0)) = C_n^{n-1} \cdot \left( J^{T_p}(x(0)) \right)^n \)'),
                               ('4th',
                                r'\( J^{nT_p}(x(0)) = \left( C_n^1 \cdot J^{T_p}(x(0)) \right)^n \)'),
                               ('5th',
                                r'\( J^{nT_p}(x(0)) = \left( C_n^{n-1} \cdot J^{T_p}(x(0)) \right)^n \)'),
                           ))

    class Meta:
        model = Hw4_submit
        fields = ['q1', 'q2', 'q3', 'q4', 'q5', 'email']

# 
