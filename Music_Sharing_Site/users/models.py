from __future__ import unicode_literals
#
from django.contrib.auth.models import User
from django.db import models


class Friend(models.Model):
    follower = models.ForeignKey(User, related_name="followees",on_delete=models.CASCADE) 
    #It establishes a relationship between the Friend model and the User model. It means that a Friend instance will have a single follower who is a User.
    #The on_delete=models.CASCADE specifies that if the related User is deleted, the Friend instance will also be deleted. 
    #The related_name attribute specifies the reverse relationship name from User to Friend.
    followee = models.ForeignKey(User, related_name="followers",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    #The auto_now_add=True attribute automatically sets the field's value to the current date and time when a new Friend instance is created.
    updated_at = models.DateTimeField(auto_now=True)