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
    ACC_PROFILE     = "roomalloc/user/user_profile.html"
    
    USER_HOME       = "roomalloc/user/user_home.html"
    
    RES_LIST        = "roomalloc/user/reserve/res_list.html"
    RES_DETAIL      = "roomalloc/user/reserve/res_detail.html"
    
    ROOM_EXPLORE    = "roomalloc/user/room/room_explore.html"
    ROOM_DETAIL     = "roomalloc/user/room/room_detail.html"
    ROOM_RESERVE    = "roomalloc/user/room/room_reserve.html"
    ROOM_CONFIRM    = "roomalloc/user/room/room_confirm.html"

class TplConst():
    """
    Const that appear in django template
    """
    
    NBAR = "nbar"
    
class GroupName():
    NORMAL = 'normal'
    STAFF = 'staff'
    
