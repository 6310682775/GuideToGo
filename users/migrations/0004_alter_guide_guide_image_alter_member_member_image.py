# Generated by Django 4.1.1 on 2022-11-06 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_guide_guide_image_alter_member_member_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guide',
            name='guide_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/guide/'),
        ),
        migrations.AlterField(
            model_name='member',
            name='member_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/member/'),
        ),
    ]
