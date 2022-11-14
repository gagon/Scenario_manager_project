from django.urls import path, include


urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),

]

# auth/users/me/ - currentUser
# auth/users/    - createUser
# auth/token/login/ - loginUser and create token
# auth/token/logout/- logoutUser and delete token