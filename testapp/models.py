from typing import List

from django.db import models

from gpp.django.fields import CompressedTextField
from gpp.django.mixins import BaseModelMixin, ArchiveModelMixin, TaskModelMixin


class AllFieldMixin(models.Model):
    booleanfield = models.BooleanField('BooleanField', null=False, blank=False)
    charfield = models.CharField('CharField', null=False, blank=False, max_length=100)
    # commaseparatedintegerfield = models.CommaSeparatedIntegerField('CommaSeparatedIntegerField', null=False, blank=False, max_length=100,)
    datefield = models.DateField('DateField', null=False, blank=False)
    datetimefield = models.DateTimeField('DateTimeField', null=False, blank=False)
    decimalfield = models.DecimalField('DecimalField', null=False, blank=False, max_digits=30, decimal_places=10)
    durationfield = models.DurationField('DurationField', null=False, blank=False)
    emailfield = models.EmailField('EmailField', null=False, blank=False)
    filepathfield = models.FilePathField('FilePathField', null=False, blank=False)
    floatfield = models.FloatField('FloatField', null=False, blank=False)
    integerfield = models.IntegerField('IntegerField', null=False, blank=False)
    bigintegerfield = models.BigIntegerField('BigIntegerField', null=False, blank=False)
    smallintegerfield = models.SmallIntegerField('SmallIntegerField', null=False, blank=False)
    genericipaddressfield = models.GenericIPAddressField('GenericIPAddressField', null=False, blank=False)
    # nullbooleanfield = models.NullBooleanField('NullBooleanField', null=False, blank=False)
    positivebigintegerfield = models.PositiveBigIntegerField('PositiveBigIntegerField', null=False, blank=False)
    positiveintegerfield = models.PositiveIntegerField('PositiveIntegerField', null=False, blank=False)
    positivesmallintegerfield = models.PositiveSmallIntegerField('PositiveSmallIntegerField', null=False, blank=False)
    slugfield = models.SlugField('SlugField', null=False, blank=False)
    textfield = models.TextField('TextField', null=False, blank=False)
    timefield = models.TimeField('TimeField', null=False, blank=False)
    urlfield = models.URLField('URLField', null=False, blank=False)
    binaryfield = models.BinaryField('BinaryField', null=False, blank=False)
    uuidfield = models.UUIDField('UUIDField', null=False, blank=False)
    compressefield = CompressedTextField('CompressedTextField', max_length=10*1024, null=False, blank=False)

    class Meta:
        abstract = True


class AllFieldModel(BaseModelMixin, AllFieldMixin):

    class Meta:
        verbose_name = 'Test Model'
        verbose_name_plural = 'Test Models'

    @classmethod
    def check_field_list(cls) -> List[str]:
        return [
            'booleanfield',
            'charfield',
            # 'commaseparatedintegerfield',
            'datefield',
            'datetimefield',
            'decimalfield',
            'durationfield',
            'emailfield',
            'filepathfield',
            'floatfield',
            'integerfield',
            'bigintegerfield',
            'smallintegerfield',
            'genericipaddressfield',
            # 'nullbooleanfield',
            'positivebigintegerfield',
            'positiveintegerfield',
            'positivesmallintegerfield',
            'slugfield',
            'textfield',
            'timefield',
            'urlfield',
            'binaryfield',
            'uuidfield',
            'created',
            'modified',
            'compressefield',
        ]


class ArchivedAllFieldModel(ArchiveModelMixin, BaseModelMixin, AllFieldMixin):

    class Meta:
        verbose_name = 'Test Model'
        verbose_name_plural = 'Test Models'


class TaskModel(BaseModelMixin, TaskModelMixin):

    class Meta:
        verbose_name = 'Test Test Model'
        verbose_name_plural = 'Test Test Models'
