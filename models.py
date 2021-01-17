from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.signals import user_logged_in

# Create your models here.
class Post(models.Model):
   post_id =models.AutoField(primary_key = True,null=False)
   post_title = models.CharField(max_length=60,default="")
   heading = models.CharField(max_length=100,default="")
   content = models.CharField(max_length=1000,default="")
   pub_date = models.DateField()
   thumbnail= models.ImageField(default="",null=True)
   user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
   likes = models.ManyToManyField(User,related_name="post_likes")
   updated = models.DateTimeField(auto_now=True)




   def __str__(self):
     return self.post_title

   @property
   def num_likes(self):
      return self.likes.all().count()

LIKE_CHOICES = (
   ('Like','Like'),
   ('Unlike','Unlike'),
)

class Like(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   post = models.ForeignKey(Post, on_delete=models.CASCADE)
   value = models.CharField(choices=LIKE_CHOICES,default='Like', max_length=10)


   def __str__(self):
      return str(self.post)

class Comment(models.Model):
   post = models.ForeignKey(Post,related_name='comments', on_delete=models.CASCADE)
   name = models.CharField(max_length=100)
   body = models.TextField()
   date_added = models.DateTimeField(auto_now=True)


   def __str__(self):
      return '%s - %s'% (self.post.title,self.name)



class ProfileEdit(models.Model):
   education = models.CharField(max_length=100,null=False)
   stream = models.CharField(max_length=100,null=False)
   company = models.CharField(max_length=200,null=True,default=" ")
   current_position = models.CharField(max_length=200,null=True,default=" ")
   country = models.CharField(max_length=100,null=True,default=" ")
   location = models.CharField(max_length=150,null=True,default=" ")
   experience = models.CharField(max_length=100,null=True,default="Fresher")
   skills = models.CharField(max_length=500,null=False,default=" ")
   interests = models.CharField(max_length=100,null=False,default=" ")
   contact = models.CharField(max_length=100,null=True,default=" ")
   user = models.OneToOneField(User, on_delete=models.CASCADE,default= 1)
   login_count = models.PositiveIntegerField(default=0)



   def __str__(self):
      return str(self.user)

   def login_user(sender, request, user, **kwargs):
      user.profileedit.login_count = user.profileedit.login_count + 1
      user.profileedit.save()

   user_logged_in.connect(login_user)

class Status(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   status_value = models.BooleanField(default=False)



   def __str__(self):
      return str(self.status_value)