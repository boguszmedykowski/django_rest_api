from django.contrib import admin
from .models import Exercise, Workout


# @admin.register(Exercise)
# class ExerciseAdmin(admin.ModelAdmin):
#     list_display = ('title', 'id', 'author')


admin.site.register(Exercise)
admin.site.register(Workout)




