from django.contrib import admin

from .models import Question, Dataset, Submission

admin.site.register(Question)
admin.site.register(Dataset)
admin.site.register(Submission)