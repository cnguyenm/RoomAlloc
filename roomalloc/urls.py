
from django.conf.urls import url 

from roomalloc.view import public, account, user, room

# register app_name for template url
app_name = 'roomalloc'

# url patterns
urlpatterns = [

    # public 
    url(r'^$'               , public.index  , name='index'),
    url(r'^public/about/$'  , public.about  , name='about'),
    url(r'^public/contact/$', public.contact, name='contact'),
    
    # account
    url(r'^account/signup/$', account.signup , name='signup'),
    url(r'^account/login/$' , account.log_in , name='login'),
    url(r'^account/logout/$', account.log_out, name='logout'),
    
    # user
    url(r'^user/$'          , user.home     , name='user_home'),
    url(r'^user/reserve/$'  , user.reserve  , name='user_reserve'),
   
    # room
    url(r'^room/$'                      , room.explore, name='room_explore'),
    url(r'^room/(?P<room_id>[0-9]+)/$'  , room.detail , name='room_detail'),
    url(r'^room/(?P<room_id>[0-9]+)/res$'  , room.reserve , name='room_reserve'),
]

