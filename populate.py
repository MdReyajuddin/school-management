import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'schoolmanagement.settings')
django.setup()

from faker import Faker
from random import *
from django.utils import timezone
from django.contrib.auth.models import User
from schooladmin.models import Students

def populate(n):
    fake = Faker()
    for _ in range(n):
        fname = fake.name()
        fadmission_no = fake.random_number(5)
        femail = fake.email()
        fcontact_no = fake.phone_number()
        ffather_name = fake.name()
        fmother_name = fake.name()
        fparent_email = fake.email()
        fparent_contact_no = fake.phone_number()
        fblood_group = fake.random_element(elements=('A', 'B', 'C', 'D'))
        fcategory = fake.random_element(elements=('math', 'science', 'biology', 'physics', 'chemistry'))
        freligion = fake.random_element(elements=('muslim', 'hindu', 'christian', 'other'))
        fpincode = fake.postalcode()
        faddress = fake.address()
        fpermanent_address = fake.city()
        fsection = fake.random_element(elements=('A', 'B', 'C', 'D'))
        fclasses = fake.random_element(elements=('1', '2', '3', '4', '5', '6', '7', '8', '9'))
        fpic = fake.file_name()

        create_post =Students.objects.get_or_create(name=fname,admission_no=fadmission_no,email=femail,contact_no=fcontact_no,father_name=ffather_name,mother_name=fmother_name ,parent_email=fparent_email,parent_contact_no=fparent_contact_no,blood_group=fblood_group,category=fcategory, religion=freligion,pincode=fpincode,address=faddress,permanent_address=fpermanent_address,section=fsection,classes=fclasses,pic=fpic)

populate(30)