from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Post


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','password1','password2']

class PostForm(ModelForm):
   class Meta:
      model = Post
      fields = ['post_id','post_title','heading','content','pub_date']
