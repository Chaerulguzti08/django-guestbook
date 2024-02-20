from django.db import models

class TblEvent(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=250)
    created_by = models.CharField(max_length=50)
    updated_by = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tbl_event'

class TblGuest(models.Model):
    event_id = models.IntegerField()
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=50)
    froms = models.CharField(max_length=50)
    date_time = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'tbl_guest'