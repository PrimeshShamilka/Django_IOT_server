from rest_framework import serializers
from . models import devices
from . models import data

class devicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = devices
        fields = '__all__'

    def create(self, validated_data):
        return devices.objects.create(**validated_data)


    

    # def create(self, validated_data):
    #     device_id_ = validated_data.get('device_id', None)
    #     if device_id_ is not None:
    #         device_id = devices.objects.filter(id=device_id_).first()
    #         if device_id is not None:
    #             answer = question.answer
    #             if answer is not None:
    #                # update your answer
    #                return answer

    #     answer = Answer.objects.create(**validated_data)
    #     return answer

class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = data
        fields = ['device','values']