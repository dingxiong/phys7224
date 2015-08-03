from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone
from .forms import *


def submitted(request):
    return render(request, 'submitted.html')


def hw1(request):
    if request.method == 'POST':
        
        return render(request, 'homework1.html',
                      {'hwForm': Hw1Form()})

    # default action
    return render(request, 'homework1.html',
                  {'hwForm': Hw1Form()})


def hw2(request):
    if request.method == 'POST':
        hw2Form = Hw2Form(request.POST)
        if hw2Form.is_valid():
            email = hw2Form.cleaned_data['email']
            q1 = hw2Form.cleaned_data['q1']
            q2 = hw2Form.cleaned_data['q2']
            q3 = hw2Form.cleaned_data['q3']
            q4 = hw2Form.cleaned_data['q4']
            q5 = hw2Form.cleaned_data['q5']
            points = grade(Hw2_key, {'q1': q1, 'q2': q2, 'q3': q3, 'q4': q4, 'q5': q5})
            item = Hw2_submit(email=email, q1=q1, q2=q2,
                              q3=q3, q4=q4, q5=q5,
                              g1=points['q1'], g2=points['q2'],
                              g3=points['q3'], g4=points['q4'],
                              g5=points['q5'], gs=points['gs'],
                              gp=points['gp'], hasGraded=True,
                              time=timezone.now()
            )
            item.save()
            return HttpResponseRedirect(reverse('submitted'))

    # default action
    return render(request, 'homework2.html',
                  {'hwForm': Hw2Form()})


######################################################################
#                      grade function                                #
######################################################################

def grade(keyTable, answer):
    points = {}
    full = 0.0
    s = 0.0
    for name, value in answer.iteritems():
        x = keyTable.objects.get(qname=name)
        full += x.qpoints
        if x.qtype == 'number':
            if abs(value - x.numberAnswer) <= x.qtol:
                points[name] = x.qpoints
                s += x.qpoints
            else:
                points[name] = 0
                
        elif x.qtype == 'choice':
            if value == x.choiceAnswer:
                points[name] = x.qpoints
                s += x.qpoints
            else:
                points[name] = 0
        else :
            print "wrong type"

    points['gs'] = s
    points['gp'] = s / full

    return points
