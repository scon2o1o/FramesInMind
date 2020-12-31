from django.shortcuts import render
from django.http import HttpResponse
from.models import Product

# Create your views here.

def home(request):

	prod1 = Product()
	prod1.name = 'Christmas Bauble'
	prod1.desc = 'A lovely Christmas Bauble'
	prod1.price = '25.00'
	prod1.img = 'https://scontent-dub4-1.xx.fbcdn.net/v/t1.0-9/126206158_1062800807493980_3049868636039537948_o.jpg?_nc_cat=105&ccb=2&_nc_sid=a26aad&_nc_ohc=HxHUPnj6S10AX90PM84&_nc_ht=scontent-dub4-1.xx&oh=8bcb1225c6a17be30e3ddf0ed2a64ee0&oe=6014524A'
	

	prod2 = Product()
	prod2.name = 'Christmas Bauble'
	prod2.desc = 'A lovely Christmas Bauble'
	prod2.price = '25.00'
	prod2.img = 'https://scontent-dub4-1.xx.fbcdn.net/v/t1.0-9/126206158_1062800807493980_3049868636039537948_o.jpg?_nc_cat=105&ccb=2&_nc_sid=a26aad&_nc_ohc=HxHUPnj6S10AX90PM84&_nc_ht=scontent-dub4-1.xx&oh=8bcb1225c6a17be30e3ddf0ed2a64ee0&oe=6014524A'

	prod3 = Product()
	prod3.name = 'Christmas Bauble'
	prod3.desc = 'A lovely Christmas Bauble'
	prod3.price = '25.00'
	prod3.img = 'https://scontent-dub4-1.xx.fbcdn.net/v/t1.0-9/126206158_1062800807493980_3049868636039537948_o.jpg?_nc_cat=105&ccb=2&_nc_sid=a26aad&_nc_ohc=HxHUPnj6S10AX90PM84&_nc_ht=scontent-dub4-1.xx&oh=8bcb1225c6a17be30e3ddf0ed2a64ee0&oe=6014524A'

	products = [prod1, prod2, prod3]
	
	return render(request, 'home.html', {'products': products})
