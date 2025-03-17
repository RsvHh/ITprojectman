from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0002_auto_20230518_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.IntegerField(choices=[(1, 'Not Updated Yet'), (2, 'Partial Payment'), (3, 'Full Payment')], default=1),
        ),
        migrations.AlterField(
            model_name='paymenthistory',
            name='status',
            field=models.IntegerField(choices=[(1, 'Not Updated Yet'), (2, 'Partial Payment'), (3, 'Full Payment')], default=1),
        ),
    ]
