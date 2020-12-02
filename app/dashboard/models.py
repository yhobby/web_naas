import uuid
import datetime

from django.db import models
from django.utils import timezone


class DeviceInfo(models.Model):
    city = models.CharField(max_length=200)
    vendor = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    tenant = models.CharField(max_length=200)
    hostname = models.CharField(max_length=200)
    ip = models.GenericIPAddressField(protocol='IPv4', primary_key=True)
    role = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    soft = models.CharField(max_length=200)
    patch = models.CharField(max_length=200)
    uptime = models.CharField(max_length=200)
    # uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # upload_date = models.DateTimeField('date uploaded')

    def __str__(self):
        return self.hostname + ' ' + self.ip

    def was_uploaded_recently(self):
        return self.upload_date >= timezone.now() - datetime.timedelta(days=1)

    class Meta:
        # app_label = 'my_db'
        managed = False
        db_table = 'device_info'


class AclInfo(models.Model):
    hostname = models.CharField(max_length=200)
    ip = models.GenericIPAddressField(protocol='IPv4')
    acl = models.IntegerField()
    description = models.CharField(max_length=200)
    # uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    uid = models.TextField(primary_key=True)
    # upload_date = models.DateTimeField('date uploaded')

    def __str__(self):
        return self.hostname + ' ' + self.acl

    def was_uploaded_recently(self):
        return self.upload_date >= timezone.now() - datetime.timedelta(days=1)

    class Meta:
        # app_label = 'my_db'
        managed = False
        db_table = 'acl_info'


class BgpInfo(models.Model):
    hostname = models.CharField(max_length=200)
    ip = models.GenericIPAddressField(protocol='IPv4')
    vrf = models.CharField(max_length=200)
    peer = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    version = models.IntegerField()
    asn = models.IntegerField()
    uptime = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    routes = models.IntegerField()
    bfd = models.CharField(max_length=200)
    route_limit = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    # uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    uid = models.TextField(primary_key=True)
    # upload_date = models.DateTimeField('date uploaded')

    def __str__(self):
        return self.hostname + ' ' + self.peer

    def was_uploaded_recently(self):
        return self.upload_date >= timezone.now() - datetime.timedelta(days=1)

    class Meta:
        # app_label = 'my_db'
        managed = False
        db_table = 'bgp_info'


class BoardsInfo(models.Model):
    hostname = models.CharField(max_length=200)
    ip = models.GenericIPAddressField(protocol='IPv4')
    chassis = models.CharField(max_length=200)
    slot = models.IntegerField()
    type = models.CharField(max_length=200)
    barcode = models.CharField(max_length=200)
    board = models.CharField(max_length=200)
    # uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    uid = models.TextField(primary_key=True)
    # upload_date = models.DateTimeField('date uploaded')

    def __str__(self):
        return self.hostname + ' ' + self.board

    def was_uploaded_recently(self):
        return self.upload_date >= timezone.now() - datetime.timedelta(days=1)

    class Meta:
        # app_label = 'my_db'
        managed = False
        db_table = 'boards_info'


class LagInfo(models.Model):
    hostname = models.CharField(max_length=200)
    ip = models.GenericIPAddressField(protocol='IPv4')
    lag = models.IntegerField()
    description = models.CharField(max_length=200)
    # uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    uid = models.TextField(primary_key=True)
    # upload_date = models.DateTimeField('date uploaded')

    def __str__(self):
        return self.hostname + ' ' + self.lag

    def was_uploaded_recently(self):
        return self.upload_date >= timezone.now() - datetime.timedelta(days=1)

    class Meta:
        # app_label = 'my_db'
        managed = False
        db_table = 'lag_info'


class PortsInfo(models.Model):
    hostname = models.CharField(max_length=200)
    ip = models.GenericIPAddressField(protocol='IPv4')
    interface = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    mtu = models.IntegerField()
    port_bw = models.CharField(max_length=200)
    current_bw = models.CharField(max_length=200)
    sfp_vendor = models.CharField(max_length=200)
    sfp_dist = models.CharField(max_length=200)
    sfp_mode = models.CharField(max_length=200)
    port_mode = models.CharField(max_length=200)
    # uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    uid = models.TextField(primary_key=True)
    # upload_date = models.DateTimeField('date uploaded')

    def __str__(self):
        return self.hostname + ' ' + self.interface

    def was_uploaded_recently(self):
        return self.upload_date >= timezone.now() - datetime.timedelta(days=1)

    class Meta:
        # app_label = 'my_db'
        managed = False
        db_table = 'ports_info'


class VlanInfo(models.Model):
    hostname = models.CharField(max_length=200)
    ip = models.GenericIPAddressField(protocol='IPv4')
    vlan = models.IntegerField()
    description = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    # uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    uid = models.TextField(primary_key=True)
    # upload_date = models.DateTimeField('date uploaded')

    def __str__(self):
        return self.hostname + ' ' + self.vlan

    def was_uploaded_recently(self):
        return self.upload_date >= timezone.now() - datetime.timedelta(days=1)

    class Meta:
        # app_label = 'my_db'
        managed = False
        db_table = 'vlan_info'


class VrfInfo(models.Model):
    hostname = models.CharField(max_length=200)
    ip = models.GenericIPAddressField(protocol='IPv4')
    vrf_type = models.CharField(max_length=200)
    vrf_name = models.CharField(max_length=200)
    protocol = models.IntegerField()
    rd = models.CharField(max_length=200)
    rt_export = models.CharField(max_length=200)
    rt_import = models.CharField(max_length=200)
    diffserv = models.CharField(max_length=200)
    ttl_mode = models.CharField(max_length=200)
    # uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    uid = models.TextField(primary_key=True)
    # upload_date = models.DateTimeField('date uploaded')

    def __str__(self):
        return self.hostname + ' ' + self.vrf_name

    def was_uploaded_recently(self):
        return self.upload_date >= timezone.now() - datetime.timedelta(days=1)

    class Meta:
        # app_label = 'my_db'
        managed = False
        db_table = 'vrf_info'