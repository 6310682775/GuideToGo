# Generated by Django 4.1.1 on 2022-11-26 17:01

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('article_image', models.ImageField(blank=True, null=True, upload_to='images/article/')),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('post_date', models.DateField(auto_now_add=True)),
                ('category', models.CharField(choices=[('HOTEL', 'HOTEL'), ('CAFE', 'CAFE'), ('NATURAL', 'NATURAL'), ('LANDMARK', 'LANDMARK'), ('BEACH', 'BEACH'), ('MOUNTAIN', 'MOUNTAIN'), ('CAMPING', 'CAMPING'), ('FOREST', 'FOREST'), ('TOUR', 'TOUR'), ('PARTY', 'PARTY'), ('FAMILY', 'FAMILY'), ('ALL', 'ALL')], default='ALL', max_length=10)),
                ('snippet', models.CharField(max_length=255)),
            ],
        ),
    ]
