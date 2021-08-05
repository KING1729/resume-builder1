from django.db import models

# Create your models here.
class Details(models.Model):
    username = models.CharField(max_length=50)
    personName = models.CharField(max_length=100)
    jobTitle = models.TextField()
    email = models.EmailField()
    website = models.URLField()
    linkedIn = models.URLField()
    phoneNumber = models.CharField(max_length=20)

    personalProfile=models.TextField()

    company1=models.CharField(max_length=100)
    role1=models.CharField(max_length=100)
    company1startdate=models.CharField(max_length=50)
    company1enddate=models.CharField(max_length=50)
    jobDescription1 = models.TextField(max_length=200)

    company2 = models.CharField(max_length=100)
    role2 = models.CharField(max_length=100)
    company2startdate = models.CharField(max_length=50)
    company2enddate = models.CharField(max_length=50)
    jobDescription2 = models.TextField(max_length=200)

    skill1 = models.CharField(max_length=50)
    skill2 = models.CharField(max_length=50)
    skill3 = models.CharField(max_length=50)
    skill4 = models.CharField(max_length=50)
    skill5 = models.CharField(max_length=50)
    skill6 = models.CharField(max_length=50)

    collegeName1 = models.CharField(max_length=100)
    degree1=models.CharField(max_length=100)
    college1startdate = models.CharField(max_length=50)
    college1enddate = models.CharField(max_length=50)
    cgpa1 = models.FloatField()

    collegeName2 = models.CharField(max_length=100)
    degree2 = models.CharField(max_length=100)
    college2startdate = models.CharField(max_length=50)
    college2enddate = models.CharField(max_length=50)
    cgpa2 = models.FloatField()

    project1 = models.CharField(max_length=100)
    projectDescription1=models.TextField()
    project2 = models.CharField(max_length=100)
    projectDescription2 = models.TextField()

    def __str__(self):
        return self.username
