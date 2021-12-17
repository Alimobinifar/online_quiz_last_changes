from django.db import models

# Create your models here.



class Cat(models.Model):
    cat=models.CharField(max_length=100)
    
    def __str__(self):
        return self.cat

class Questions(models.Model):
    title=models.CharField(max_length=500)
    cat=models.ForeignKey(Cat,related_name='question', on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.title

class Answers(models.Model):
    title=models.CharField(max_length=120)
    question=models.ForeignKey(Questions,related_name='answer', on_delete=models.CASCADE)
    is_correct=models.BooleanField(default=False)

    def __str__(self):
        return self.title

class User(models.Model):
    user_name=models.CharField(max_length=250)
    phone_number=models.CharField(max_length=11)

class User_answers(models.Model): #one to many 
    user=models.ForeignKey(User,related_name='user', on_delete=models.CASCADE)
    question=models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer=models.ForeignKey(Answers,on_delete=models.CASCADE)
    result=models.CharField(max_length=15)

class reportـcard(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    score=models.IntegerField(max_length=3)




