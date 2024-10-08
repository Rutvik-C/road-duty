# Generated by Django 3.1 on 2022-11-20 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Challan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_number', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('amount', models.IntegerField(default=0)),
                ('date_time', models.DateTimeField(blank=True, editable=False, null=True)),
                ('locations', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Rider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=50)),
                ('challan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roadduty.challan')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alt', models.TextField(blank=True, max_length=250)),
                ('image', models.ImageField(default='posts/default.jpg', upload_to='images/')),
                ('slug', models.SlugField(default='title', max_length=250, unique_for_date='created')),
                ('challan', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='roadduty.challan')),
            ],
        ),
        migrations.AddField(
            model_name='challan',
            name='rider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roadduty.rider'),
        ),
    ]
