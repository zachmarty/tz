from django.db import models

class Menu(models.Model):
    id = models.AutoField('id', primary_key=True)
    name = models.CharField('Name', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

class Field(models.Model):
    id = models.AutoField('id', primary_key=True)
    table_id = models.ForeignKey('Menu', on_delete=models.CASCADE)
    name = models.CharField('Name', max_length=50)
    layer = models.IntegerField('Layer')
    parent_field = models.ForeignKey('Field', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Поле'
        verbose_name_plural = 'Поля'