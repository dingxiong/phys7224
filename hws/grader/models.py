from django.db import models


class hw1_submit(models.Model):
    email = models.EmailField(max_length=300)
    time = models.DateTimeField()
    hasGraded = models.BooleanField(default=False)
    q1 = models.DecimalField()
    q2 = models.FloatField()
    q3 = models.FloatField()
    q4 = models.FloatField()
    q5 = models.FloatField()



