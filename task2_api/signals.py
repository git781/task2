from django.db.models.signals import post_save
from django.dispatch import receiver 
from task2_main.models import Measurement, ValidatedMeasurement, InvalidMeasurement

@receiver(post_save, sender=Measurement)
def validate_measurement(sender, instance, **kwargs):
    print(instance, "AAAAAAA", sender)
    #if measurement saved =>validate it:
    #TODO: if validated create Valideted measurement
    #TODO: if invalid create invalid measurement

@receiver(post_save, sender=InvalidMeasurement)
def create_email(sender, instance, **kwargs):
    pass
    #instance.send_email()-->TODO: create send_email in utils
    #TODO: send an e-mail if created InvalidMeasurement
