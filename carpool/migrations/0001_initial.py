# Generated by Django 4.2.4 on 2023-08-02 05:56

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(default='Unknown', max_length=100)),
                ('seats', models.IntegerField(default=4)),
                ('plate', models.CharField(default='', max_length=10)),
                ('fuel_type', models.CharField(choices=[('gasoline', 'Gasoline'), ('electric', 'Electric'), ('gas', 'Gas'), ('ethanol', 'Ethanol'), ('diesel', 'Diesel')], default='gasoline', max_length=10)),
                ('year', models.IntegerField(default=2023)),
                ('brand', models.CharField(default='Unknown', max_length=50)),
                ('last_maintenance', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_driver', models.BooleanField(default=False)),
                ('bio', models.TextField(blank=True, default='')),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('smoking', models.BooleanField(default=False)),
                ('pets', models.BooleanField(default=False)),
                ('chat', models.BooleanField(default=False)),
                ('music', models.BooleanField(default=False)),
                ('ranking', models.FloatField(default=0)),
                ('rides_given', models.IntegerField(default=0)),
                ('rides_taken', models.IntegerField(default=0)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='carpool_user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='carpool_user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserRoute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_location', models.CharField(default='', max_length=200)),
                ('end_location', models.CharField(default='', max_length=200)),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('max_divert_distance', models.FloatField(default=0, help_text='Maximum distance the user is willing to divert from the route, in km')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_routes', to='carpool.user')),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actual_start_location', models.CharField(default='', max_length=200)),
                ('actual_end_location', models.CharField(default='', max_length=200)),
                ('actual_start_time', models.DateTimeField(blank=True, null=True)),
                ('actual_end_time', models.DateTimeField(blank=True, null=True)),
                ('actual_total_time', models.DurationField(blank=True, null=True)),
                ('total_carpool_tip', models.FloatField(default=0)),
                ('is_finished', models.BooleanField(default=False)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carpool.car')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='driven_trips', to='carpool.user')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='carpool.user'),
        ),
    ]
