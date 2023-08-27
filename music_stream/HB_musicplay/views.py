from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from rest_framework.response import Response
from .models import User, Playlist, Song, Artist
from .serializers import UserSerializer, PlaylistSerializer, SongSerializer, ArtistSerializer
from rest_framework import generics
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SignupForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .forms import PlaylistForm
# ... other views ...

from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework import status
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm


# class Userlist(APIView):
#     def get(self, request):
#         queryset = User.objects.all()
#         serializer = UserSerializer(queryset, many=True)
#         return Response(serializer.data)

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ApiPlaylist(APIView):
    def get(self, request):
        queryset = Playlist.objects.all()
        serializer = PlaylistSerializer(queryset, many=True)
        return Response(serializer.data)


class ArtistList(APIView):
    def get(self, request):
        queryset = Artist.objects.all()
        serializer = ArtistSerializer(queryset, many=True)
        return Response(serializer.data)


# def songs_view(request):
#   songs = Song.objects.all()
#  return render(request, 'HB_musicplay/songs.html', {'songs': songs})

def playlists_view(request):
    playlists = Playlist.objects.filter(owner=request.user)
    return render(request, 'playlists.html', {'playlists': playlists})

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User, Playlist, Song, Artist
from .serializers import UserSerializer, PlaylistSerializer, SongSerializer, ArtistSerializer
from rest_framework import generics
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response

# ... other imports ...

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# ... other imports ...

class SongList(APIView):
    # ...

    @method_decorator(login_required)  # Apply login_required decorator
    def get(self, request):
        queryset = Song.objects.all()
        serializer = SongSerializer(queryset, many=True)
        return render(request, 'song.html', {'songs': serializer.data})

    # ...


def home_view(request):
    return render(request, 'home.html')


from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.shortcuts import render, redirect


# ... other views ...

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('HB_musicplay:songs')  # Redirect to the songs page
            else:
                form.add_error(None, "Invalid username or password.")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def signup_view(request):
    return render(request, 'signup.html')


def base_view(request):
    return render(request, 'base.html')

# ... other imports ...

def home_view(request):
    return render(request, 'home.html')


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('HB_musicplay:home')  # Replace with your home URL
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/songs/')
            else:
                form.add_error(None, "Invalid username or password.")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def create_playlist_view(request):
    if request.method == 'POST':
        form = PlaylistForm(request.POST)
        if form.is_valid():
            playlist = form.save(commit=False)
            playlist.owner = request.user
            playlist.save()
            form.save_m2m()
            return redirect('HB_musicplay:playlists')
    else:
        form = PlaylistForm()

    # Fetch available songs for the form
    available_songs = Song.objects.all()
    context = {'form': form, 'available_songs': available_songs}
    return render(request, 'create_playlist.html', context)

# def add_to_playlist(request, id):
#     song = Song.objects.get(id=id)
#     Playlist.objects.create(
#         name = 'Playlist 1',
#         owner=request.user,
#     )