# - * - mode: python; coding: utf-8 - * 

from django.contrib import admin
from admin_db.models import Kurs_Work, Tags, Predmets, Grupps

admin.site.register(Kurs_Work)
admin.site.register(Tags)
admin.site.register(Predmets)
admin.site.register(Grupps)
