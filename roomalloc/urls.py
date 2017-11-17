
from django.conf.urls import url 

from roomalloc.view import public, account, user

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
    url(r'^user/explore/$'  , user.explore  , name='user_explore'),
]

