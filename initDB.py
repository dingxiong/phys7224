import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hws.settings")

from django.contrib.auth.models import User
from grader.models import *

print User.objects.all()

############################################################
# hw 1
k = Hw1_key(qname='q1', qtitle="Q1.1   Equilibria of the Roessler flow (ChaosBook.org version14.5.7, exercise 2.8 a)", qtype='choice', choiceAnswer='2nd', qpoints=1)
k.save()

k = Hw1_key(qname='q2', qtitle="Q1.2   Equilibria of the Roessler flow (ChaosBook.org version14.5.7, exercise 2.8 b)", qtype='number', numberAnswer=0.007, qtol=0.0001, qpoints=3)
k.save()

k = Hw1_key(qname='q3', qtitle="Q1.3   Runge-Kutta integration", qtype='number', numberAnswer=-0.839, qtol=0.007, qpoints=3)
k.save()

k = Hw1_key(qname='q4', qtitle="Q1.4   Integrating Roessler system", qtype='number', numberAnswer=-5.56, qtol=0.07, qpoints=4)
k.save()

k = Hw1_key(qname='q5', qtitle="Q1.5   Poincare sections and return maps of the Rossler system", qtype='number', numberAnswer=8.38, qtol=0.08, qpoints=5)
k.save()

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
# hw 3
k = Hw3_key(qname='q1', qtitle="Q3.1   Shortest periodic orbit of the Rossler system ( x coordinate )", qtype='number', numberAnswer=9.265, qtol=0.1, qpoints=3)
k.save()

k = Hw3_key(qname='q2', qtitle="Q3.2   Shortest periodic orbit of the Rossler system ( y coordinate )", qtype='number', numberAnswer=0, qtol=0.0002, qpoints=3)
k.save()

k = Hw3_key(qname='q3', qtitle="Q3.3   Shortest periodic orbit of the Rossler system ( z coordinate )", qtype='number', numberAnswer=2.575, qtol=0.03, qpoints=4)
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

############################################################
# hw 5
k = Hw5_key(qname='q1', qtitle="Q5.1  generator of continuous symmetry", qtype='choice', choiceAnswer='2nd',  qpoints=2)
k.save()

k = Hw5_key(qname='q2', qtitle="Q5.2   Two modes system (Chapter 13 Excercise 13.7)", qtype='choice', choiceAnswer='3rd', qpoints=2)
k.save()

k = Hw5_key(qname='q3', qtitle='Q5.3  Two modes system continued: relative equilibria', qtype='number', numberAnswer='-0.5440841', qtol=0.3, qpoints=3)
k.save()

k = Hw5_key(qname='q4', qtitle='Q5.4  Two modes system continued: Poincare return map', qtype='number', numberAnswer='0.908', qtol=0.1, qpoints=4)
k.save()

k = Hw5_key(qname='q5', qtitle='Q5.5  Jacobian of a relative periodic orbit', qtype='choice', choiceAnswer='1st', qpoints=3)
k.save()
