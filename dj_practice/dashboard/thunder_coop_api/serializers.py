from rest_framework import serializers
from dashboard.models import Normal, BigRun, TeamContest, RewardGear, RewardInfo, PhaseRewards

class RewardGearSerializer(serializers.ModelSerializer):
    rewardId= serializers.CharField()
    kind = serializers.CharField()
    id = serializers.IntegerField()

    class Meta:
        model = RewardGear
        fields = '__all__'


class NormalSerializer(serializers.ModelSerializer):
    bigBoss = serializers.CharField()
    rewardGear = RewardGearSerializer()
    phaseId = serializers.CharField()
    startTime = serializers.DateTimeField()
    endTime = serializers.DateTimeField()
    stage = serializers.IntegerField()
    weapons = serializers.ListField(child=serializers.IntegerField(), allow_empty=True)
    rareWeapons = serializers.ListField(child=serializers.IntegerField(), allow_empty=True)

    class Meta:
        model = Normal
        fields = '__all__'

    def create(self, validated_data):
        self.create_or_update_nested(validated_data)

        normalInstance = Normal.objects.filter(phaseId=validated_data.get('phaseId')).first()
        if normalInstance:
            self.update(normalInstance, validated_data)
            return normalInstance
        else:
            return Normal.objects.create(**validated_data)

    def create_or_update_nested(self, validated_data):
        rewardGear = validated_data.pop('rewardGear')

        RewardGear.objects.update_or_create(**rewardGear)
        rewardGearInstance = RewardGear.objects.get(rewardId=rewardGear.get('rewardId'))
        validated_data['rewardGear'] = rewardGearInstance

class RewardInfoSerializer(serializers.ModelSerializer):
    reward = serializers.IntegerField()
    topPercent = serializers.IntegerField()
    minimumScore = serializers.IntegerField()
    
    class Meta:
        model = RewardInfo
        fields = '__all__'

class PhaseRewardsSerializer(serializers.ModelSerializer):
    normal = RewardInfoSerializer()
    bronze = RewardInfoSerializer()
    silver = RewardInfoSerializer()
    gold = RewardInfoSerializer()

    class Meta:
        model = PhaseRewards
        fields = '__all__'

class BigRunSerializer(serializers.ModelSerializer):
    phaseId = serializers.CharField()
    startTime = serializers.DateTimeField()
    endTime = serializers.DateTimeField()
    stage = serializers.IntegerField()
    weapons = serializers.ListField(child=serializers.IntegerField(), allow_empty=True)
    rareWeapons = serializers.ListField(child=serializers.IntegerField(), allow_empty=True)
    bigBoss = serializers.CharField()

    rewards = PhaseRewardsSerializer()

    class Meta:
        model = BigRun
        fields = '__all__'


class TeamContestSerializer(serializers.ModelSerializer):
    phaseId = serializers.CharField()
    startTime = serializers.DateTimeField()
    endTime = serializers.DateTimeField()
    stage = serializers.IntegerField()
    weapons = serializers.ListField(child=serializers.IntegerField(), allow_empty=True)
    rareWeapons = serializers.ListField(child=serializers.IntegerField(), allow_empty=True)
    specials = serializers.IntegerField()

    rewards = PhaseRewardsSerializer()

    class Meta:
        model = TeamContest
        fields = '__all__'




