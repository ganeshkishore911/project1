from django.contrib.auth.models import User #build in user model has fields like username,password,email
from rest_framework import serializers# this handle the validation,serialize, deserialize


class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True) #override for secure cause we cant get the password with api
    class Meta:
        model=User
        fields = ('username', 'email', 'password')
    def create(self, validated_data): # DRF automatically runs validations (e.g., username not blank, email valid).
        user=User.objects.create_user( 
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']

            )
        return user
    
