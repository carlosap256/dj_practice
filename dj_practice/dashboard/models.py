from django.db import models
from django.contrib.postgres.fields import ArrayField


class RewardGear(models.Model):
    rewardId= models.CharField(primary_key=True)
    kind = models.CharField()
    id = models.IntegerField()


class Normal(models.Model):
    bigBoss = models.CharField(null=True)
    rewardGear = models.ForeignKey(RewardGear, to_field="rewardId", on_delete=models.CASCADE)
    phaseId = models.CharField(primary_key=True)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    stage = models.IntegerField()
    weapons = ArrayField(models.IntegerField(null=False, default=-1), size=4, default=list)
    rareWeapons = ArrayField(models.IntegerField(), default=list)


class RewardInfo(models.Model):
    reward = models.IntegerField(primary_key=True)
    topPercent = models.IntegerField()
    minimumScore = models.IntegerField()    


class PhaseRewards(models.Model):
    normal = models.ForeignKey(RewardInfo, to_field='reward', related_name='normal_reward', on_delete=models.CASCADE)
    bronze = models.ForeignKey(RewardInfo, to_field='reward', related_name='bronze_reward', on_delete=models.CASCADE)
    silver = models.ForeignKey(RewardInfo, to_field='reward', related_name='silver_reward', on_delete=models.CASCADE)
    gold = models.ForeignKey(RewardInfo, to_field='reward', related_name='gold_reward', on_delete=models.CASCADE)


class BigRun(models.Model):
    phaseId = models.CharField(primary_key=True)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    stage = models.IntegerField()
    weapons = ArrayField(models.IntegerField(null=False, default=-1), size=4, default=list)
    rareWeapons = ArrayField(models.IntegerField())
    bigBoss = models.CharField(null=True)

    rewards = models.ForeignKey(PhaseRewards, on_delete=models.CASCADE)


class TeamContest(models.Model):
    phaseId = models.CharField(primary_key=True)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    stage = models.IntegerField()
    weapons = ArrayField(models.IntegerField(null=False, default=-1), size=4, default=list)
    rareWeapons = ArrayField(models.IntegerField())
    specials = ArrayField(models.IntegerField())

    rewards = models.ForeignKey(PhaseRewards, on_delete=models.CASCADE)

