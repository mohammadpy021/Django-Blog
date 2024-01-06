# from .models import IPAddress
# class SaveIPAddressMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         # One-time configuration and initialization.

#     def __call__(self, request):
#         # Code to be executed for each request before
#         # the view (and later middleware) are called.

#         x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#         if x_forwarded_for:
#             ip = x_forwarded_for.split(',')[0]
#         else:
#             ip = request.META.get('REMOTE_ADDR')
#         try:
#             ip_address = IPAddress.objects.get(ip_address=ip)
#         except : 
#             # ip_address = IPAddress(ip_address=ip)
#             # ip_address.save()
#             ip_address = IPAddress.objects.create(ip_address=ip) # we don't need .save() method in this line
#         # ip_address = IPAddress.objects.get(ip_address=ip)
#         # if not ip_address:
#         #     # ip_address = IPAddress(ip_address=ip)
#         #     # ip_address.save()
#         #     ip_address = IPAddress.objects.create(ip_address=ip) # we don't need .save() method in this line
#         request.user.ip_address = ip_address

#         response = self.get_response(request)

#         # Code to be executed for each request/response after
#         # the view is called.

#         return response