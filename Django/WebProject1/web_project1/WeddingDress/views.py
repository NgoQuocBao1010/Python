from django.shortcuts import render, redirect
from .models import WeddingDress
from django.http import HttpResponse

# Create your views here.
def home(resquest):
	context = {
		'data': WeddingDress.objects.all()
	}
	return render(resquest, 'WeddingDress/home.html', context)


def detail(response, id):
	dress = WeddingDress.objects.get(id=id)

	if response.method == "POST":
		sz = response.POST.get("size")
		email = response.POST.get("email")
		phone = response.POST.get("p_number")

		if response.POST.get("buy"):
			method = 'buy'
			price = dress.salesprice
			print(sz, email, phone, method)

		if response.POST.get("rent"):
			method = 'rent'
			price = dress.rental_price
			print(sz, email, phone, method)

		import smtplib, os
		from email.message import EmailMessage

		msg = EmailMessage()
		msg['subject'] = "Confirm Message"
		msg['from'] = 'totti.chelsea@gmail.com'
		msg['to'] = email
		path = os.getcwd() + '\\WeddingDress\\templates\\WeddingDress\\email_send.html'
		temp = open(path).read()
		msg.add_alternative(temp, subtype='html')

		with smtplib.SMTP_SSL("smtp.gmail.com", 465) as sv:
			sv.login('totti.chelsea@gmail.com', 'mkcnhqb1010')
			sv.send_message(msg)

		purchased_info = {
			'name': dress.name,
			'size': sz,
			'method': method,
			'email': email,
			'image_url': dress.image.url,
			'price': price,
		}
		print(email)
		return render(response, 'WeddingDress/confirm.html', {"info": purchased_info})
	else:
		return render(response, 'WeddingDress/dress.html', {"dress": dress})