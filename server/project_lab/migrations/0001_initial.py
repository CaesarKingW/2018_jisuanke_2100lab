# Generated by Django 2.1 on 2018-08-23 10:36

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('Supermanager', models.BooleanField(default=False)),
                ('Manage_course', models.BooleanField(default=False)),
                ('Manage_user', models.BooleanField(default=False)),
                ('Manage_message', models.BooleanField(default=False)),
                ('Manage_order', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
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
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('brief_introduction', models.TextField(verbose_name='简介')),
                ('audio', models.FileField(blank=True, null=True, upload_to='audio/', verbose_name='音频')),
                ('whole_introduction', models.FileField(blank=True, null=True, upload_to='word/', verbose_name='详解')),
                ('Is_distory', models.BooleanField(default=False, verbose_name='是否阅后即焚')),
                ('distory_time', models.DurationField(blank=True, null=True, verbose_name='可阅时长')),
                ('Is_free', models.BooleanField(default=True, verbose_name='免费')),
                ('price', models.FloatField(blank=True, default=0.0, null=True, verbose_name='价格')),
                ('sale_count', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='销量')),
                ('view_count', models.PositiveIntegerField(default=0, verbose_name='观看量')),
                ('share_rate', models.FloatField(blank=True, null=True, verbose_name='分销比例')),
                ('can_comment', models.BooleanField(default=True, verbose_name='允许用户留言')),
            ],
        ),
        migrations.CreateModel(
            name='Course_picture',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('course_picture', models.ImageField(blank=True, null=True, upload_to='course_picture', verbose_name='课程图片')),
                ('start_time', models.DurationField(verbose_name='')),
                ('end_time', models.DurationField(verbose_name='')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_lab.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Cover_picture',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Cover_picture', models.ImageField(blank=True, null=True, upload_to='course_picture', verbose_name='课程图片')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_lab.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('praise_count', models.IntegerField(default=0)),
                ('exists', models.BooleanField(default=True)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_lab.Course', verbose_name='课程编号')),
            ],
        ),
        migrations.CreateModel(
            name='Operating_history',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('operate_type', models.CharField(max_length=50, verbose_name='操作类型')),
                ('object_type', models.CharField(max_length=50, verbose_name='操作对象')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('manager_username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('Order_number', models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='订单号')),
                ('amount_of_money', models.FloatField(verbose_name='支付金额')),
                ('status', models.CharField(max_length=10, verbose_name='订单状态')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_lab.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Praise',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('message_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_lab.Message', verbose_name='留言编号')),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('message_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_lab.Message', verbose_name='留言编号')),
            ],
        ),
        migrations.CreateModel(
            name='Takes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('start_time', models.DateTimeField(auto_now_add=True, verbose_name='开始学习时间')),
                ('last_study_percent', models.DurationField(default=0, verbose_name='上次学习进度条')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_lab.Course')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('phone_number', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('user_name', models.CharField(blank=True, max_length=15, null=True)),
                ('head_protrait', models.ImageField(blank=True, null=True, upload_to='user_photos')),
                ('welfare', models.FloatField(default=0.0)),
                ('Can_comment', models.BooleanField(default=True)),
                ('Is_teacher', models.BooleanField(default=False)),
                ('exists', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='takes',
            name='user_phone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_lab.User'),
        ),
        migrations.AddField(
            model_name='reply',
            name='user_phone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_lab.User', verbose_name='用户号码'),
        ),
        migrations.AddField(
            model_name='praise',
            name='user_phone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_lab.User', verbose_name='用户号码'),
        ),
        migrations.AddField(
            model_name='order',
            name='user_phone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_lab.User'),
        ),
        migrations.AddField(
            model_name='message',
            name='user_phone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_lab.User', verbose_name='用户号码'),
        ),
    ]
