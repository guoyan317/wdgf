from django.db import models

# Create your models here.
TAO_LU_TYPE = (
    (0, '单一'),
    (1, '混合'),
    (2, '自编'),
)


# 武当门派
class School(models.Model):
    name = models.CharField(max_length=20)
    headmaster = models.CharField(max_length=20)

    class Meta:
        db_table = 'wd_gf_school'
        verbose_name_plural = '门派'

    def __unicode__(self):
        return '{0}'.format(self.name)


# 武器
class Weapon(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'wd_gf_weapon'
        verbose_name_plural = '武器'

    def __unicode__(self):
        return '{0}'.format(self.name)


# 武当功夫套路
class TaoLu(models.Model):
    name = models.CharField(max_length=20)
    type = models.IntegerField(choices=TAO_LU_TYPE, default=0)
    school = models.ForeignKey('School')
    weapon = models.ForeignKey('Weapon')
    sword_spectrum = models.TextField(max_length=300, null=True, blank=True)

    class Meta:
        db_table = 'wd_gf_tao_lu'
        verbose_name_plural = '功夫套路'

    def __unicode__(self):
        return '{0}'.format(self.name)