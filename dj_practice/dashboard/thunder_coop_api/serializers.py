import json

from rest_framework import serializers
from dashboard.models import Normal, BigRun, TeamContest, RewardGear, RewardInfo, PhaseRewards


class RewardGearSerializer(serializers.ModelSerializer):
    rewardId= serializers.CharField()
    kind = serializers.CharField()
    id = serializers.IntegerField()

    class Meta:
        model = RewardGear
        fields = '__all__'

def get_default_weapons():
    return [-1, -1, -1, -1]

def weapon_validator(value):
    if value is None:
        return get_default_weapons()
    else:
        weapons = value
        for index, weapon in enumerate(weapons):
            if weapon is None:
                weapons[index] = -1
        return weapons


class NormalSerializer(serializers.ModelSerializer):
    bigBoss = serializers.CharField(allow_null=True)
    rewardGear = RewardGearSerializer()
    phaseId = serializers.CharField()
    startTime = serializers.DateTimeField()
    endTime = serializers.DateTimeField()
    stage = serializers.IntegerField()
    weapons = serializers.ListField(child=serializers.IntegerField(allow_null=True, default=-1), allow_null=False, allow_empty=True, default=get_default_weapons())
    rareWeapons = serializers.ListField(child=serializers.IntegerField(), allow_empty=True)

    class Meta:
        model = Normal
        fields = '__all__'
    
    def validate_weapons(self, value):
        return weapon_validator(value)


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
    


    def create(self, validated_data):

        rewardInfoInstance = RewardInfo.objects.filter(reward=validated_data.get('reward')).first()
        if rewardInfoInstance:
            self.update(rewardInfoInstance, validated_data)
            return rewardInfoInstance
        else:
            return RewardInfo.objects.create(**validated_data)


class PhaseRewardsSerializer(serializers.ModelSerializer):
    normal = RewardInfoSerializer()
    bronze = RewardInfoSerializer()
    silver = RewardInfoSerializer()
    gold = RewardInfoSerializer()

    class Meta:
        model = PhaseRewards
        fields = '__all__'

    def create(self, validated_data):
        self.create_or_update_nested(validated_data)

        updateOrCreateResult = PhaseRewards.objects.update_or_create(normal=validated_data.get('normal'),
                                                           bronze=validated_data.get('bronze'),
                                                           silver=validated_data.get('silver'),
                                                           gold=validated_data.get('gold'))

        return updateOrCreateResult[0]

    def create_or_update_nested(self, validated_data):
        self.create_reward_info_instance(validated_data, validated_data.pop('normal'), 'normal')
        self.create_reward_info_instance(validated_data, validated_data.pop('bronze'), 'bronze')
        self.create_reward_info_instance(validated_data, validated_data.pop('silver'), 'silver')
        self.create_reward_info_instance(validated_data, validated_data.pop('gold'), 'gold')

    def create_reward_info_instance(self, validated_data, rewardInfoRawData, rewardInfoFieldIdentifier):
        RewardInfo.objects.update_or_create(**rewardInfoRawData)
        rewardInfoInstance = RewardInfo.objects.get(reward=rewardInfoRawData.get('reward'))
        validated_data[rewardInfoFieldIdentifier] = rewardInfoInstance


class BigRunSerializer(serializers.ModelSerializer):
    phaseId = serializers.CharField()
    startTime = serializers.DateTimeField()
    endTime = serializers.DateTimeField()
    stage = serializers.IntegerField()
    weapons = serializers.ListField(child=serializers.IntegerField(allow_null=True, default=-1), allow_null=False, allow_empty=True, default=get_default_weapons())
    rareWeapons = serializers.ListField(child=serializers.IntegerField(), allow_empty=True)
    bigBoss = serializers.CharField(allow_null=True)

    rewards = PhaseRewardsSerializer()

    class Meta:
        model = BigRun
        fields = '__all__'
    
    def validate_weapons(self, value):
        return weapon_validator(value)


    def create(self, validated_data):
        self.create_or_update_nested(validated_data)

        bigRunInstance = BigRun.objects.filter(phaseId=validated_data.get('phaseId')).first()
        if bigRunInstance:
            self.update(bigRunInstance, validated_data)
            return bigRunInstance
        else:
            return BigRun.objects.create(**validated_data)

    def create_or_update_nested(self, validated_data):
        rewards = validated_data.pop('rewards')
        # deserialize_object(rewards, PhaseRewardsSerializer)

        normal = self.deserialize_reward_info(rewards, rewardInfoCategoryName='normal')
        bronze = self.deserialize_reward_info(rewards, rewardInfoCategoryName='bronze')
        silver = self.deserialize_reward_info(rewards, rewardInfoCategoryName='silver')
        gold = self.deserialize_reward_info(rewards, rewardInfoCategoryName='gold')
        

        updateOrCreateResult = PhaseRewards.objects.update_or_create(normal=normal, bronze=bronze, silver=silver, gold=gold)

        validated_data['rewards'] = updateOrCreateResult[0]

    def deserialize_reward_info(self, rewards, rewardInfoCategoryName):
        rewardInfoRawData = rewards.get(rewardInfoCategoryName, None)
        deserialize_object(rewardInfoRawData, RewardInfoSerializer)
        return RewardInfo.objects.get(reward=rewardInfoRawData.get('reward'))


class TeamContestSerializer(serializers.ModelSerializer):
    phaseId = serializers.CharField()
    startTime = serializers.DateTimeField()
    endTime = serializers.DateTimeField()
    stage = serializers.IntegerField()
    weapons = serializers.ListField(child=serializers.IntegerField(default=-1), allow_null=False, allow_empty=True, default=get_default_weapons())
    rareWeapons = serializers.ListField(child=serializers.IntegerField(), allow_empty=True)
    specials = serializers.ListField(child=serializers.IntegerField(), allow_empty=True)

    rewards = PhaseRewardsSerializer()

    class Meta:
        model = TeamContest
        fields = '__all__'

    def validate_weapons(self, value):
        return weapon_validator(value)


    def create(self, validated_data):
        self.create_or_update_nested(validated_data)

        teamContestInstance = TeamContest.objects.filter(phaseId=validated_data.get('phaseId')).first()
        if teamContestInstance:
            self.update(teamContestInstance, validated_data)
            return teamContestInstance
        else:
            return TeamContest.objects.create(**validated_data)

    def create_or_update_nested(self, validated_data):
        rewards = validated_data.pop('rewards')

        normal = self.deserialize_reward_info(rewards, rewardInfoCategoryName='normal')
        bronze = self.deserialize_reward_info(rewards, rewardInfoCategoryName='bronze')
        silver = self.deserialize_reward_info(rewards, rewardInfoCategoryName='silver')
        gold = self.deserialize_reward_info(rewards, rewardInfoCategoryName='gold')
        

        updateOrCreateResult = PhaseRewards.objects.update_or_create(normal=normal, bronze=bronze, silver=silver, gold=gold)

        validated_data['rewards'] = updateOrCreateResult[0]

    def deserialize_reward_info(self, rewards, rewardInfoCategoryName):
        rewardInfoRawData = rewards.get(rewardInfoCategoryName, None)
        deserialize_object(rewardInfoRawData, RewardInfoSerializer)
        return RewardInfo.objects.get(reward=rewardInfoRawData.get('reward'))



def deserialize_bulk(json_data):
    total_before = Normal.objects.all().count() + BigRun.objects.all().count() + TeamContest.objects.all().count()
    json_object = json.loads(json_data)
    deserialize_object(json_object.get('Normal', None), NormalSerializer, is_many=True)
    deserialize_object(json_object.get('BigRun', None), BigRunSerializer, is_many=True)
    deserialize_object(json_object.get('TeamContest', None), TeamContestSerializer, is_many=True)

    total_after = Normal.objects.all().count() + BigRun.objects.all().count() + TeamContest.objects.all().count()
    return total_after - total_before

def deserialize_object(json_object, model_serializer, is_many=False):
    if json_object:
        serializer = model_serializer(data=json_object, many=is_many)
        is_valid = serializer.is_valid()
        if not is_valid:
            errors = serializer.errors
        
            for error in zip(errors, json_object):
                if error[0]:
                    print(f"Error: {error[0]} \n In json {error[1]} \n\n")
        else:
            print("data serialized")
            serializer.save()

