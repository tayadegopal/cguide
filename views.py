from django.shortcuts import render,redirect,get_object_or_404,reverse
from django.http import HttpResponseRedirect

from django.contrib.auth import authenticate ,login ,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm,PostForm
from .models import Post,Like,Comment,ProfileEdit




# Create your views here.



def index(request):
    posts = Post.objects.all()
    user = request.user
    #pro = ProfileEdit.objects.get(user_id=user)

    context = {'posts': posts,
               'user': user,
     #          'pro': pro,

               }

    return render(request,'index/index.html',context)
def home(request):
    posts = Post.objects.all()
    user = request.user
    pro = ProfileEdit.objects.get(user_id=user)

    context = {'posts': posts,
               'user': user,
               'pro': pro,
               }

    return render(request,'index/index.html',context)

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form_saved = form.save()
            if form_saved:
              return redirect('login')
    context = {'form': form}
    return render(request, "register.html", context)

def loginPage(request):
    if request.user.is_authenticated:
        print("user is authenticated")
        posts = Post.objects.all()
        user = request.user
        last= request.user.last_login
        print(last)

        pro = ProfileEdit.objects.get(user_id=user)
        print(pro)
        context = {'posts': posts,
                   'user': user,
                   'pro': pro,

                   }

        print(pro.login_count)
        if pro.login_count > 1:
          return render(request,'index/index.html',context)

        else:
            return render(request,'profilePage.html',context)

    else:

      if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username= username, password=password)
        if user is not None:

              login(request,user)

              posts = Post.objects.all()
              user = request.user
              last = request.user.last_login
              print(last)
              if request.user.last_login is None:
                  return redirect('/profilePage.html')

              else:
                  pro = ProfileEdit.objects.get(user_id=user)

                  if pro.login_count > 1:
                      pro = ProfileEdit.objects.get(user_id=user)
                      print(pro)

                      context = {'posts': posts,
                         'user': user,
                         'pro': pro,
                        }
                      return render(request, 'index/index.html', context)
                  else:
                    context = {'posts': posts,
                              'user': user,
                              'pro': pro,
                             }

                    return render(request,'profilePage.html',context)
        else:
            messages.info(request,'username or password is incorrect')


    return render(request,"login.html")


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def viewProfile(request,id):
    user = request.user
    pro=ProfileEdit.objects.get(user_id=user)
    print(pro)
    context={'user':user,
             'pro':pro,
             }

    return render(request,"profilePage.html",context)

@login_required(login_url='login')
def postPage(request):
    post = PostForm()
    user = request.user
    if request.method == 'POST':
        post_title = request.POST['post_title']
        heading = request.POST['heading']
        content = request.POST['content']
        pub_date = request.POST['pub_date']
        thumbnail = request.POST['thumbnail']
        form = Post(post_title=post_title, heading=heading, content=content, pub_date=pub_date, thumbnail=thumbnail,user=request.user)
        form.save()
        # instance.user = request.user
        # instance.save()
        print("Post Created")
        pro = ProfileEdit.objects.get(user_id=user)
        context={'pro':pro}
        return render(request, "profilePage.html",context)
    else:
        context = {'post': post}
        return render(request, "post.html", context)

@login_required(login_url='login')
def likePost(request):
        # pk = int(id)
        #post = get_object_or_404(Post, post_id=int(request.POST.get('post_id')))
        #post.likes.add(request.user)
        posts = Post.objects.all()
        user = request.user
        if request.method == 'POST':
            post_id = request.POST.get('post_id')
            post_obj = Post.objects.get(post_id=post_id)

            if user in post_obj.likes.all():
                post_obj.likes.remove(user)
            else:
                post_obj.likes.add(user)

            like,created = Like.objects.get_or_create(user=user,post_id=post_id)

            if not created:
                if like.value == 'Like':
                    like.value = 'Unlike'
                else:
                    like.value = 'Like'

            like.save()
        pro = ProfileEdit.objects.get(user_id=user)

        context={'posts':posts,
                 'user':user,
                 'pro':pro,
                }
        return render(request,'index/index.html',context)


def commentPost(request,id):
    post = Post.objects.get(post_id=id)
    user = request.user.first_name
    if request.method == 'POST':

        body = request.POST.get('body')
        new_comment = Comment(post_id=id,name=user,body=body)
        new_comment.save()
        print('Comment added')
    id = request.user
    pro = ProfileEdit.objects.get(user_id=id)

    context={'post':post,
             'user':user,
             'pro':pro,
             }

    return render(request,'comment.html',context)


def editProfile(request,id):

    if request.method == 'POST' :
        education = request.POST['education']
        stream = request.POST['stream']
        company = request.POST['company']
        current_position = request.POST['c_position']
        country = request.POST['country']
        location = request.POST['location']
        experience = request.POST['experience']
        skills = request.POST['skills']
        interests = request.POST['interests']
        contact = request.POST['contact']

        form = ProfileEdit(education=education,stream=stream,company=company,current_position=current_position,country=country,location=location,experience=experience,skills=skills,interests=interests,contact=contact,user=request.user)
        form.save()
        print("Profile Updated")
        pro = ProfileEdit.objects.get(user_id=id)

        context = {'pro': pro,
                   'form':form
                   }
        return render(request,'profilePage.html',context)

    else:
        user = request.user
        context = {'user':user}

        return render (request,'editProfile.html',context)

def dashboard(request):
    return render(request,'dashboard/dashboard.html')