from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import authenticate
import jwt
from django.conf import settings

# Create your models here.

class User(AbstractUser):
    token = models.CharField('token', max_length=1024, blank=True, null=True)
    
    def auth(self, username, password):
        self.usuario = authenticate(username=username, password=password)
        
        if self.usuario:
            token = jwt.encode({
                'id': self.usuario.id,
                'username': self.usuario.username
            }, settings.SECRET_KEY, algorithm='HS256')
            self.token = token
            self.save()
            
            return True
        return False
    
    def obter_nome(self):
        return f'{self.first_name} {self.last_name}'
    
    def obter_ultimo_login(self):
        if self.last_login:
            return self.last_login.strftime('%d/%m/%Y as %H:%M')
        return None