# Generated by Django 3.2.5 on 2021-07-29 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markets', '0004_auto_20210728_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='change24h',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='close',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='high',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='industry',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='low',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='marketCap',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='numOfShares',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='open',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='price',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='sector',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='volume',
            field=models.FloatField(null=True),
        ),
    ]
