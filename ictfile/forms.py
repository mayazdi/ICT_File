from django import forms


class UploadFileForm(forms.Form):
    file = forms.FileField()
    username = forms.CharField()
    password = forms.CharField()
    team_name = forms.CharField()
    team_code = forms.DecimalField(max_digits=100, decimal_places=2)
    question_code = forms.DecimalField(max_digits=100, decimal_places=2)
    challenge_code = forms.CharField()
