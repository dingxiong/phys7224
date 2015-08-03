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
                                '\(\{ e\}\)'),
                               ('2nd',
                                '\(\{ e, \sigma_{12}, \sigma_{23}, \sigma_{31}, C^{1/3}, C^{2/3}\}\)'),
                               ('3rd',
                                '\( \{\sigma_{12}, \sigma_{23}, \sigma_{31} \} \)'),
                               ('4rd',
                                '\( \{C^{1/3}, C^{2/3} \} \)'),
                           ))
    
    q2 = forms.ChoiceField(required=False,
                           widget=forms.RadioSelect,
                           choices=(
                               ('1st', '\( T_p \)'),
                               ('2nd', '\( 2T_p\)'),
                               ('3rd', '\( 3T_p \)'),
                               ('4rd', '\( 6T_p \)'),
                           ))

    q5 = forms.ChoiceField(required=False,
                           widget=forms.RadioSelect,
                           choices=(
                               ('1st',
                                '\( J^{nT_p}(x(0)) = \left( J^{T_p}(x(0)) \right)^n \)'),
                               ('2nd',
                                '\( J^{nT_p}(x(0)) = C_n^1 \cdot \left( J^{T_p}(x(0)) \right)^n \)'),
                               ('3rd',
                                '\( J^{nT_p}(x(0)) = C_n^{n-1} \cdot \left( J^{T_p}(x(0)) \right)^n \)'),
                               ('4th',
                                '\( J^{nT_p}(x(0)) = \left( C_n^1 \cdot J^{T_p}(x(0)) \right)^n \)'),
                               ('5th',
                                '\( J^{nT_p}(x(0)) = \left( C_n^{n-1} \cdot J^{T_p}(x(0)) \right)^n \)'),
                           ))

    class Meta:
        model = Hw4_submit
        fields = ['q1', 'q2', 'q3', 'q4', 'q5', 'email']

