from django.db import models
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist

# Create your models here.

# host model
class Host(models.Model):
    hostname = models.CharField(max_length=20,null=False,default='')
    system = models.CharField(max_length=10,null=False,default='')
    sn = models.CharField(max_length=128,null=False,default='')
    architecture = models.CharField(max_length=10,null=False,default='')
    os_family = models.CharField(max_length=20,null=False,default='')
    distribution = models.CharField(max_length=20,null=False,default='')
    memtotal_mb = models.PositiveIntegerField(null=False,default=0)
    processor_cores = models.IntegerField(null=False, default=0)
    diskmount = models.CharField(max_length=512,null=False,default='{}')
    ip_business = models.GenericIPAddressField(null=False,default='0.0.0.0')
    ip_manager = models.GenericIPAddressField(null=False,default='0.0.0.0')
    rack_number = models.CharField(max_length=20,null=False,default='')
    unit_number = models.CharField(max_length=10,null=False,default='')
    status = models.CharField(max_length=5,null=False,default='')
#   type = models.CharField(max)
    remark = models.CharField(max_length=100,null=False,default='')
#   owner
#   label
    
    create_time = models.DateTimeField(null=False,auto_now_add=True)
    update_time = models.DateTimeField(null=False)

    @classmethod
    def create_or_replace(cls, hostname,system,sn,architecture,os_family,distribution,
                         memtotal_mb,processor_cores,diskmount,ip_business):
        try:
            obj = cls.objects.get(ip_business = ip_business)
        except ObjectDoesNotExist:
            obj = cls()
            obj.ip_business = ip_business

        obj.hostname = hostname
        obj.system = system
        obj.sn = sn
        obj.architecture = architecture
        obj.os_family = os_family
        obj.distribution = distribution
        obj.memtotal_mb = memtotal_mb
        obj.processor_cores = processor_cores
        obj.diskmount = diskmount
        obj.update_time = timezone.now()
        obj.save()
        return obj
