from django.db import models

# Create your models here.

# host model
class Host(models.Model):
    hostname = models.CharField(max_length=20,null=False,default='')
    system = models.CharField(max_length=10,null=False,default='')
    sn = models.CharField(max_length=128,null=False,default='')
    architecture = models.CharField(max_length=10,null=False,default='')
    os_family = models.CharField(max_length=10,null=False,default='')
    distribution = models.CharField(max_length=10,null=False,default='')
    distribution_version = models.CharField(max_length=10,null=False,default='')
    memtotal_mb = models.PositiveIntegerField(null=False,default=0)
    swaptotal_mb = models.PositiveIntegerField(null=False,default=0)
    processor_count  = models.IntegerField(null=False,default=0)
    processor_cores = models.IntegerField(null=False, default=0)
    diskdevice = models.CharField(max_length=100,null=False,default='{}')
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