from django.shortcuts import render, HttpResponseRedirect
from User.forms import CharityAuthorForm, UserUpdateForm
from User.models import Profile
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import *







def charity(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse('login_url'))
	else:

		profile = Profile.objects.get_or_create(user=request.user)
		if request.method == 'POST':
			u_form = UserUpdateForm(request.POST, instance=request.user)
			p_form = CharityAuthorForm(request.POST, request.FILES, instance=request.user.profile)
			# i_form = InvestForm(request.POST)
			if u_form.is_valid() and p_form.is_valid():
				u_form.save()
				p_form.save()
				# i_form.save()
				return render(request, 'dobro/feedback.html', context={})

		else:
			u_form = UserUpdateForm(instance=request.user)
			p_form = CharityAuthorForm(instance=request.user.profile)
			# i_form = InvestForm(request.POST, instance=request.user)




		context = {
			'u_form': u_form,
			'p_form': p_form,
			# 'i_form': i_form

		}
		return render(request, 'dobro/dobro.html', context)
