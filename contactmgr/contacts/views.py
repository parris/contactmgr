from django.views.generic import ListView
from contacts.models import Contact

class ListContactsView(ListView):
	
	model =  Contact
	template_name = 'list.html'

