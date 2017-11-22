"""
const.py:

Store class to help deal with constant variable

"""

class Template():
    """
    Store template name
    """
    
    PUBLIC_INDEX    = "roomalloc/public/index.html"
    PUBLIC_ABOUT    = "roomalloc/public/about.html"
    PUBLIC_CONTACT  = "roomalloc/public/contact.html"
    
    ACC_LOGIN       = "roomalloc/public/login.html"
    ACC_SIGNUP      = "roomalloc/public/signup.html"
    
    USER_HOME       = "roomalloc/user/user_home.html"
    USER_RESERVE    = "roomalloc/user/user_reserve.html"
    USER_ROOM       = "roomalloc/user/user_room.html"
    
    ROOM_EXPLORE    = "roomalloc/user/room/room_explore.html"
    ROOM_DETAIL     = "roomalloc/user/room/room_detail.html"
    ROOM_RESERVE    = "roomalloc/user/room/room_reserve.html"

class TplConst():
    """
    Const that appear in django template
    """
    
    NBAR = "nbar"
    
class GroupName():
    NORMAL = 'normal'
    STAFF = 'staff'
    
