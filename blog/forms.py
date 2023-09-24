from django import forms 

class BlogForm(forms.Form):  
    title = forms.CharField(label="Enter blog title",max_length=50)  
    description  = forms.CharField(label="Enter blog description", max_length = 300)  

    