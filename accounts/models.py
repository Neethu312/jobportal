from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser,PermissionsMixin

# Create your models here.


class CustomUserManger(BaseUserManager):
    def create_user(self, username=None, password=None, **extra_fields):
        if not username:
            raise ValueError("User must have a Username")
        if not password:
            raise ValueError('User must have a Password')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 1)
        return self.create_user(username, password, **extra_fields)


ROLE_CHOICE = [
    (1, 'Admin'),
    (2, 'Company'),
    (3, 'Applicant')
]


class CustomUser(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name='active')
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    role = models.IntegerField(choices=ROLE_CHOICE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = CustomUserManger()

    def _str_(self):
        return self.username


class CompanyProfile(models.Model):
    fk_company = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    company_name = models.CharField(max_length=100)
    profile = models.ImageField(upload_to='Company_Profile/')
    description = models.TextField(null=True)
    location = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    website = models.URLField()
    industry = models.CharField(max_length=100)
    hr_name = models.CharField(max_length=200)


class ApplicantProfile(models.Model):
    GENDER_CHOICES = [
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('OTHERS', 'Others'),
    ]

    MARITAL_STATUS_CHOICES = [
        ('SINGLE', 'Single'),
        ('MARRIED', 'Married'),
        ('DIVORCED', 'Divorced'),
        ('WIDOWED', 'Widowed'),
    ]

    WORK_STATUS_CHOICES = [
        ('Experienced', 'I have work experience'),
        ('Fresher', 'I am a fresher'),
    ]

    fk_user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    photo = models.ImageField(upload_to='Profile_Photo/')
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    marital_status = models.CharField(max_length=50, choices=MARITAL_STATUS_CHOICES)
    dob = models.DateField()
    address = models.TextField()
    phone = models.CharField(max_length=12)
    work_status = models.CharField(max_length=100, choices=WORK_STATUS_CHOICES)
    Proof_of_citizenship = models.ImageField(upload_to='id_proof/')
