from django.contrib import admin


from .models import Questions ,Cat , Answers,Exsam

admin.site.register(Exsam)

@admin.register(Cat)
class Cat_admin(admin.ModelAdmin):
    pass

@admin.register(Answers)
class Answers_admin(admin.ModelAdmin):
    pass

@admin.register(Questions)
class Question_admin(admin.ModelAdmin):
    pass
