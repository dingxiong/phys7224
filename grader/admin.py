from django.contrib import admin
from .models import *


class Hw_submit_Admin(admin.ModelAdmin):
    list_display = ('email', 'gs', 'gf', 'gp', 'time')


class Hw_key_Admin(admin.ModelAdmin):
    list_display = ('qname', 'qtype', 'choiceAnswer',
                    'numberAnswer', 'qtol', 'qpoints')

admin.site.register(Hw1_submit, Hw_submit_Admin)
admin.site.register(Hw1_key,  Hw_key_Admin)

admin.site.register(Hw2_submit, Hw_submit_Admin)
admin.site.register(Hw2_key, Hw_key_Admin)

admin.site.register(Hw3_submit, Hw_submit_Admin)
admin.site.register(Hw3_key, Hw_key_Admin)

admin.site.register(Hw4_submit, Hw_submit_Admin)
admin.site.register(Hw4_key, Hw_key_Admin)

admin.site.register(Hw5_submit, Hw_submit_Admin)
admin.site.register(Hw5_key, Hw_key_Admin)

admin.site.register(Hw6_submit, Hw_submit_Admin)
admin.site.register(Hw6_key, Hw_key_Admin)

admin.site.register(Hw7_submit, Hw_submit_Admin)
admin.site.register(Hw7_key, Hw_key_Admin)

admin.site.register(Hw8_submit, Hw_submit_Admin)
admin.site.register(Hw8_key, Hw_key_Admin)

admin.site.register(Hw9_submit, Hw_submit_Admin)
admin.site.register(Hw9_key, Hw_key_Admin)

admin.site.register(Hw10_submit, Hw_submit_Admin)
admin.site.register(Hw10_key, Hw_key_Admin)

admin.site.register(Hw11_submit, Hw_submit_Admin)
admin.site.register(Hw11_key, Hw_key_Admin)

admin.site.register(Hw12_submit, Hw_submit_Admin)
admin.site.register(Hw12_key, Hw_key_Admin)

admin.site.register(Hw13_submit, Hw_submit_Admin)
admin.site.register(Hw13_key, Hw_key_Admin)

admin.site.register(Hw14_submit, Hw_submit_Admin)
admin.site.register(Hw14_key, Hw_key_Admin)

admin.site.register(Hw15_submit, Hw_submit_Admin)
admin.site.register(Hw15_key, Hw_key_Admin)

admin.site.register(Hw16_submit, Hw_submit_Admin)
admin.site.register(Hw16_key, Hw_key_Admin)
