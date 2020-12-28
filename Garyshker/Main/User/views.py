from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.views.generic import View





def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			name = form.cleaned_data.get('username')
			messages.success(request, f'Your account has been created!. Now able to log in')
			return redirect('login_url')
	else:
		form = UserRegisterForm()
	return render(request, 'user/register.html', context={'form':form})







def profiles(request):
	profile = Profile.objects.get_or_create(user=request.user)
	if request.method == 'POST':
		print("GONNA")
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
		print(p_form)
		if p_form.is_valid():
			print("gonna save")
			# u_form.save()
			p_form.save()

			print(p_form)
			# return redirect('obrazovanie_url')


	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)
		print("didn't work")
		# return redirect('obrazovanie_url')


	context = {
		'u_form': u_form,
		'p_form': p_form
	}
	return render(request, 'user/profile.html', context)

#
# class UserProfile(View):
# 	model = Profile
# 	template = 'user/profile.html'
#
# 	def get(self, request, *args, **kwargs):
# 		profile = self.model.objects.get_or_create(user=request.user)
# 		u_form = UserUpdateForm(instance=request.user)
# 		p_form = ProfileUpdateForm(instance=request.user.profile)
# 		context = {
# 			'u_form': u_form,
# 			'p_form': p_form
# 			}
# 		return render(request, self.template, context)
#
#
# 	def post(self, request, *args, **kwargs):
# 		profile = self.model.objects.get_or_create(user=request.user)
# 		u_form = UserUpdateForm(request.POST, instance=request.user)
# 		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
#
# 		if u_form.is_valid() and p_form.is_valid():
# 			u_form.save()
# 			p_form.save()
# 			messages.success(request, f'Your account has been updated!')
# 			return redirect('profile_url')
#
# 		context = {
# 			'u_form': u_form,
# 			'p_form': p_form
# 		}
# 		return render(request, self.template, context)





def someone_profile(request, id):
	profile = User.objects.get(id=id)
	# print(profile.user)
	context = {
		'profile':profile
	}
	return render(request, 'user/someone_profile.html', context)


# def profile(request):
# 	profile = Profile.objects.get_or_create(user=request.user)
# 	if request.method == 'POST':
# 		u_form = UserUpdateForm(request.POST, instance=request.user)
# 		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
# 		if u_form.is_valid() and p_form.is_valid():
# 			u_form.save()
# 			p_form.save()

# 	else:
# 		u_form = UserUpdateForm(instance=request.user)
# 		p_form = ProfileUpdateForm(instance=request.user.profile)

# 	context = {
# 		'u_form': u_form,
# 		'p_form': p_form
# 	}

# 	return render(request, 'user/profile.html', context)
