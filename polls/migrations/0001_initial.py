# Generated by Django 2.1.3 on 2018-11-25 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userNum', models.IntegerField(unique=True)),
                ('userAge', models.IntegerField(default=0)),
                ('userGender', models.CharField(default='', max_length=3)),
                ('userEducation', models.CharField(default='', max_length=3)),
                ('userIncome', models.CharField(default='', max_length=3)),
                ('userCountry', models.ManyToManyField(to='polls.Country')),
                ('userLanguage', models.ManyToManyField(to='polls.Language')),
                ('userOther', models.ManyToManyField(to='polls.Other')),
            ],
        ),
        migrations.CreateModel(
            name='Votable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.User')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('votable_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='polls.Votable')),
            ],
            options={
                'ordering': ['text'],
            },
            bases=('polls.votable',),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('votable_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='polls.Votable')),
                ('commentCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Category')),
            ],
            bases=('polls.votable',),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('votable_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='polls.Votable')),
            ],
            bases=('polls.votable',),
        ),
        migrations.AddField(
            model_name='vote',
            name='votable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Votable'),
        ),
        migrations.AddField(
            model_name='user',
            name='userVotes',
            field=models.ManyToManyField(through='polls.Vote', to='polls.Votable'),
        ),
        migrations.AddField(
            model_name='question',
            name='questionUser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='polls.User'),
        ),
        migrations.AddField(
            model_name='comment',
            name='commentQuestion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Question'),
        ),
        migrations.AddField(
            model_name='comment',
            name='commentUser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='polls.User'),
        ),
        migrations.AddField(
            model_name='category',
            name='categoryQuestion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Question'),
        ),
    ]
