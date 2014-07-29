from django.shortcuts import render
from django.template import Context, loader 
from django.http import HttpResponse
from models import UserLink

# Create your views here.
def ListUsers(request): 
  user_list = UserLink.objects.all()
  t = loader.get_template('MySN/allUsers.html') 
  c = Context({ 'user_list': user_list, }) 
  return HttpResponse(t.render(c))

def ListFollowers(request, username):
  follower_list = UserLink.objects.filter(to_user__username = username)
  t = loader.get_template('MySN/followers.html') 
  c = Context({ 'follower_list': follower_list, }) 
  return HttpResponse(t.render(c))

def ListFollowing(request, username):
  follow_list = UserLink.objects.filter(from_user__username = username)
  t = loader.get_template('MySN/following.html') 
  c = Context({ 'follow_list': follow_list, }) 
  return HttpResponse(t.render(c))