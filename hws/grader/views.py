from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.template.loader import get_template
from django.template import Context
from django.core.mail import EmailMultiAlternatives
from .forms import *
from .info import *

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
            points, gradeTable = grade(Hw2_key, {'q1': q1, 'q2': q2, 'q3': q3, 'q4': q4, 'q5': q5})
            emailGrade(2, courseLinks[1], courseNames[1],
                       weekLinks[2], 'week 2',
                       homeworkLinks[2], 'homework 2',
                       points['gs'], points['gf'], (int)(points['gp']*100),
                       email, timezone.now(),
                       gradeTable
            )
            item = Hw2_submit(email=email, q1=q1, q2=q2,
                              q3=q3, q4=q4, q5=q5,
                              g1=points['q1'], g2=points['q2'],
                              g3=points['q3'], g4=points['q4'],
                              g5=points['q5'], gs=points['gs'],
                              gf=points['gf'], gp=points['gp'],
                              hasGraded=True,
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

    # a list of dic {full, color, points, answer, title}
    gradeTable = []

    full = 0.0
    s = 0.0
    for name, value in sorted(answer.iteritems()):
        x = keyTable.objects.get(qname=name)
        full += x.qpoints
        item = {}
        item['full'] = x.qpoints
        item['title'] = x.qtitle
        item['answer'] = value
        if x.qtype == 'number':
            if value is not None and abs(value - x.numberAnswer) <= x.qtol:
                points[name] = x.qpoints
                s += x.qpoints
                item['points'] = x.qpoints
                item['color'] = '#06ac06'
            else:
                points[name] = 0
                item['points'] = 0
                item['color'] = '#FF3333'
                
        elif x.qtype == 'choice':
            if value is not None and value == x.choiceAnswer:
                points[name] = x.qpoints
                s += x.qpoints
                item['points'] = x.qpoints
                item['color'] = '#06ac06'
            else:
                points[name] = 0
                item['points'] = 0
                item['color'] = '#FF3333'
        else:
            print "wrong type"

        gradeTable.append(item)

    points['gs'] = s
    points['gf'] = full
    points['gp'] = s / full

    return points, gradeTable


######################################################################
#                      email function                                #
######################################################################


def emailGrade(hwNo, courseLink, courseName, weekLink, weekName,
               homeworkLink, homeworkName, gradeSum, gradeFull,
               percent, email, time, gradeTable):
    htmlMsg = get_template('baseEmail.html')
    textMsg = get_template('baseEmail.txt')
    d = Context({
        'hwNo': hwNo,
        'courseLink': courseLink,
        'courseName': courseName,
        'weekLink': weekLink,
        'weekName': weekName,
        'homeworkLink': homeworkLink,
        'homeworkName': homeworkName,
        'gradeSum': gradeSum,
        'gradeFull': gradeFull,
        'percent': percent,
        'email': email,
        'time': time,
        'gradeTable': gradeTable
    })
    
    subject = 'Your grade for ' + homeworkName
    fromEamil = 'phys7224@gmail.com'
    to = email
    txtContent = textMsg.render(d)
    htmlContent = htmlMsg.render(d)
    
    msg = EmailMultiAlternatives(subject, txtContent, fromEamil, [to])
    msg.attach_alternative(htmlContent, "text/html")
    msg.send()
    
    
