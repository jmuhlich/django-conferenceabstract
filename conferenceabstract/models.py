from django.db import models


class Participant(models.Model):
    email = models.EmailField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    auth_hash = models.CharField(max_length=200)


class Submission(models.Model):
    owner = models.ForeignKey(Participant)
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=2000)
    date_created = models.DateTimeField(auto_now=True)


class Author(models.Model):

    submission = models.ForeignKey('Submission')
    name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    affiliation = models.CharField('affiliations', max_length=400) # delimiter-separated
    email = models.EmailField(max_length=200)
    is_presenting = models.BooleanField('presenting?')

    class Meta:
        order_with_respect_to = 'submission'

    def get_affiliations(self):
        return self.affiliation.split(settings.AFFILIATION_SEPARATOR)
