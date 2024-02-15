# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Store(models.Model):

    #__Store_FIELDS__
    storeid = models.CharField(max_length=255, null=True, blank=True)
    storename = models.CharField(max_length=255, null=True, blank=True)

    #__Store_FIELDS__END

    class Meta:
        verbose_name        = _("Store")
        verbose_name_plural = _("Store")


class Appuser(models.Model):

    #__Appuser_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    employeeid = models.CharField(max_length=255, null=True, blank=True)
    role = models.CharField(max_length=255, null=True, blank=True)

    #__Appuser_FIELDS__END

    class Meta:
        verbose_name        = _("Appuser")
        verbose_name_plural = _("Appuser")



#__MODELS__END
