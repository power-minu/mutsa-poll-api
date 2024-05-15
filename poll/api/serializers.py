from rest_framework import serializers
from poll.models import Poll

class PollSerializer(serializers.ModelSerializer):
    agreeRate = serializers.SerializerMethodField()
    disagreeRate = serializers.SerializerMethodField()
    
    def get_agreeRate(self, obj):
        a = obj.agree
        d = obj.disagree
        
        if a == 0:
            return 0
        else:
            return a / (a + d)
        
    def get_disagreeRate(self, obj):
        a = obj.agree
        d = obj.disagree
        
        if d == 0:
            return 0
        else:
            return d / (a + d)
    
    class Meta:
        model = Poll
        fields = (
            'id',
            'title',
            'description',
            'agree',
            'disagree',
            'agreeRate',
            'disagreeRate',
            'createdAt'
            )
        
class PollRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ('title', 'description')