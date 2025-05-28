from django.shortcuts import redirect
from django.urls import resolve
from django.utils.deprecation import MiddlewareMixin

class AuthRequiredMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # List of public URL names (not paths)
        PUBLIC_VIEW_NAMES = [
            'login',
            'signup',
            'forgot_password',
            'reset_password',  # This covers all reset password URLs
        ]

        try:
            # Resolve the current URL to get its view name
            current_view_name = resolve(request.path_info).url_name
        except:
            current_view_name = None

        # Skip middleware for:
        # 1. Public views
        # 2. Admin interface
        # 3. Static files
        if (current_view_name in PUBLIC_VIEW_NAMES or
            request.path_info.startswith('/admin/') or
            request.path_info.startswith('/static/')):
            return None

        # Redirect to login if not authenticated
        if not request.user.is_authenticated:
            return redirect('login')

        return None


# from django.shortcuts import redirect
# from django.urls import reverse
# from django.utils.deprecation import MiddlewareMixin


# class AuthRequiredMiddleware(MiddlewareMixin):
#   PUBLIC_URLS = [
#     reverse('login'),
#     reverse('signup'),
#     reverse('forgot_password'),
#     reverse('reset_password'), #Placeholder Url
#   ]

#   def process_request(self, request):
#     # Skip middleware for public URLs
#     if any(request.path.startswith(url) for url in self.PUBLIC_URLS):
#         return None
    
#     # Skip middleware for admin URLs
#     if request.path.startswith('/admin/'):
#         return None
    
#     # Redirect to login if not authenticated
#     if not request.user.is_authenticated:
#         return redirect('login')
        
#     return None

#   # def __init___(self, get_response):
#   #   self.get_response = get_response

#   # def __call__(self, request):
#   #   response = self.get_response(request)
#   #   return response
  
#   # def process_view(self, request, view_func, view_args, view_kwargs):
#   #   path = request.path_info

#   #   if any(path.startswith(str(public)) for public in PUBLIC_URLS):
#   #     return None
    
#   #   if not request.user.is_authenticated:
#   #     return redirect('login')
    
#   #   return None
  
