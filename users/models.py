from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.urls import reverse


class CustomUserManager(BaseUserManager):
  def _create_user(self, email, password, **extra_fields):
    """
    Cria e salva um usuário com o email e senha fornecidos.
    """
    if not email:
        raise ValueError("O campo de email deve ser preenchido.")
    email = self.normalize_email(email)
    user = self.model(email=email, **extra_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, email, password=None, **extra_fields):
    extra_fields.setdefault("is_staff", False)
    extra_fields.setdefault("is_superuser", False)
    return self._create_user(email, password, **extra_fields)

  def create_superuser(self, email, password=None, **extra_fields):
    extra_fields.setdefault("is_staff", True)
    extra_fields.setdefault("is_superuser", True)

    if extra_fields.get("is_staff") is not True:
        raise ValueError("O superusuário deve ter is_staff=True.")
    if extra_fields.get("is_superuser") is not True:
        raise ValueError("O superusuário deve ter is_superuser=True.")

    return self._create_user(email, password, **extra_fields)

# Create your models here.
class CustomUser(AbstractUser):

  USERNAME_FIELD = "email"
  REQUIRED_FIELDS = []
  email = models.EmailField(unique=True)
  objects = CustomUserManager()

  @property
  def name(self):
      return "{} {}".format(self.first_name, self.last_name)

  class Meta:
      verbose_name = ("user")
      verbose_name_plural = ("users")
      db_table = "users"

  def __str__(self):
      return self.name

  def get_absolute_url(self):
      return reverse("CustomUser_detail", kwargs={"pk": self.pk})
