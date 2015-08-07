from django import forms

from .models import *


class Hw1Form(forms.ModelForm):

    q1 = forms.ChoiceField(required=False,
                           widget=forms.RadioSelect,
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


class Hw3Form(forms.ModelForm):

    class Meta:
        model = Hw3_submit
        fields = ['q1', 'q2', 'q3', 'email']


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
                               ('4th',
                                r'\( \{C^{1/3}, C^{2/3} \} \)'),
                           ))
    
    q2 = forms.ChoiceField(required=False,
                           widget=forms.RadioSelect,
                           choices=(
                               ('1st', r'\( T_p \)'),
                               ('2nd', r'\( 2T_p\)'),
                               ('3rd', r'\( 3T_p \)'),
                               ('4th', r'\( 6T_p \)'),
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


class Hw5Form(forms.ModelForm):

    q1 = forms.ChoiceField(required=False,
                           widget=forms.RadioSelect,
                           choices=(
                               ('1st',
                                r'\( T_\tau = T_1\) , \(T_\rho = T_1 \)'),
                               ('2nd',
                                r'\( T_\tau = T_1\) , \(T_\rho = T_2 \)'),
                               ('3rd',
                                r'\( T_\tau = T_2\) , \(T_\rho = T_1 \)'),
                               ('4th',
                                r'\( T_\tau = T_2\) , \(T_\rho = T_2 \)'),
                           ))
    
    q2 = forms.ChoiceField(required=False,
                           widget=forms.RadioSelect,
                           choices=(
                               ('1st', 0),
                               ('2nd', 1),
                               ('3rd', 2),
                               ('4th', 3),
                               ('5th', 'none of above')
                           ))

    q5 = forms.ChoiceField(required=False,
                           widget=forms.RadioSelect,
                           choices=(
                               ('1st',
                                r'\( J_p(x)t(x) = t(x) \)'),
                               ('2nd',
                                r'\( J_p(x)t(x) = g(\phi_p)t(x) \)'),
                               ('3rd',
                                r'\( J_p(x)t(x) = g(-\phi_p)t(x) \)'),
                               ('4th',
                                r'\( J_p(x)t(x) = t\left(g(\phi_p)x\right) \)'),
                               ('5th',
                                r'\( J_p(x)t(x) = t\left(g(-\phi_p)x\right) \)'),
                           ))

    class Meta:
        model = Hw5_submit
        fields = ['q1', 'q2', 'q3', 'q4', 'q5', 'email']


class Hw6Form(forms.ModelForm):

    q1 = forms.ChoiceField(required=False,
                           widget=forms.RadioSelect,
                           choices=(
                               ('1st',
                                r"\( h(\hat{x}) \) is not symmetric in general"),
                               ('2nd',
                                r"\( h(\hat{x})  t(\hat{x}) = 0 \)"),
                               ('3rd',
                                r"\( t'^\top  h(\hat{x})  = 0 \)"),
                               ('4th',
                                r"\( h(\hat{x}) \) is not well defined at slice boarder"),
                               ('5th',
                                r"The inverse of \( h(\hat{x}) \) transforms \(\hat{v}(\hat{x}) \) to \( v(\hat{x})\)"),
                           ))
    
    q2 = forms.ChoiceField(required=False,
                           widget=forms.RadioSelect,
                           choices=(
                               ('1st',
                                r'\( \hat{J}(\hat{x}_2, \hat{x}_1) h(\hat{x}_1)g(-\phi_1) = h(\hat{x}_2) g(-\phi_2) J(x_2, x_1) \)'),
                               ('2nd',
                                r'\( h(\hat{x}_1)g(-\phi_1) \hat{J}(\hat{x}_2, \hat{x}_1) = J(x_2, x_1) h(\hat{x}_2) g(-\phi_2) \)'),
                               ('3rd',
                                r'\( \hat{J}(\hat{x}_2, \hat{x}_1) h(\hat{x}_1) = h(\hat{x}_2)  J(x_2, x_1) \)'),
                               ('4th',
                                r'\( \hat{J}(\hat{x}_2, \hat{x}_1) g(-\phi_1) = g(-\phi_2) J(x_2, x_1) \)'),
                               ('5th',
                                r'\( \hat{J}(\hat{x}_2, \hat{x}_1) h(\hat{x}_1)g(\phi_1) = h(\hat{x}_2) g(\phi_2) J(x_2, x_1) \)'),
                               ('6th',
                                r'\( h(\hat{x}_1)g(\phi_1) \hat{J}(\hat{x}_2, \hat{x}_1) = J(x_2, x_1) h(\hat{x}_2) g(\phi_2) \)'),
                               ('7th',
                                r'none of above'),
                           ))

    q5 = forms.ChoiceField(required=False,
                           widget=forms.RadioSelect,
                           choices=(
                               ('1st',
                                r'\( \overline{1}  \)'),
                               ('2nd',
                                r'\( \overline{01}\)'),
                               ('3rd',
                                r'\( \overline{001}\)'),
                               ('4th',
                                r'\( \overline{01011}\)'),
                               ('5th',
                                r'\( \overline{101110} \)'),
                           ))

    class Meta:
        model = Hw6_submit
        fields = ['q1', 'q2', 'q3', 'q4', 'q5', 'email']


class Hw7Form(forms.ModelForm):
    
    q2 = forms.ChoiceField(required=False,
                           widget=forms.RadioSelect,
                           choices=(
                               ('1st', "0B"),
                               ('2nd', "0D"),
                               ('3rd', "BC"),
                               ('4th', "CD"),
                               ('5th', "none of above"),
                           ))

    class Meta:
        model = Hw7_submit
        fields = ['q1', 'q2', 'q3', 'q4', 'email']


