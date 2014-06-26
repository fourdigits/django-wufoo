from django.db import models

class WufooForm(models.Model):
    name = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ['id']
        
class WufooField(models.Model):
    wufoo_id = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    field_type = models.CharField(max_length=255, null=True, blank=True)
    form = models.ForeignKey(WufooForm)
    
    def __unicode__(self):
        return self.title
    
    class Meta:
        ordering = ['id']
        
class WufooSubField(models.Model):
    wufoo_id = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    default_val = models.CharField(max_length=255)
    field = models.ForeignKey(WufooField)
    
    def __unicode__(self):
        return self.label
    
    class Meta:
        ordering = ['id']
        verbose_name = 'Wufoo subfield'
        verbose_name_plural = 'Wufoo subfields'

class WufooEntry(models.Model):
    entry_id = models.CharField(max_length=255)
    form = models.ForeignKey(WufooForm)
    
    def __unicode__(self):
        return self.entry_id
    
    class Meta:
        verbose_name_plural = 'Wufoo entries'

class WufooFieldEntry(models.Model):
    wufoo_entry = models.ForeignKey(WufooEntry)
    field = models.ForeignKey(WufooField)
    subfield = models.ForeignKey(WufooSubField, blank=True, null=True)
    value = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.value
    
    class Meta:
        ordering = ['field', 'subfield']
        verbose_name_plural = 'Wufoo field entries'