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


def hw8(request):
    if request.method == 'POST':
        hw8Form = Hw8Form(request.POST)
        if hw8Form.is_valid():
            email = hw8Form.cleaned_data['email']
            q1 = hw8Form.cleaned_data['q1']
            q2 = hw8Form.cleaned_data['q2']
            points, gradeTable = grade(Hw8_key,
                                       {'q1': q1, 'q2': q2},
                                       Hw8Form())
            emailGrade(8, courseLinks[1], courseNames[1],
                       weekLinks[8], 'week 8',
                       homeworkLinks[8], 'homework 8',
                       points['gs'], points['gf'], (int)(points['gp']*100),
                       email, timezone.now(),
                       gradeTable
            )
            item = Hw8_submit(email=email, q1=q1, q2=q2,
                              g1=points['q1'], g2=points['q2'],
                              gs=points['gs'],
                              gf=points['gf'], gp=points['gp'],
                              hasGraded=True,
                              time=timezone.now()
            )
            item.save()
            return HttpResponseRedirect(reverse('submitted'))

    # default action
    return render(request, 'homework8.html',
                  {'hwForm': Hw8Form()})


def hw9(request):
    if request.method == 'POST':
        hw9Form = Hw9Form(request.POST)
        if hw9Form.is_valid():
            email = hw9Form.cleaned_data['email']
            q1 = hw9Form.cleaned_data['q1']
            q2 = hw9Form.cleaned_data['q2']
            q3 = hw9Form.cleaned_data['q3']
            q4 = hw9Form.cleaned_data['q4']
            q5 = hw9Form.cleaned_data['q5']
            points, gradeTable = grade(Hw9_key,
                                       {'q1': q1, 'q2': q2, 'q3': q3, 'q4': q4, 'q5': q5},
                                       Hw9Form())
            emailGrade(9, courseLinks[1], courseNames[1],
                       weekLinks[9], 'week 9',
                       homeworkLinks[9], 'homework 9',
                       points['gs'], points['gf'], (int)(points['gp']*100),
                       email, timezone.now(),
                       gradeTable
            )
            item = Hw9_submit(email=email, q1=q1, q2=q2,
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
    return render(request, 'homework9.html',
                  {'hwForm': Hw9Form()})


def hw10(request):
    if request.method == 'POST':
        hw10Form = Hw10Form(request.POST)
        if hw10Form.is_valid():
            email = hw10Form.cleaned_data['email']
            q1 = hw10Form.cleaned_data['q1']
            q2 = hw10Form.cleaned_data['q2']
            q3 = hw10Form.cleaned_data['q3']
            q4 = hw10Form.cleaned_data['q4']
            points, gradeTable = grade(Hw10_key,
                                       {'q1': q1, 'q2': q2, 'q3': q3, 'q4': q4},
                                       Hw10Form())
            emailGrade(10, courseLinks[1], courseNames[1],
                       weekLinks[10], 'week 10',
                       homeworkLinks[10], 'homework 10',
                       points['gs'], points['gf'], (int)(points['gp']*100),
                       email, timezone.now(),
                       gradeTable
            )
            item = Hw10_submit(email=email, q1=q1, q2=q2,
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
    return render(request, 'homework10.html',
                  {'hwForm': Hw10Form()})


def hw11(request):
    if request.method == 'POST':
        hw11Form = Hw11Form(request.POST)
        if hw11Form.is_valid():
            email = hw11Form.cleaned_data['email']
            q1 = hw11Form.cleaned_data['q1']
            q2 = hw11Form.cleaned_data['q2']
            points, gradeTable = grade(Hw11_key,
                                       {'q1': q1, 'q2': q2},
                                       Hw11Form())
            emailGrade(11, courseLinks[1], courseNames[1],
                       weekLinks[11], 'week 11',
                       homeworkLinks[11], 'homework 11',
                       points['gs'], points['gf'], (int)(points['gp']*100),
                       email, timezone.now(),
                       gradeTable
            )
            item = Hw11_submit(email=email, q1=q1, q2=q2,
                               g1=points['q1'], g2=points['q2'],
                               gs=points['gs'],
                               gf=points['gf'], gp=points['gp'],
                               hasGraded=True,
                               time=timezone.now()
            )
            item.save()
            return HttpResponseRedirect(reverse('submitted'))

    # default action
    return render(request, 'homework11.html',
                  {'hwForm': Hw11Form()})


def hw12(request):
    if request.method == 'POST':
        hw12Form = Hw12Form(request.POST)
        if hw12Form.is_valid():
            email = hw12Form.cleaned_data['email']
            q1 = hw12Form.cleaned_data['q1']
            q2 = hw12Form.cleaned_data['q2']
            q3 = hw12Form.cleaned_data['q3']
            q4 = hw12Form.cleaned_data['q4']
            points, gradeTable = grade(Hw12_key,
                                       {'q1': q1, 'q2': q2, 'q3': q3, 'q4': q4},
                                       Hw12Form())
            emailGrade(12, courseLinks[1], courseNames[1],
                       weekLinks[12], 'week 12',
                       homeworkLinks[12], 'homework 12',
                       points['gs'], points['gf'], (int)(points['gp']*100),
                       email, timezone.now(),
                       gradeTable
            )
            item = Hw12_submit(email=email, q1=q1, q2=q2,
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
    return render(request, 'homework12.html',
                  {'hwForm': Hw12Form()})


def hw13(request):
    if request.method == 'POST':
        hw13Form = Hw13Form(request.POST)
        if hw13Form.is_valid():
            email = hw13Form.cleaned_data['email']
            q1 = hw13Form.cleaned_data['q1']
            q2 = hw13Form.cleaned_data['q2']
            q3 = hw13Form.cleaned_data['q3']
            q4 = hw13Form.cleaned_data['q4']
            points, gradeTable = grade(Hw13_key,
                                       {'q1': q1, 'q2': q2, 'q3': q3, 'q4': q4},
                                       Hw13Form())
            emailGrade(13, courseLinks[1], courseNames[1],
                       weekLinks[13], 'week 13',
                       homeworkLinks[13], 'homework 13',
                       points['gs'], points['gf'], (int)(points['gp']*100),
                       email, timezone.now(),
                       gradeTable
            )
            item = Hw13_submit(email=email, q1=q1, q2=q2,
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
    return render(request, 'homework13.html',
                  {'hwForm': Hw13Form()})


def hw14(request):
    if request.method == 'POST':
        hw14Form = Hw14Form(request.POST)
        if hw14Form.is_valid():
            email = hw14Form.cleaned_data['email']
            q1 = hw14Form.cleaned_data['q1']
            q2 = hw14Form.cleaned_data['q2']
            q3 = hw14Form.cleaned_data['q3']
            points, gradeTable = grade(Hw14_key,
                                       {'q1': q1, 'q2': q2, 'q3': q3},
                                       Hw14Form())
            emailGrade(14, courseLinks[1], courseNames[1],
                       weekLinks[14], 'week 14',
                       homeworkLinks[14], 'homework 14',
                       points['gs'], points['gf'], (int)(points['gp']*100),
                       email, timezone.now(),
                       gradeTable
            )
            item = Hw14_submit(email=email, q1=q1, q2=q2, q3=q3,
                               g1=points['q1'], g2=points['q2'],
                               g3=points['q3'], gs=points['gs'],
                               gf=points['gf'], gp=points['gp'],
                               hasGraded=True,
                               time=timezone.now()
            )
            item.save()
            return HttpResponseRedirect(reverse('submitted'))

    # default action
    return render(request, 'homework14.html',
                  {'hwForm': Hw14Form()})


def hw15(request):
    if request.method == 'POST':
        hw15Form = Hw15Form(request.POST)
        if hw15Form.is_valid():
            email = hw15Form.cleaned_data['email']
            q1 = hw15Form.cleaned_data['q1']
            q2 = hw15Form.cleaned_data['q2']
            points, gradeTable = grade(Hw15_key,
                                       {'q1': q1, 'q2': q2},
                                       Hw15Form())
            emailGrade(15, courseLinks[1], courseNames[1],
                       weekLinks[15], 'week 15',
                       homeworkLinks[15], 'homework 15',
                       points['gs'], points['gf'], (int)(points['gp']*100),
                       email, timezone.now(),
                       gradeTable
            )
            item = Hw15_submit(email=email, q1=q1, q2=q2,
                               g1=points['q1'], g2=points['q2'],
                               gs=points['gs'],
                               gf=points['gf'], gp=points['gp'],
                               hasGraded=True,
                               time=timezone.now()
            )
            item.save()
            return HttpResponseRedirect(reverse('submitted'))

    # default action
    return render(request, 'homework15.html',
                  {'hwForm': Hw15Form()})


def hw16(request):
    if request.method == 'POST':
        hw16Form = Hw16Form(request.POST)
        if hw16Form.is_valid():
            email = hw16Form.cleaned_data['email']
            q1 = hw16Form.cleaned_data['q1']
            q2 = hw16Form.cleaned_data['q2']
            q3 = hw16Form.cleaned_data['q3']
            points, gradeTable = grade(Hw16_key,
                                       {'q1': q1, 'q2': q2, 'q3': q3},
                                       Hw16Form())
            emailGrade(16, courseLinks[1], courseNames[1],
                       weekLinks[16], 'week 16',
                       homeworkLinks[16], 'homework 16',
                       points['gs'], points['gf'], (int)(points['gp']*100),
                       email, timezone.now(),
                       gradeTable
            )
            item = Hw16_submit(email=email, q1=q1, q2=q2,
                               q3=q3,
                               g1=points['q1'], g2=points['q2'],
                               g3=points['q3'],
                               gs=points['gs'],
                               gf=points['gf'], gp=points['gp'],
                               hasGraded=True,
                               time=timezone.now()
            )
            item.save()
            return HttpResponseRedirect(reverse('submitted'))

    # default action
    return render(request, 'homework16.html',
                  {'hwForm': Hw16Form()})


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
