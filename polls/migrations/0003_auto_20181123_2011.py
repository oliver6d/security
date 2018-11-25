# Generated by Django 2.1.3 on 2018-11-24 01:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20181119_0442'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('countryText', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('educationText', models.CharField(default='', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genderText', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('incomeText', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('languageText', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Other',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otherText', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userID', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('userAge', models.IntegerField(default=0)),
                ('userCountry', models.ManyToManyField(to='polls.Country')),
                ('userEducation', models.ManyToManyField(to='polls.Education')),
                ('userGender', models.ManyToManyField(to='polls.Gender')),
                ('userIncome', models.ManyToManyField(to='polls.Income')),
                ('userLanguage', models.ManyToManyField(to='polls.Language')),
                ('userOther', models.ManyToManyField(to='polls.Other')),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='userVotes',
        ),
        migrations.AlterField(
            model_name='comment',
            name='commentUser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='polls.User'),
        ),
        migrations.AlterField(
            model_name='question',
            name='questionUser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='polls.User'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.User'),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.AddField(
            model_name='user',
            name='userVotes',
            field=models.ManyToManyField(through='polls.Vote', to='polls.Votable'),
        ),
    ]