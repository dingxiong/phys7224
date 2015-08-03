import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hws.settings")

from django.contrib.auth.models import User
from grader.models import *

print User.objects.all()

############################################################
# hw 2
k = Hw2_key(qname='q1', qtitle="Q2.1   A contracting baker's map (ChaosBook.org version14.5.7, exercise 4.6)", qtype='number', numberAnswer='0.665', qtol=0.01, qpoints=2)
k.save()

k = Hw2_key(qname='q2', qtitle="Q2.2   A limit cycle with analytic Floquet exponent. (ChaosBook.org version14.5.7, exercise 5.1)", qtype='choice', choiceAnswer='2nd', qpoints=1)
k.save()

k = Hw2_key(qname='q3', qtitle='Q2.3   continuing from Question 2', qtype='choice', choiceAnswer='1st', qpoints=4)
k.save()

k = Hw2_key(qname='q4', qtitle='Q2.4   Stability of an equilibrium', qtype='number', numberAnswer='0.097', qtol=0.001, qpoints=3)
k.save()


k = Hw2_key(qname='q5', qtitle='Q2.5   Stability of a periodic orbit', qtype='choice', choiceAnswer='3rd', qpoints=3)
k.save()

############################################################
# hw 4
k = Hw4_key(qname='q1', qtitle="Q4.1 \(D_3\): symmetries of an equilateral triangle (ChaosBook.org version14.5.7, exercise 9.5 a)", qtype='choice', choiceAnswer='2nd',  qpoints=3)
k.save()

k = Hw4_key(qname='q2', qtitle="Q4.2  \(D_3\): symmetries of a three-billiard game", qtype='choice', choiceAnswer='3rd', qpoints=3)
k.save()

k = Hw4_key(qname='q3', qtitle='Q4.3  \(C_2\): symmetry of Lorenz flow', qtype='number', numberAnswer='4.79623498', qtol=0.2, qpoints=4)
k.save()

k = Hw4_key(qname='q4', qtitle='Q4.4  \(C_2\): symmetry of Lorenz flow: continued', qtype='number', numberAnswer='-2.17093193', qtol=0.1, qpoints=3)
k.save()

k = Hw4_key(qname='q5', qtitle='Q4.5  \(C_n\): cyclic group by a single element', qtype='choice', choiceAnswer='4th', qpoints=4)
k.save()

