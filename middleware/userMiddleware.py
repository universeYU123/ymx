from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render,redirect

class UserMiddleware(MiddlewareMixin):
    def process_request(self, request): #请求之前
        path = request.path_info
        if path == '/app/login/' or path == '/app/register/':
            return None
        else:
            if not request.session.get('username'):
                return redirect('/app/login/')
            else:
                return None


    def process_view(self,request,callback,callback_args,callback_kwargs):#view和路由之间
        pass

    def process_response(self,request,response):#响应中间键
        return response