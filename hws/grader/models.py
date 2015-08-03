from django.db import models


class Hw1_submit(models.Model):
    email = models.EmailField(max_length=300)
    time = models.DateTimeField()
    hasGraded = models.BooleanField(default=False)
    
    q1 = models.CharField(max_length=500)
    q2 = models.FloatField()
    q3 = models.FloatField()
    q4 = models.FloatField()
    q5 = models.FloatField()

    g1 = models.FloatField()
    g2 = models.FloatField()
    g3 = models.FloatField()
    g4 = models.FloatField()
    g5 = models.FloatField()

    def __str__(self):
        return self.email


class Hw1_key(models.Model):
    q1 = models.CharField(max_length=500)
    q2 = models.FloatField()
    q3 = models.FloatField()
    q4 = models.FloatField()
    q5 = models.FloatField()
    

class Hw2_submit(models.Model):
    email = models.EmailField(max_length=300)
    time = models.DateTimeField()
    hasGraded = models.BooleanField(default=False)
    
    q1 = models.FloatField()
    q2 = models.CharField(max_length=500)
    q3 = models.CharField(max_length=500)
    q4 = models.FloatField()
    q5 = models.CharField(max_length=500)

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
    # name of the question
    qname = models.CharField(max_length=20)
    # title of the question
    qtitle = models.CharField(max_length=800)
    # type of the question. only 'number' or 'choice'
    qtype = models.CharField(max_length=20, default='number')
    # answer for choice type question
    choiceAnswer = models.CharField(max_length=300, default="first")
    # answer for number type quesiton
    numberAnswer = models.FloatField(default=0)
    # tolerance for number type question
    qtol = models.FloatField(default=0.001)
    # points of this question
    qpoints = models.FloatField()

    def __str__(self):
        return self.qname
    
