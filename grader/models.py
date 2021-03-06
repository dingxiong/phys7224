from django.db import models


class Hw1_submit(models.Model):
    """
    qi: the user submision
    gi: the corresponding grade
    """
    email = models.EmailField(max_length=300)
    time = models.DateTimeField()
    hasGraded = models.BooleanField(default=False)
    
    q1 = models.CharField(blank=True, max_length=500)
    q2 = models.FloatField(blank=True, null=True)
    q3 = models.FloatField(blank=True, null=True)
    q4 = models.FloatField(blank=True, null=True)
    q5 = models.FloatField(blank=True, null=True)

    g1 = models.FloatField(blank=True, default=0)
    g2 = models.FloatField(blank=True, default=0)
    g3 = models.FloatField(blank=True, default=0)
    g4 = models.FloatField(blank=True, default=0)
    g5 = models.FloatField(blank=True, default=0)
    gs = models.FloatField(blank=True, default=0)    # total points
    gf = models.FloatField(blank=True, default=0)    # full points
    gp = models.FloatField(blank=True, default=0)    # percentage

    def __str__(self):
        return self.email


class Hw1_key(models.Model):
    """
    qname : name of the question
    qtitle: title of the question
    qtype : type of the question. only 'number' or 'choice'
    choiceAnswer : answer for choice type question
    numberAnser : answer for number type quesiton
    qtol : tolerance for number type question
    qpoints : points of this question
    """
    qname = models.CharField(max_length=20)
    qtitle = models.CharField(max_length=800)
    qtype = models.CharField(max_length=20, default='number')
    choiceAnswer = models.CharField(max_length=300, default="first")
    numberAnswer = models.FloatField(default=0)
    qtol = models.FloatField(default=0.001)
    qpoints = models.FloatField()

    def __str__(self):
        return self.qname


class Hw2_submit(models.Model):
    email = models.EmailField(max_length=300)
    time = models.DateTimeField()
    hasGraded = models.BooleanField(default=False)
    
    q1 = models.FloatField(blank=True, null=True)
    q2 = models.CharField(blank=True, max_length=500)
    q3 = models.CharField(blank=True, max_length=500)
    q4 = models.FloatField(blank=True, null=True)
    q5 = models.CharField(blank=True, max_length=500)

    g1 = models.FloatField(blank=True, default=0)
    g2 = models.FloatField(blank=True, default=0)
    g3 = models.FloatField(blank=True, default=0)
    g4 = models.FloatField(blank=True, default=0)
    g5 = models.FloatField(blank=True, default=0)
    gs = models.FloatField(blank=True, default=0)    # total points
    gf = models.FloatField(blank=True, default=0)    # full points
    gp = models.FloatField(blank=True, default=0)    # percentage

    def __str__(self):
        return self.email


class Hw2_key(models.Model):
    qname = models.CharField(max_length=20)
    qtitle = models.CharField(max_length=800)
    qtype = models.CharField(max_length=20, default='number')
    choiceAnswer = models.CharField(max_length=300, default="first")
    numberAnswer = models.FloatField(default=0)
    qtol = models.FloatField(default=0.001)
    qpoints = models.FloatField()

    def __str__(self):
        return self.qname


class Hw3_submit(models.Model):
    email = models.EmailField(max_length=300)
    time = models.DateTimeField()
    hasGraded = models.BooleanField(default=False)

    q1 = models.FloatField(blank=True, null=True)
    q2 = models.FloatField(blank=True, null=True)
    q3 = models.FloatField(blank=True, null=True)

    g1 = models.FloatField(blank=True, default=0)
    g2 = models.FloatField(blank=True, default=0)
    g3 = models.FloatField(blank=True, default=0)
    gs = models.FloatField(blank=True, default=0)    # total points
    gf = models.FloatField(blank=True, default=0)    # full points
    gp = models.FloatField(blank=True, default=0)    # percentage

    def __str__(self):
        return self.email


class Hw3_key(models.Model):
    qname = models.CharField(max_length=20)
    qtitle = models.CharField(max_length=800)
    qtype = models.CharField(max_length=20, default='number')
    choiceAnswer = models.CharField(max_length=300, default="first")
    numberAnswer = models.FloatField(default=0)
    qtol = models.FloatField(default=0.001)
    qpoints = models.FloatField()

    def __str__(self):
        return self.qname


class Hw4_submit(models.Model):
    email = models.EmailField(max_length=300)
    time = models.DateTimeField()
    hasGraded = models.BooleanField(default=False)

    q1 = models.CharField(blank=True, max_length=500)
    q2 = models.CharField(blank=True, max_length=500)
    q3 = models.FloatField(blank=True, null=True)
    q4 = models.FloatField(blank=True, null=True)
    q5 = models.CharField(blank=True, max_length=500)

    g1 = models.FloatField(blank=True, default=0)
    g2 = models.FloatField(blank=True, default=0)
    g3 = models.FloatField(blank=True, default=0)
    g4 = models.FloatField(blank=True, default=0)
    g5 = models.FloatField(blank=True, default=0)
    gs = models.FloatField(blank=True, default=0)    # total points
    gf = models.FloatField(blank=True, default=0)    # full points
    gp = models.FloatField(blank=True, default=0)    # percentage

    def __str__(self):
        return self.email


class Hw4_key(models.Model):
    qname = models.CharField(max_length=20)
    qtitle = models.CharField(max_length=800)
    qtype = models.CharField(max_length=20, default='number')
    choiceAnswer = models.CharField(max_length=300, default="first")
    numberAnswer = models.FloatField(default=0)
    qtol = models.FloatField(default=0.001)
    qpoints = models.FloatField()

    def __str__(self):
        return self.qname
    

class Hw5_submit(models.Model):
    email = models.EmailField(max_length=300)
    time = models.DateTimeField()
    hasGraded = models.BooleanField(default=False)

    q1 = models.CharField(blank=True, max_length=500)
    q2 = models.CharField(blank=True, max_length=500)
    q3 = models.FloatField(blank=True, null=True)
    q4 = models.FloatField(blank=True, null=True)
    q5 = models.CharField(blank=True, max_length=500)

    g1 = models.FloatField(blank=True, default=0)
    g2 = models.FloatField(blank=True, default=0)
    g3 = models.FloatField(blank=True, default=0)
    g4 = models.FloatField(blank=True, default=0)
    g5 = models.FloatField(blank=True, default=0)
    gs = models.FloatField(blank=True, default=0)    # total points
    gf = models.FloatField(blank=True, default=0)    # full points
    gp = models.FloatField(blank=True, default=0)    # percentage

    def __str__(self):
        return self.email


class Hw5_key(models.Model):
    qname = models.CharField(max_length=20)
    qtitle = models.CharField(max_length=800)
    qtype = models.CharField(max_length=20, default='number')
    choiceAnswer = models.CharField(max_length=300, default="first")
    numberAnswer = models.FloatField(default=0)
    qtol = models.FloatField(default=0.001)
    qpoints = models.FloatField()

    def __str__(self):
        return self.qname


class Hw6_submit(models.Model):
    email = models.EmailField(max_length=300)
    time = models.DateTimeField()
    hasGraded = models.BooleanField(default=False)

    q1 = models.CharField(blank=True, max_length=500)
    q2 = models.CharField(blank=True, max_length=500)
    q3 = models.FloatField(blank=True, null=True)
    q4 = models.FloatField(blank=True, null=True)
    q5 = models.CharField(blank=True, max_length=500)

    g1 = models.FloatField(blank=True, default=0)
    g2 = models.FloatField(blank=True, default=0)
    g3 = models.FloatField(blank=True, default=0)
    g4 = models.FloatField(blank=True, default=0)
    g5 = models.FloatField(blank=True, default=0)
    gs = models.FloatField(blank=True, default=0)    # total points
    gf = models.FloatField(blank=True, default=0)    # full points
    gp = models.FloatField(blank=True, default=0)    # percentage

    def __str__(self):
        return self.email


class Hw6_key(models.Model):
    qname = models.CharField(max_length=20)
    qtitle = models.CharField(max_length=800)
    qtype = models.CharField(max_length=20, default='number')
    choiceAnswer = models.CharField(max_length=300, default="first")
    numberAnswer = models.FloatField(default=0)
    qtol = models.FloatField(default=0.001)
    qpoints = models.FloatField()

    def __str__(self):
        return self.qname


class Hw7_submit(models.Model):
    email = models.EmailField(max_length=300)
    time = models.DateTimeField()
    hasGraded = models.BooleanField(default=False)

    q1 = models.FloatField(blank=True, null=True)
    q2 = models.CharField(blank=True, max_length=500)
    q3 = models.FloatField(blank=True, null=True)
    q4 = models.FloatField(blank=True, null=True)

    g1 = models.FloatField(blank=True, default=0)
    g2 = models.FloatField(blank=True, default=0)
    g3 = models.FloatField(blank=True, default=0)
    g4 = models.FloatField(blank=True, default=0)
    gs = models.FloatField(blank=True, default=0)    # total points
    gf = models.FloatField(blank=True, default=0)    # full points
    gp = models.FloatField(blank=True, default=0)    # percentage

    def __str__(self):
        return self.email


class Hw7_key(models.Model):
    qname = models.CharField(max_length=20)
    qtitle = models.CharField(max_length=800)
    qtype = models.CharField(max_length=20, default='number')
    choiceAnswer = models.CharField(max_length=300, default="first")
    numberAnswer = models.FloatField(default=0)
    qtol = models.FloatField(default=0.001)
    qpoints = models.FloatField()

    def __str__(self):
        return self.qname


class Hw8_submit(models.Model):
    email = models.EmailField(max_length=300)
    time = models.DateTimeField()
    hasGraded = models.BooleanField(default=False)
    
    q1 = models.FloatField(blank=True, null=True)
    q2 = models.FloatField(blank=True, null=True)

    g1 = models.FloatField(blank=True, default=0)
    g2 = models.FloatField(blank=True, default=0)
    gs = models.FloatField(blank=True, default=0)    # total points
    gf = models.FloatField(blank=True, default=0)    # full points
    gp = models.FloatField(blank=True, default=0)    # percentage

    def __str__(self):
        return self.email


class Hw8_key(models.Model):
    qname = models.CharField(max_length=20)
    qtitle = models.CharField(max_length=800)
    qtype = models.CharField(max_length=20, default='number')
    choiceAnswer = models.CharField(max_length=300, default="first")
    numberAnswer = models.FloatField(default=0)
    qtol = models.FloatField(default=0.001)
    qpoints = models.FloatField()

    def __str__(self):
        return self.qname


class Hw9_submit(models.Model):
    email = models.EmailField(max_length=300)
    time = models.DateTimeField()
    hasGraded = models.BooleanField(default=False)

    q1 = models.FloatField(blank=True, null=True)
    q2 = models.FloatField(blank=True, null=True)
    q3 = models.FloatField(blank=True, null=True)
    q4 = models.FloatField(blank=True, null=True)
    q5 = models.FloatField(blank=True, null=True)

    g1 = models.FloatField(blank=True, default=0)
    g2 = models.FloatField(blank=True, default=0)
    g3 = models.FloatField(blank=True, default=0)
    g4 = models.FloatField(blank=True, default=0)
    g5 = models.FloatField(blank=True, default=0)
    gs = models.FloatField(blank=True, default=0)    # total points
    gf = models.FloatField(blank=True, default=0)    # full points
    gp = models.FloatField(blank=True, default=0)    # percentage

    def __str__(self):
        return self.email


class Hw9_key(models.Model):
    qname = models.CharField(max_length=20)
    qtitle = models.CharField(max_length=800)
    qtype = models.CharField(max_length=20, default='number')
    choiceAnswer = models.CharField(max_length=300, default="first")
    numberAnswer = models.FloatField(default=0)
    qtol = models.FloatField(default=0.001)
    qpoints = models.FloatField()

    def __str__(self):
        return self.qname


class Hw10_submit(models.Model):
    email = models.EmailField(max_length=300)
    time = models.DateTimeField()
    hasGraded = models.BooleanField(default=False)

    q1 = models.FloatField(blank=True, null=True)
    q2 = models.FloatField(blank=True, null=True)
    q3 = models.FloatField(blank=True, null=True)
    q4 = models.FloatField(blank=True, null=True)

    g1 = models.FloatField(blank=True, default=0)
    g2 = models.FloatField(blank=True, default=0)
    g3 = models.FloatField(blank=True, default=0)
    g4 = models.FloatField(blank=True, default=0)
    gs = models.FloatField(blank=True, default=0)    # total points
    gf = models.FloatField(blank=True, default=0)    # full points
    gp = models.FloatField(blank=True, default=0)    # percentage

    def __str__(self):
        return self.email


class Hw10_key(models.Model):
    qname = models.CharField(max_length=20)
    qtitle = models.CharField(max_length=800)
    qtype = models.CharField(max_length=20, default='number')
    choiceAnswer = models.CharField(max_length=300, default="first")
    numberAnswer = models.FloatField(default=0)
    qtol = models.FloatField(default=0.001)
    qpoints = models.FloatField()

    def __str__(self):
        return self.qname


class Hw11_submit(models.Model):
    email = models.EmailField(max_length=300)
    time = models.DateTimeField()
    hasGraded = models.BooleanField(default=False)

    q1 = models.FloatField(blank=True, null=True)
    q2 = models.FloatField(blank=True, null=True)

    g1 = models.FloatField(blank=True, default=0)
    g2 = models.FloatField(blank=True, default=0)
    gs = models.FloatField(blank=True, default=0)    # total points
    gf = models.FloatField(blank=True, default=0)    # full points
    gp = models.FloatField(blank=True, default=0)    # percentage

    def __str__(self):
        return self.email


class Hw11_key(models.Model):
    qname = models.CharField(max_length=20)
    qtitle = models.CharField(max_length=800)
    qtype = models.CharField(max_length=20, default='number')
    choiceAnswer = models.CharField(max_length=300, default="first")
    numberAnswer = models.FloatField(default=0)
    qtol = models.FloatField(default=0.001)
    qpoints = models.FloatField()

    def __str__(self):
        return self.qname


class Hw12_submit(models.Model):
    email = models.EmailField(max_length=300)
    time = models.DateTimeField()
    hasGraded = models.BooleanField(default=False)

    q1 = models.FloatField(blank=True, null=True)
    q2 = models.FloatField(blank=True, null=True)
    q3 = models.FloatField(blank=True, null=True)
    q4 = models.FloatField(blank=True, null=True)

    g1 = models.FloatField(blank=True, default=0)
    g2 = models.FloatField(blank=True, default=0)
    g3 = models.FloatField(blank=True, default=0)
    g4 = models.FloatField(blank=True, default=0)
    gs = models.FloatField(blank=True, default=0)    # total points
    gf = models.FloatField(blank=True, default=0)    # full points
    gp = models.FloatField(blank=True, default=0)    # percentage

    def __str__(self):
        return self.email


class Hw12_key(models.Model):
    qname = models.CharField(max_length=20)
    qtitle = models.CharField(max_length=800)
    qtype = models.CharField(max_length=20, default='number')
    choiceAnswer = models.CharField(max_length=300, default="first")
    numberAnswer = models.FloatField(default=0)
    qtol = models.FloatField(default=0.001)
    qpoints = models.FloatField()

    def __str__(self):
        return self.qname


class Hw13_submit(models.Model):
    email = models.EmailField(max_length=300)
    time = models.DateTimeField()
    hasGraded = models.BooleanField(default=False)

    q1 = models.FloatField(blank=True, null=True)
    q2 = models.FloatField(blank=True, null=True)
    q3 = models.FloatField(blank=True, null=True)
    q4 = models.FloatField(blank=True, null=True)

    g1 = models.FloatField(blank=True, default=0)
    g2 = models.FloatField(blank=True, default=0)
    g3 = models.FloatField(blank=True, default=0)
    g4 = models.FloatField(blank=True, default=0)
    gs = models.FloatField(blank=True, default=0)    # total points
    gf = models.FloatField(blank=True, default=0)    # full points
    gp = models.FloatField(blank=True, default=0)    # percentage

    def __str__(self):
        return self.email


class Hw13_key(models.Model):
    qname = models.CharField(max_length=20)
    qtitle = models.CharField(max_length=800)
    qtype = models.CharField(max_length=20, default='number')
    choiceAnswer = models.CharField(max_length=300, default="first")
    numberAnswer = models.FloatField(default=0)
    qtol = models.FloatField(default=0.001)
    qpoints = models.FloatField()

    def __str__(self):
        return self.qname


class Hw14_submit(models.Model):
    email = models.EmailField(max_length=300)
    time = models.DateTimeField()
    hasGraded = models.BooleanField(default=False)

    q1 = models.FloatField(blank=True, null=True)
    q2 = models.FloatField(blank=True, null=True)
    q3 = models.CharField(blank=True, max_length=500)

    g1 = models.FloatField(blank=True, default=0)
    g2 = models.FloatField(blank=True, default=0)
    g3 = models.FloatField(blank=True, default=0)
    gs = models.FloatField(blank=True, default=0)    # total points
    gf = models.FloatField(blank=True, default=0)    # full points
    gp = models.FloatField(blank=True, default=0)    # percentage

    def __str__(self):
        return self.email


class Hw14_key(models.Model):
    qname = models.CharField(max_length=20)
    qtitle = models.CharField(max_length=800)
    qtype = models.CharField(max_length=20, default='number')
    choiceAnswer = models.CharField(max_length=300, default="first")
    numberAnswer = models.FloatField(default=0)
    qtol = models.FloatField(default=0.001)
    qpoints = models.FloatField()

    def __str__(self):
        return self.qname


class Hw15_submit(models.Model):
    email = models.EmailField(max_length=300)
    time = models.DateTimeField()
    hasGraded = models.BooleanField(default=False)

    q1 = models.CharField(blank=True, max_length=500)
    q2 = models.CharField(blank=True, max_length=500)

    g1 = models.FloatField(blank=True, default=0)
    g2 = models.FloatField(blank=True, default=0)
    gs = models.FloatField(blank=True, default=0)    # total points
    gf = models.FloatField(blank=True, default=0)    # full points
    gp = models.FloatField(blank=True, default=0)    # percentage

    def __str__(self):
        return self.email


class Hw15_key(models.Model):
    qname = models.CharField(max_length=20)
    qtitle = models.CharField(max_length=800)
    qtype = models.CharField(max_length=20, default='number')
    choiceAnswer = models.CharField(max_length=300, default="first")
    numberAnswer = models.FloatField(default=0)
    qtol = models.FloatField(default=0.001)
    qpoints = models.FloatField()

    def __str__(self):
        return self.qname


class Hw16_submit(models.Model):
    email = models.EmailField(max_length=300)
    time = models.DateTimeField()
    hasGraded = models.BooleanField(default=False)

    q1 = models.FloatField(blank=True, null=True)
    q2 = models.FloatField(blank=True, null=True)
    q3 = models.FloatField(blank=True, null=True)

    g1 = models.FloatField(blank=True, default=0)
    g2 = models.FloatField(blank=True, default=0)
    g3 = models.FloatField(blank=True, default=0)
    gs = models.FloatField(blank=True, default=0)    # total points
    gf = models.FloatField(blank=True, default=0)    # full points
    gp = models.FloatField(blank=True, default=0)    # percentage

    def __str__(self):
        return self.email


class Hw16_key(models.Model):
    qname = models.CharField(max_length=20)
    qtitle = models.CharField(max_length=800)
    qtype = models.CharField(max_length=20, default='number')
    choiceAnswer = models.CharField(max_length=300, default="first")
    numberAnswer = models.FloatField(default=0)
    qtol = models.FloatField(default=0.001)
    qpoints = models.FloatField()

    def __str__(self):
        return self.qname
