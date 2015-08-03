from django.contrib.auth.models import User
from grader.models import *


print User.objects.all()

k = Hw2_key(qname='q1', qtitle="Q2.1   A contracting baker's map (ChaosBook.org version14.5.7, exercise 4.6)", qtype='number', numberAnswer='0.665', qtol=0.01, qpoints=2)
k.save()

k = Hw2_key(qname='q2', qtitle="Q2.2   A limit cycle with analytic Floquet exponent. (ChaosBook.org version14.5.7, exercise 5.1)", qtype='choice', choiceAnswer='Unstable', qpoints=1)
k.save()

k = Hw2_key(qname='q3', qtitle='Q2.3   continuing from Question 2', qtype='choice', choiceAnswer='-2', qpoints=4)
k.save()

k = Hw2_key(qname='q4', qtitle='Q2.4   Stability of an equilibrium', qtype='number', numberAnswer='0.097', qtol=0.001, qpoints=3)
k.save()


k = Hw2_key(qname='q5', qtitle='Q2.5   Stability of a periodic orbit', qtype='choice', choiceAnswer='Red', qpoints=3)
k.save()

