# Generated by Django 3.0.5 on 2021-01-15 13:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileEdit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education', models.CharField(max_length=100)),
                ('stream', models.CharField(max_length=100)),
                ('company', models.CharField(default=' ', max_length=200, null=True)),
                ('current_position', models.CharField(default=' ', max_length=200, null=True)),
                ('country', models.CharField(default=' ', max_length=100, null=True)),
                ('location', models.CharField(default=' ', max_length=150, null=True)),
                ('experience', models.CharField(default='Fresher', max_length=100, null=True)),
                ('skills', models.CharField(default=' ', max_length=500)),
                ('interests', models.CharField(default=' ', max_length=100)),
                ('contact', models.CharField(default=' ', max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('post_title', models.CharField(default='', max_length=60)),
                ('heading', models.CharField(default='', max_length=100)),
                ('content', models.CharField(default='', max_length=1000)),
                ('pub_date', models.DateField()),
                ('thumbnail', models.ImageField(default='', null=True, upload_to='')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('likes', models.ManyToManyField(related_name='post_likes', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(choices=[('Like', 'Like'), ('Unlike', 'Unlike')], default='Like', max_length=10)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='accounts.Post')),
            ],
        ),
    ]
