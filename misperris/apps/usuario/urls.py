from django.conf.urls import url, include
from apps.usuario.views import RegistroUsuario, UserAPI
from django.contrib.auth.views import LoginView, logout_then_login, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    url(r'^registrar', RegistroUsuario.as_view(), name='registrar'),
    url(r'^api', UserAPI.as_view(), name='api'),

    
    url(r'^reset/password_reset', PasswordResetView.as_view(), 
        {'template_name':'registration/password_reset_form.html',
        'email_template_name': 'registration/password_reset_email.html'}, 
        name='password_reset'), 
    url(r'^password_reset_done', PasswordResetDoneView.as_view(), 
        {'template_name': 'registration/password_reset_done.html'}, 
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', PasswordResetConfirmView.as_view(), 
        {'template_name': 'registration/password_reset_confirm.html'},
        name='password_reset_confirm'
        ),
    url(r'^reset/done', PasswordResetCompleteView.as_view(), {'template_name': 'registration/password_reset_complete.html'},
        name='password_reset_complete'),

]