# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class App(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    appid = models.CharField(db_column='AppId', max_length=500)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=500)  # Field name made lowercase.
    orgid = models.CharField(db_column='OrgId', max_length=32)  # Field name made lowercase.
    orgname = models.CharField(db_column='OrgName', max_length=64)  # Field name made lowercase.
    ownername = models.CharField(db_column='OwnerName', max_length=500)  # Field name made lowercase.
    owneremail = models.CharField(db_column='OwnerEmail', max_length=500)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted', default=False)  # Field name made lowercase. This field type is a guess.
    datachange_createdby = models.CharField(db_column='DataChange_CreatedBy', max_length=32)  # Field name made lowercase.
    datachange_createdtime = models.DateTimeField(db_column='DataChange_CreatedTime')  # Field name made lowercase.
    datachange_lastmodifiedby = models.CharField(db_column='DataChange_LastModifiedBy', max_length=32, blank=True, null=True)  # Field name made lowercase.
    datachange_lasttime = models.DateTimeField(db_column='DataChange_LastTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'App'


class Appnamespace(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=32)  # Field name made lowercase.
    appid = models.CharField(db_column='AppId', max_length=32)  # Field name made lowercase.
    format = models.CharField(db_column='Format', max_length=32)  # Field name made lowercase.
    ispublic = models.TextField(db_column='IsPublic')  # Field name made lowercase. This field type is a guess.
    comment = models.CharField(db_column='Comment', max_length=64)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted', default=False)  # Field name made lowercase. This field type is a guess.
    datachange_createdby = models.CharField(db_column='DataChange_CreatedBy', max_length=32)  # Field name made lowercase.
    datachange_createdtime = models.DateTimeField(db_column='DataChange_CreatedTime')  # Field name made lowercase.
    datachange_lastmodifiedby = models.CharField(db_column='DataChange_LastModifiedBy', max_length=32, blank=True, null=True)  # Field name made lowercase.
    datachange_lasttime = models.DateTimeField(db_column='DataChange_LastTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AppNamespace'


class Authorities(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=50)  # Field name made lowercase.
    authority = models.CharField(db_column='Authority', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Authorities'


class Consumer(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    appid = models.CharField(db_column='AppId', max_length=500)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=500)  # Field name made lowercase.
    orgid = models.CharField(db_column='OrgId', max_length=32)  # Field name made lowercase.
    orgname = models.CharField(db_column='OrgName', max_length=64)  # Field name made lowercase.
    ownername = models.CharField(db_column='OwnerName', max_length=500)  # Field name made lowercase.
    owneremail = models.CharField(db_column='OwnerEmail', max_length=500)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase. This field type is a guess.
    datachange_createdby = models.CharField(db_column='DataChange_CreatedBy', max_length=32)  # Field name made lowercase.
    datachange_createdtime = models.DateTimeField(db_column='DataChange_CreatedTime')  # Field name made lowercase.
    datachange_lastmodifiedby = models.CharField(db_column='DataChange_LastModifiedBy', max_length=32, blank=True, null=True)  # Field name made lowercase.
    datachange_lasttime = models.DateTimeField(db_column='DataChange_LastTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Consumer'


class Consumeraudit(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    consumerid = models.PositiveIntegerField(db_column='ConsumerId', blank=True, null=True)  # Field name made lowercase.
    uri = models.CharField(db_column='Uri', max_length=1024)  # Field name made lowercase.
    method = models.CharField(db_column='Method', max_length=16)  # Field name made lowercase.
    datachange_createdtime = models.DateTimeField(db_column='DataChange_CreatedTime')  # Field name made lowercase.
    datachange_lasttime = models.DateTimeField(db_column='DataChange_LastTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ConsumerAudit'


class Consumerrole(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    consumerid = models.PositiveIntegerField(db_column='ConsumerId', blank=True, null=True)  # Field name made lowercase.
    roleid = models.PositiveIntegerField(db_column='RoleId', blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase. This field type is a guess.
    datachange_createdby = models.CharField(db_column='DataChange_CreatedBy', max_length=32, blank=True, null=True)  # Field name made lowercase.
    datachange_createdtime = models.DateTimeField(db_column='DataChange_CreatedTime')  # Field name made lowercase.
    datachange_lastmodifiedby = models.CharField(db_column='DataChange_LastModifiedBy', max_length=32, blank=True, null=True)  # Field name made lowercase.
    datachange_lasttime = models.DateTimeField(db_column='DataChange_LastTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ConsumerRole'


class Consumertoken(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    consumerid = models.PositiveIntegerField(db_column='ConsumerId', blank=True, null=True)  # Field name made lowercase.
    token = models.CharField(db_column='Token', unique=True, max_length=128)  # Field name made lowercase.
    expires = models.DateTimeField(db_column='Expires')  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase. This field type is a guess.
    datachange_createdby = models.CharField(db_column='DataChange_CreatedBy', max_length=32)  # Field name made lowercase.
    datachange_createdtime = models.DateTimeField(db_column='DataChange_CreatedTime')  # Field name made lowercase.
    datachange_lastmodifiedby = models.CharField(db_column='DataChange_LastModifiedBy', max_length=32, blank=True, null=True)  # Field name made lowercase.
    datachange_lasttime = models.DateTimeField(db_column='DataChange_LastTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ConsumerToken'


class Favorite(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    userid = models.CharField(db_column='UserId', max_length=32)  # Field name made lowercase.
    appid = models.CharField(db_column='AppId', max_length=500)  # Field name made lowercase.
    position = models.IntegerField(db_column='Position')  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase. This field type is a guess.
    datachange_createdby = models.CharField(db_column='DataChange_CreatedBy', max_length=32)  # Field name made lowercase.
    datachange_createdtime = models.DateTimeField(db_column='DataChange_CreatedTime')  # Field name made lowercase.
    datachange_lastmodifiedby = models.CharField(db_column='DataChange_LastModifiedBy', max_length=32, blank=True, null=True)  # Field name made lowercase.
    datachange_lasttime = models.DateTimeField(db_column='DataChange_LastTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Favorite'


class Permission(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    permissiontype = models.CharField(db_column='PermissionType', max_length=32)  # Field name made lowercase.
    targetid = models.CharField(db_column='TargetId', max_length=256)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase. This field type is a guess.
    datachange_createdby = models.CharField(db_column='DataChange_CreatedBy', max_length=32)  # Field name made lowercase.
    datachange_createdtime = models.DateTimeField(db_column='DataChange_CreatedTime')  # Field name made lowercase.
    datachange_lastmodifiedby = models.CharField(db_column='DataChange_LastModifiedBy', max_length=32, blank=True, null=True)  # Field name made lowercase.
    datachange_lasttime = models.DateTimeField(db_column='DataChange_LastTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Permission'


class Role(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    rolename = models.CharField(db_column='RoleName', max_length=256)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase. This field type is a guess.
    datachange_createdby = models.CharField(db_column='DataChange_CreatedBy', max_length=32)  # Field name made lowercase.
    datachange_createdtime = models.DateTimeField(db_column='DataChange_CreatedTime')  # Field name made lowercase.
    datachange_lastmodifiedby = models.CharField(db_column='DataChange_LastModifiedBy', max_length=32, blank=True, null=True)  # Field name made lowercase.
    datachange_lasttime = models.DateTimeField(db_column='DataChange_LastTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Role'


class Rolepermission(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    roleid = models.PositiveIntegerField(db_column='RoleId', blank=True, null=True)  # Field name made lowercase.
    permissionid = models.PositiveIntegerField(db_column='PermissionId', blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase. This field type is a guess.
    datachange_createdby = models.CharField(db_column='DataChange_CreatedBy', max_length=32, blank=True, null=True)  # Field name made lowercase.
    datachange_createdtime = models.DateTimeField(db_column='DataChange_CreatedTime')  # Field name made lowercase.
    datachange_lastmodifiedby = models.CharField(db_column='DataChange_LastModifiedBy', max_length=32, blank=True, null=True)  # Field name made lowercase.
    datachange_lasttime = models.DateTimeField(db_column='DataChange_LastTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RolePermission'


class Serverconfig(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    key = models.CharField(db_column='Key', max_length=64)  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=2048)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase. This field type is a guess.
    datachange_createdby = models.CharField(db_column='DataChange_CreatedBy', max_length=32)  # Field name made lowercase.
    datachange_createdtime = models.DateTimeField(db_column='DataChange_CreatedTime')  # Field name made lowercase.
    datachange_lastmodifiedby = models.CharField(db_column='DataChange_LastModifiedBy', max_length=32, blank=True, null=True)  # Field name made lowercase.
    datachange_lasttime = models.DateTimeField(db_column='DataChange_LastTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ServerConfig'


class Userrole(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    userid = models.CharField(db_column='UserId', max_length=128, blank=True, null=True)  # Field name made lowercase.
    roleid = models.PositiveIntegerField(db_column='RoleId', blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted', default=False)  # Field name made lowercase. This field type is a guess.
    datachange_createdby = models.CharField(db_column='DataChange_CreatedBy', max_length=32, blank=True, null=True)  # Field name made lowercase.
    datachange_createdtime = models.DateTimeField(db_column='DataChange_CreatedTime')  # Field name made lowercase.
    datachange_lastmodifiedby = models.CharField(db_column='DataChange_LastModifiedBy', max_length=32, blank=True, null=True)  # Field name made lowercase.
    datachange_lasttime = models.DateTimeField(db_column='DataChange_LastTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UserRole'


class Users(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=64)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=64)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=64)  # Field name made lowercase.
    enabled = models.IntegerField(db_column='Enabled', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Users'
