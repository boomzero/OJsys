from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    pub_date = models.DateTimeField("date published")
    timeLimit = models.IntegerField(default=1000)
    memoryLimit = models.IntegerField(default=128)
    submissionCnt = models.IntegerField(default=0)
    acceptedCnt = models.IntegerField(default=0)
    def __str__(self):
        return self.title


class Dataset(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    dataset_in = models.TextField()
    dataset_out = models.TextField()
    isSample = models.BooleanField(default=False)
    isSpj = models.BooleanField(default=False)
    spj = models.TextField()
    def __str__(self):
        return self.dataset_in


class Submission(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    code = models.TextField()
    lang = models.CharField(max_length=20,default="C++")
    user = models.CharField(max_length=20)
    def __str__(self):
        return self.code

class Record(models.Model):
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    time = models.IntegerField(default=0)
    memory = models.IntegerField(default=0)
    def __str__(self):
        return self.status
