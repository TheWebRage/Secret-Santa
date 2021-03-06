# Generated by Django 3.1.2 on 2020-11-09 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RandomizeApp', '0003_auto_20201109_0612'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='amazon',
            new_name='amazon_wishlist_link',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='colors',
            new_name='colors_in_home_or_room',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='favorite',
            new_name='favorite_gift_i_have_gotten',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='treat',
            new_name='favorite_treat',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='plenty_of',
            new_name='i_have_plenty_of',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='like_more',
            new_name='i_would_like_more_of',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='pants',
            new_name='pants_size',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='shirt',
            new_name='shirt_size',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='shoes',
            new_name='shoe_size',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='reference',
            new_name='someone_who_knows_what_gifts_i_like',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='want_secretly',
            new_name='something_i_am_hoping_for_christmas_but_have_not_told_anyone',
        ),
    ]
