from django.db import models

# Create your models here.
class Regular_Expression(models.Model):
    name = models.CharField('Regular Description', unique = True, max_length = 250)
    expression = models.CharField('Expression', max_length = 250)
    class Meta:
        db_table = 'regular_expression'
class Detected_Message(models.Model):
    regression = models.ForeignKey(Regular_Expression, on_delete = models.CASCADE)
    content = models.TextField("Content", max_length=1000)
    
    class Meta:
        db_table = 'detected_message'