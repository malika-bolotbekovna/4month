from django import forms
from posts.models import Category, Post, Tag

class PostForm(forms.Form):
    image = forms.ImageField()
    title = forms.CharField(max_length=256)
    content = forms.CharField(max_length=512)

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        content = cleaned_data.get("content")
        if (title and content) and (title.lower() == content.lower()):
            raise forms.ValidationError(message="Title and content must be different")
        return cleaned_data
    
    def clean_title(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        if title and title.lower() == "javascript":
            raise forms.ValidationError(message="JavaScript is not allowed")
        return title
    
class PostForm2(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["image", "title", "content"]

class SearchForm(forms.Form):
    search = forms.CharField(min_length=1, required=False)
    category_id = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False)
    orderings = (
        ("rate", "Rate"), 
        ("-rate", "Rate descending"), 
        ("created_at", "Created at"), 
        ("-created_at", "Created at descending")
    )
    ordering = forms.ChoiceField(choices=orderings, required=False)

