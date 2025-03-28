from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Packagetype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('packagename', models.CharField(max_length=200, null=True)),
                ('creationdate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Paymenthistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.IntegerField(choices=[(1, 'New'), (2, 'Partial'), (3, 'Full')], default=1)),
                ('creationdate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='bookingDate',
            new_name='creationdate',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='categoryName',
            new_name='categoryname',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='creationDate',
            new_name='creationdate',
        ),
        migrations.RenameField(
            model_name='package',
            old_name='creationDate',
            new_name='creationdate',
        ),
        migrations.RenameField(
            model_name='package',
            old_name='PackageName',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='signup',
            old_name='creationDate',
            new_name='creationdate',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='payment',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='paymentType',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='user',
        ),
        migrations.AddField(
            model_name='booking',
            name='bookingnumber',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='register',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gym.signup'),
        ),
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.IntegerField(choices=[(1, 'New'), (2, 'Partial'), (3, 'Full')], default=1),
        ),
        migrations.AddField(
            model_name='package',
            name='packageduration',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='package',
            name='price',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='package',
            name='titlename',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='package',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gym.package'),
        ),
        migrations.DeleteModel(
            name='AddPackage',
        ),
        migrations.AddField(
            model_name='paymenthistory',
            name='booking',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gym.booking'),
        ),
        migrations.AddField(
            model_name='paymenthistory',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gym.signup'),
        ),
        migrations.AddField(
            model_name='packagetype',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gym.category'),
        ),
        migrations.AddField(
            model_name='package',
            name='packagename',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gym.packagetype'),
        ),
    ]
