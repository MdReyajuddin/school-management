from django.db import models

# Create your models here.
class Students(models.Model):
    name                =       models.CharField(max_length=664, null=True)
    email               =       models.EmailField(null=True)
    admission_no        =       models.IntegerField(null=True)
    contact_no          =       models.CharField(max_length=12, unique=True, null=True)
    father_name         =       models.CharField(max_length=664, null=True)
    mother_name         =       models.CharField(max_length=664, null=True)
    parent_email        =       models.EmailField(null=True)
    parent_contact_no   =       models.CharField(max_length=612, null=True)
    blood_group         =       models.CharField(max_length=620, default="B", null=True, choices=(('A', 'A'), ('B', 'B'), ('O', 'O'), ('AB', 'AB')))
    category            =       models.CharField(max_length=620, null=True, default="math",choices=(('science', 'science'), ('math', 'math'), ('biology', 'biology'), ('physics', 'physics'), ('chemistry', 'chemistry')))
    religion            =       models.CharField(max_length=600, null=True, default="hindu", choices=(('hindu', 'hindu'), ('muslim', 'muslim'), ('christian', 'christian'), ('other', 'other')))
    pincode             =       models.CharField(max_length=6, null=True)
    classes             =       models.CharField(max_length=600, null=True, default="1", choices=(('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')))
    section             =       models.CharField(max_length=600, null=True, default="A", choices=(('A', 'A'), ('B', 'B'), ('C', 'C'),('D', 'D')))
    address             =       models.TextField(null=True)
    permanent_address   =       models.TextField(null=True)
    pic                 =       models.FileField(null=True,blank=True)

    def __str__(self):
        return self.name

class Index(models.Model):
    school_name                 =       models.CharField(max_length=664, null=True)
    school_code                 =       models.CharField(max_length=664, null=True)
    user_name                   =       models.CharField(max_length=664, null=True)
    login_id                    =       models.CharField(max_length=664, null=True)
    contact_no                  =       models.CharField (max_length=12, unique=True, null=True)
    school_email                =       models.EmailField(null=True)
    alternative_school_email    =       models.EmailField(null=True)
    address                     =       models.TextField(null=True)
    pincode                     =       models.CharField(max_length=6, null=True,blank=True)


class Contact(models.Model):
    name        =       models.CharField(max_length=664, null=True)
    contact_no  =       models.CharField (max_length=12, unique=True, null=True)
    email       =       models.EmailField(null=True)
    msg         =       models.TextField(null=True,)


class Staffs(models.Model):
    name        =       models.CharField(max_length=64)

class Departments(models.Model):
    name        =       models.CharField(max_length=64)

class Classes(models.Model):
    name        =       models.CharField(max_length=64)
