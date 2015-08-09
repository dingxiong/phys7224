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


############################################################
# hw 8
k = Hw8_key(qname='q1', qtitle="Q8.1  two modes system continued -- kneading theory", qtype='number', numberAnswer=0.86091831,  qtol=0.01, qpoints=3)
k.save()

k = Hw8_key(qname='q2', qtitle="Q8.2  two modes system continued -- multi-shooting method", qtype='number', numberAnswer=14.6795174346, qtol=0.15, qpoints=4)
k.save()


############################################################
# hw 9
k = Hw9_key(qname='q1', qtitle='Q9.1   Transition matrix and cycle counting (Exercise 18.5)', qtype='number', numberAnswer=19, qtol=0.0001, qpoints=2)
k.save()

k = Hw9_key(qname='q2', qtitle='Q9.2  Transition matrix and cycle counting -- countinued', qtype='number', numberAnswer=1.09861, qtol=0.001, qpoints=2)
k.save()

k = Hw9_key(qname='q3', qtitle='Q9.3  Alphabet \(\{a, b, c\}\) pruned \(\_ab\_\) (exercise 18.16)', qtype='number', numberAnswer=-3, qtol=0.0001, qpoints=2)
k.save()

k = Hw9_key(qname='q4', qtitle='Q9.4  Alphabet \(\{a, b, c\}\) pruned \(\_ab\_\) -- continued', qtype='number', numberAnswer=2, qtol=0.0001, qpoints=3)
k.save()

k = Hw9_key(qname='q5', qtitle='Q9.5  Counting periodic orbit (Example 18.8, 18.9)', qtype='number', numberAnser=536, qtol=0.001, qpoints=3)
k.save()

############################################################
# hw 10
k = Hw10_key(qname='q1', qtitle='Q10.1   Natural measure of Henon map', qtype='number', numberAnswer=5, qtol=3.5, qpoints=2)
k.save()

k = Hw10_key(qname='q2', qtitle='Q10.2  Natural measure of Henon map -- continued', qtype='number', numberAnswer=13, qtol=0.001, qpoints=2)
k.save()

k = Hw10_key(qname='q3', qtitle='Q10.3  Piece-wise invariant measure (Exercise 19.5)', qtype='number', numberAnswer=0.725, qtol=0.005, qpoints=3)
k.save()

k = Hw10_key(qname='q4', qtitle='Q10.4  Escape rate in Logistic map (Exercise 20.2)', qtype='number', numberAnswer=0.552, qtol=0.008, qpoints=3)
k.save()

############################################################
# hw 11
k = Hw11_key(qname='q1', qtitle='Q11.1  Golden mean pruned map (Exercise 22.1)', qtype='number', numberAnswer=-0.385, qtol=0.005, qpoints=4)
k.save()

k = Hw11_key(qname='q2', qtitle='Q11.2  dynamic zeta function (Exercise 22.2)', qtype='number', numberAnswer=1, qtol=0.001, qpoints=3)
k.save()

############################################################
# hw 12
k = Hw12_key(qname='q1', qtitle='Q12.1   periodic orbits in Logistic map (Exercise 23.2)', qtype='number', numberAnswer=485.09371391, qtol=0.1, qpoints=2)
k.save()

k = Hw12_key(qname='q2', qtitle='Q12.2  dynamical zeta function in Logistic map', qtype='number', numberAnswer=-9.893, qtol=0.01, qpoints=3)
k.save()

k = Hw12_key(qname='q3', qtitle='Q12.3  spectral determinant in Logistic map', qtype='number', numberAnswer=4.53181525, qtol=0.01, qpoints=3)
k.save()

k = Hw12_key(qname='q4', qtitle='Q12.4  spectral determinant in Logistic map -- continued', qtype='number', numberAnswer=0.55276511, qtol=0.00001, qpoints=2)
k.save()

############################################################
# hw 13
k = Hw13_key(qname='q1', qtitle='Q13.1   Chains of piecewise linear maps (Example 24.1)', qtype='number', numberAnswer=1, qtol=0.1, qpoints=2)
k.save()

k = Hw13_key(qname='q2', qtitle='Q13.2  modification of Example 24.4', qtype='number', numberAnswer=0.3876, qtol=0.0001, qpoints=3)
k.save()

k = Hw13_key(qname='q3', qtitle='Q13.3  Diffusion for odd integer \(\Lambda\) (Exercise 24.1)', qtype='number', numberAnswer=1.1, qtol=0.001, qpoints=3)
k.save()

k = Hw13_key(qname='q4', qtitle='Q13.4   \(\quad\) Dependence of diffusion constant on slope -- Q13.1 continued', qtype='number', numberAnswer=0.35, qtol=0.03, qpoints=2)
k.save()

############################################################
# hw 14
k = Hw14_key(qname='q1', qtitle='Q14.1   number of irreducible representations', qtype='number', numberAnswer=8, qtol=0.001, qpoints=2)
k.save()

k = Hw14_key(qname='q2', qtitle='Q14.2  Character table of \(D_2\) (or \(C_{2v}\))', qtype='number', numberAnswer=-1, qtol=0.0001, qpoints=2)
k.save()

k = Hw14_key(qname='q3', qtitle='Q14.3  Invariant basis of \(C_{4v}\)', qtype='choice',  choiceAnswer='5th', qpoints=3)
k.save()

############################################################
# hw 15
k = Hw15_key(qname='q1', qtitle='Q15.1  \(C_3\) factorization', qtype='choice',  choiceAnswer='5th', qpoints=2)
k.save()

k = Hw15_key(qname='q2', qtitle='Q15.2  \(C_{4v}\) factorization', qtype='choice',  choiceAnswer='2nd', qpoints=4)
k.save()


############################################################
# hw 16
k = Hw16_key(qname='q1', qtitle='Q16.1   Invariant subspace in Kuramoto-Sivashinsky system', qtype='number', numberAnswer=0.425, qtol=0.005, qpoints=2)
k.save()

k = Hw16_key(qname='q2', qtitle='Q16.2   Period-doubling bifurcation', qtype='number', numberAnswer= 36.3225, qtol=0.01, qpoints=4)
k.save()

k = Hw16_key(qname='q3', qtitle='Q16.3  Equilibria in anti-symmetric space', qtype='number', numberAnswer=0.0305, qtol=0.0005, qpoints=3)
k.save()

k = Hw16_key(qname='q4', qtitle='Q16.4   \(\quad\) Dependence of diffusion constant on slope -- Q16.1 continued', qtype='number', numberAnswer=0.35, qtol=0.03, qpoints=2)
k.save()
