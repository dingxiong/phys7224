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
        hw1Form = Hw1Form(request.POST)
        if hw1Form.is_valid():
            email = hw1Form.cleaned_data['email']
            q1 = hw1Form.cleaned_data['q1']
            q2 = hw1Form.cleaned_data['q2']
            q3 = hw1Form.cleaned_data['q3']
            q4 = hw1Form.cleaned_data['q4']
            q5 = hw1Form.cleaned_data['q5']
            points, gradeTable = grade(Hw1_key,
                                       {'q1': q1, 'q2': q2, 'q3': q3, 'q4': q4, 'q5': q5},
                                       Hw1Form())
            emailGrade(1, courseLinks[1], courseNames[1],
                       weekLinks[1], 'week 1',
                       homeworkLinks[1], 'homework 1',
                       points['gs'], points['gf'], (int)(points['gp']*100),
                       email, timezone.now(),
                       gradeTable
            )
            item = Hw1_submit(email=email, q1=q1, q2=q2,
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
            points, gradeTable = grade(Hw2_key,
                                       {'q1': q1, 'q2': q2, 'q3': q3, 'q4': q4, 'q5': q5},
                                       Hw2Form())
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


def hw3(request):
    if request.method == 'POST':
        hw3Form = Hw3Form(request.POST)
        if hw3Form.is_valid():
            email = hw3Form.cleaned_data['email']
            q1 = hw3Form.cleaned_data['q1']
            q2 = hw3Form.cleaned_data['q2']
            q3 = hw3Form.cleaned_data['q3']
            points, gradeTable = grade(Hw3_key,
                                       {'q1': q1, 'q2': q2, 'q3': q3},
                                       Hw3Form())
            emailGrade(3, courseLinks[1], courseNames[1],
                       weekLinks[3], 'week 3',
                       homeworkLinks[3], 'homework 3',
                       points['gs'], points['gf'], (int)(points['gp']*100),
                       email, timezone.now(),
                       gradeTable
            )
            item = Hw3_submit(email=email, q1=q1, q2=q2,
                              q3=q3,
                              g1=points['q1'], g2=points['q2'],
                              g3=points['q3'], gs=points['gs'],
                              gf=points['gf'], gp=points['gp'],
                              hasGraded=True,
                              time=timezone.now()
            )
            item.save()
            return HttpResponseRedirect(reverse('submitted'))

    # default action
    return render(request, 'homework3.html',
                  {'hwForm': Hw3Form()})


def hw4(request):
    if request.method == 'POST':
        hw4Form = Hw4Form(request.POST)
        if hw4Form.is_valid():
            email = hw4Form.cleaned_data['email']
            q1 = hw4Form.cleaned_data['q1']
            q2 = hw4Form.cleaned_data['q2']
            q3 = hw4Form.cleaned_data['q3']
            q4 = hw4Form.cleaned_data['q4']
            q5 = hw4Form.cleaned_data['q5']
            points, gradeTable = grade(Hw4_key,
                                       {'q1': q1, 'q2': q2, 'q3': q3, 'q4': q4, 'q5': q5},
                                       Hw4Form())
            emailGrade(4, courseLinks[1], courseNames[1],
                       weekLinks[4], 'week 4',
                       homeworkLinks[4], 'homework 4',
                       points['gs'], points['gf'], (int)(points['gp']*100),
                       email, timezone.now(),
                       gradeTable
            )
            item = Hw4_submit(email=email, q1=q1, q2=q2,
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
    return render(request, 'homework4.html',
                  {'hwForm': Hw4Form()})


def hw5(request):
    if request.method == 'POST':
        hw5Form = Hw5Form(request.POST)
        if hw5Form.is_valid():
            email = hw5Form.cleaned_data['email']
            q1 = hw5Form.cleaned_data['q1']
            q2 = hw5Form.cleaned_data['q2']
            q3 = hw5Form.cleaned_data['q3']
            q4 = hw5Form.cleaned_data['q4']
            q5 = hw5Form.cleaned_data['q5']
            points, gradeTable = grade(Hw5_key,
                                       {'q1': q1, 'q2': q2, 'q3': q3, 'q4': q4, 'q5': q5},
                                       Hw5Form())
            emailGrade(5, courseLinks[1], courseNames[1],
                       weekLinks[5], 'week 5',
                       homeworkLinks[5], 'homework 5',
                       points['gs'], points['gf'], (int)(points['gp']*100),
                       email, timezone.now(),
                       gradeTable
            )
            item = Hw5_submit(email=email, q1=q1, q2=q2,
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
    return render(request, 'homework5.html',
                  {'hwForm': Hw5Form()})


def hw6(request):
    if request.method == 'POST':
        hw6Form = Hw6Form(request.POST)
        if hw6Form.is_valid():
            email = hw6Form.cleaned_data['email']
            q1 = hw6Form.cleaned_data['q1']
            q2 = hw6Form.cleaned_data['q2']
            q3 = hw6Form.cleaned_data['q3']
            q4 = hw6Form.cleaned_data['q4']
            q5 = hw6Form.cleaned_data['q5']
            points, gradeTable = grade(Hw6_key,
                                       {'q1': q1, 'q2': q2, 'q3': q3, 'q4': q4, 'q5': q5},
                                       Hw6Form())
            emailGrade(6, courseLinks[1], courseNames[1],
                       weekLinks[6], 'week 6',
                       homeworkLinks[6], 'homework 6',
                       points['gs'], points['gf'], (int)(points['gp']*100),
                       email, timezone.now(),
                       gradeTable
            )
            item = Hw6_submit(email=email, q1=q1, q2=q2,
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
    return render(request, 'homework6.html',
                  {'hwForm': Hw6Form()})


def hw7(request):
    if request.method == 'POST':
        hw7Form = Hw7Form(request.POST)
        if hw7Form.is_valid():
            email = hw7Form.cleaned_data['email']
            q1 = hw7Form.cleaned_data['q1']
            q2 = hw7Form.cleaned_data['q2']
            q3 = hw7Form.cleaned_data['q3']
            q4 = hw7Form.cleaned_data['q4']
            points, gradeTable = grade(Hw7_key,
                                       {'q1': q1, 'q2': q2, 'q3': q3, 'q4': q4},
                                       Hw7Form())
            emailGrade(7, courseLinks[1], courseNames[1],
                       weekLinks[7], 'week 7',
                       homeworkLinks[7], 'homework 7',
                       points['gs'], points['gf'], (int)(points['gp']*100),
                       email, timezone.now(),
                       gradeTable
            )
            item = Hw7_submit(email=email, q1=q1, q2=q2,
                              q3=q3, q4=q4,
                              g1=points['q1'], g2=points['q2'],
                              g3=points['q3'], g4=points['q4'],
                              gs=points['gs'],
                              gf=points['gf'], gp=points['gp'],
                              hasGraded=True,
                              time=timezone.now()
            )
            item.save()
            return HttpResponseRedirect(reverse('submitted'))

    # default action
    return render(request, 'homework7.html',
                  {'hwForm': Hw7Form()})


######################################################################
#                      grade function                                #
######################################################################

def grade(keyTable, answer, form):
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
        if x.qtype == 'number':
            item['answer'] = value
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
            item['answer'] = dict(form.fields[name].choices)[value]
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
