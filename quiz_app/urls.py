
from django.urls import path
from quiz_app.views import show_questions,show_result

urlpatterns = [
    path('show_result/<int:id>',show_result),
    path('show_test/<int:id>',show_questions)
]