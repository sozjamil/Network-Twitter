# from django import forms
# from django.contrib.auth.models import User

# class FollowForm(forms.Form):
#     action = forms.CharField(widget=forms.HiddenInput)

#     def clean_action(self):
#         action = self.cleaned_data['action']
#         if action not in ['follow', 'unfollow']:
#             raise forms.ValidationError('Invalid action.')
#         return action