from ninja import Router
from .models import User
from .schemas import RegisterIn, LoginIn
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

user_authentication_api = Router()

@user_authentication_api.post("/register/")
def auth_register(request, payload: RegisterIn):
    if User.objects.filter(username=payload.username).exists():
        return {"msg": "Username already exists"}
    user = User.objects.create_user(username=payload.username, password=payload.password)
    return {"msg": "User created successfully", "username": user.username, "pwd": user.password}

@user_authentication_api.post("/login/")
def auth_login(request: HttpRequest, response: HttpResponse, payload: LoginIn): #这样用payload参数代表request body
    print(f"username: {payload.username}, password: {payload.password}")
    # authenticate()自动调用create_user()时同样的哈希计算
    user = authenticate(request, username=payload.username, password=payload.password) #就是检查用户名对应的口令
    print(user)
    print(type(user))
    if user is not None:
        login(request, user)
        response.set_cookie("cookie", "delicious") #浏览器还是没有cookie !!!(前端需要设置axios.defaults.withCredentials = true;)
        return {"msg": "Login successful", "username": user.username}
    else:
        return {"msg": "Invalid credentials"}
    
@user_authentication_api.get("/logout/")
def auth_logout(request, response: HttpResponse):
    logout(request) #把login()做的事情抵消了,session表删掉这个用户的session,删掉client的sessionid的cookie
    response.delete_cookie('cookie') #然后前端浏览器真的把这个cookie删了
    return {"msg": "Logout successfully"}
