from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from .models import Contents, User_additions, Image
import datetime
from .models import Image
from django.http import HttpResponse




# Create your views here.
@login_required(login_url='login')
def home(request):
    username = request.user.username.capitalize
    user_content = list()
    temp_user_content = list()
    user_idlist = Contents.objects.all()
    id_content = set()
    try: 
        for id in user_idlist: #list semua id yg memiliki konten
            id_content.add(id.id_user)
        # print(id_content) # print id user yang memiliki konten
        for id in id_content: #list content, nama, dan date content yg ada di database
            for j in range(1,User_additions.objects.get(id_user = id).content_count+1):
                data_content = Contents.objects.get(id_user=id, number_content=str(j))
                temp_user_content.append((User.objects.get(id=id).username, data_content.post_date, str(data_content.text_content), data_content.image))
        # komen = comments.coments
        # id = comments.id_user
        # print(comments.coments[0])
        
    except Exception as e: # work on python 3.x
        print(e)
        print("Tidak ada konten yg bisa ditampilkan")

    

    date = lambda temp_user_content:temp_user_content[1] #SORT OBJECT DENGAN KOLOM TERTENTU
    temp_user_content.sort(key=date, reverse=True)

    for data in temp_user_content: #masukkan ke list object untuk ditampilkan ke html
        user_content.append(Content_view(name=data[0], date=data[1], text_content=data[2], image=data[3]))
        print(data[3])
    
    #untuk foto profile
    # img_path = User.objects.get(id=16).image
    return render(request, 'facebook.html',{'contents': user_content, 'username':username})


def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2 and len(username) != 0 and len(email) != 0 and len(password) != 0:
            if User.objects.filter(email = None).exists():
                messages.info(request, 'email is still empty')
                return redirect('register')
            elif User.objects.filter(email = email).exists():
                messages.info(request, 'email already use')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'username already use')
                return redirect('register')
            else:
                try:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save()

                    for i in User.objects.all():
                        print(i.id)

                    user_addition = User_additions.objects.create(id_user = user.id, followed=['',], follower=['',], content_count=0)
                    user_addition.save()            
                except Exception as e:
                    print(e)

                print("Welcome new user", user)
                return redirect('login')
        else:
            messages.info(request, 'Password not the same')
            return redirect('register')
    else:
        return render(request, 'register.html')


def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        data_user = [username, password]

        user = auth.authenticate(username = username, password=password)

        if user is not None:
            auth.login(request, user)
            print("username :", user, "is just login")
            info = user.is_authenticated 
            return redirect('/', {"data" : data_user})
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')
    else:      
        return render(request, 'login.html')

def logout(request):
    print("username :", request.user, "is just logout")
    auth.logout(request)
    return redirect('/')

def post(request): #post content atau update content
    # print(Contents.objects.filter(id_user = request.user.id).exists())
    print(request.user.id)
    if not User_additions.objects.filter(id_user=request.user.id).exists():
        User_additions.objects.create(id_user = request.user.id, followed=['',], follower=['',], content_count=0)

    user_content = User_additions.objects.get(id_user = request.user.id)
    
    Contents.objects.create(text_content= request.POST['content'], post_date=datetime.datetime.now(), id_user = request.user.id, number_content=user_content.content_count+1, like_count=0, coments=['',])
    user_content.content_count = user_content.content_count+1
    user_content.save()
    return redirect('/')

def content(request): #view Content
    content_ = Contents.objects.all()
    return render(request, 'postContent.html', {'content':content_})

def searching(request):
    search_key = request.POST['search_key']
    print(request.user, "is searching", search_key)
    return redirect('/')

def image_upload(request):
    if request.method == 'POST':
        image = request.FILES['image']
        image_model = Image(image=image)
        image_model.save()
        return redirect('image_upload')
    return render(request, 'image_upload.html')


def image(request, file):
    img_path = Image.objects.get(id=16)
    return render(request, 'image.html', {'img_path':img_path.image})
    
class Content_view():
    def __init__(self, name, date, text_content, image) -> None:
        self.name = name.capitalize()
        self.date = date
        self.text_content = text_content
        self.image = image