from django.db import models

class category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class bookdetails(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    category = models.ForeignKey(category, on_delete=models.CASCADE, default=1)
    textlink = models.CharField(max_length=1000)
    image = models.ImageField(upload_to="uploads/product", blank=True, null=True)
    description = models.CharField(max_length=250, default="", blank=True, null=True)
    genre = models.CharField(max_length=50, default="None")
    
    def __str__(self):
        return self.name
    
    