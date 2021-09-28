from django.contrib import admin
from .models import Person, Medic, Direction, Cite, Diagnosis, Diet, Allergy, Record, Laboratory
# Register your models here.
admin.site.register(Person)
admin.site.register(Medic)
admin.site.register(Direction)
admin.site.register(Cite)
admin.site.register(Diagnosis)
admin.site.register(Diet)
admin.site.register(Allergy)
admin.site.register(Record)
admin.site.register(Laboratory)