from django.db import models
from django.contrib.postgres.fields import ArrayField

#from django.contrib.postgres.fields import JSONField
#strings = JSONField(default=list, blank=True, null=True)

class RewardGear(models.Model):
    rewardId= models.CharField(primary_key=True)
    kind = models.CharField()
    id = models.IntegerField()
    
class Normal(models.Model):
    bigBoss = models.CharField()
    rewardGear = models.ForeignKey(RewardGear, to_field="rewardId", on_delete=models.CASCADE)
    phaseId = models.CharField(primary_key=True)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    stage = models.IntegerField()
    weapons = ArrayField(models.IntegerField(), size=4, default=list)
    rareWeapons = ArrayField(models.IntegerField(), default=list)


class RewardInfo(models.Model):
    reward = models.IntegerField()
    topPercent = models.IntegerField()
    minimumScore = models.IntegerField()

class PhaseRewards(models.Model):
    normal = models.ForeignKey(RewardInfo, related_name='normal_reward', on_delete=models.CASCADE)
    bronze = models.ForeignKey(RewardInfo, related_name='bronze_reward', on_delete=models.CASCADE)
    silver = models.ForeignKey(RewardInfo, related_name='silver_reward', on_delete=models.CASCADE)
    gold = models.ForeignKey(RewardInfo, related_name='gold_reward', on_delete=models.CASCADE)

class BigRun(models.Model):
    phaseId = models.CharField(primary_key=True)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    stage = models.IntegerField()
    weapons = ArrayField(models.IntegerField())
    rareWeapons = ArrayField(models.IntegerField())
    bigBoss = models.CharField()

    rewards = models.ForeignKey(PhaseRewards, on_delete=models.CASCADE)


class TeamContest(models.Model):
    phaseId = models.CharField(primary_key=True)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    stage = models.IntegerField()
    weapons = ArrayField(models.IntegerField())
    rareWeapons = ArrayField(models.IntegerField())
    specials = ArrayField(models.IntegerField())

    rewards = models.ForeignKey(PhaseRewards, on_delete=models.CASCADE)

