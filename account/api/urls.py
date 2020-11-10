from django.urls import path
from django.conf.urls import url

from account.api.views import(
	registration_view,
	list_registration_view,
	detail_registration_view,
	winner_registration_view
)

from account.views import(send_email_view)

app_name = 'account'

urlpatterns = [
	path('register', registration_view, name="register"),
	path('list', list_registration_view, name="list"),
	url(r'^detail/(?P<pk>[0-9]+)$', detail_registration_view),
	path('winner', winner_registration_view),
	path('send_email', send_email_view, name='index')
]