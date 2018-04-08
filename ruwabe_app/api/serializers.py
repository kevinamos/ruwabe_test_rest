from rest_framework.serializers import ModelSerializer
from ruwabe_app.models import *

class GetUsersSerializer(ModelSerializer):
	class Meta:
		model=User
		fields=[
		'id',
		'first_name',
		'email',
		'last_name',

		]

class CreateUserSerializer(ModelSerializer):
	def create(self, validated_data):
		user = User.objects.create(
			email=validated_data['email']
			)
		user.set_password(validated_data['password'])
		user.save()
		return user
	class Meta:
		model=User
		fields = ['email', 'first_name', 'last_name', 'password']
