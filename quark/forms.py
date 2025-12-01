from django import forms

class SearchForm(forms.Form):
    search_title = forms.CharField(
        label='제목 검색',
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'style': 'width:50%;',
            'placeholder': '제목으로 검색...',
        })
    )