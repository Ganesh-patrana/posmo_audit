# Generated by Django 4.1 on 2022-10-03 11:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ClientType",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        primary_key=True,
                        serialize=False,
                        verbose_name="Id",
                    ),
                ),
                ("name", models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="CompanyDetails",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        primary_key=True,
                        serialize=False,
                        verbose_name="Company Id",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=200, null=True, verbose_name="Company Name"
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Is Active"),
                ),
                (
                    "compliance_score",
                    models.FloatField(
                        default=0, verbose_name="Present Compliance Score"
                    ),
                ),
                (
                    "previous_compliance_score",
                    models.FloatField(
                        default=-1, verbose_name="Previous Compliance Score"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="company",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Engagement",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        primary_key=True,
                        serialize=False,
                        verbose_name="Company Id",
                    ),
                ),
                ("name", models.CharField(default="", max_length=100)),
                (
                    "start_Date",
                    models.DateField(auto_now_add=True, verbose_name="Start Date"),
                ),
                ("end_Date", models.DateField()),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Is Active"),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("branding", "branding"),
                            ("positioning", "positioning"),
                            ("both", "both"),
                        ],
                        max_length=70,
                    ),
                ),
                (
                    "compliance_score",
                    models.FloatField(
                        default=0, verbose_name="Present Compliance Score"
                    ),
                ),
                (
                    "previous_compliance_score",
                    models.FloatField(
                        default=-1, verbose_name="Previous Compliance Score"
                    ),
                ),
                (
                    "client_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="configuration.clienttype",
                    ),
                ),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="configuration.companydetails",
                    ),
                ),
            ],
            options={
                "unique_together": {("type", "company")},
            },
        ),
        migrations.CreateModel(
            name="MessageArchitecture",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        primary_key=True,
                        serialize=False,
                        verbose_name="MA Id",
                    ),
                ),
                (
                    "parameter",
                    models.CharField(max_length=200, verbose_name="Parameter Name"),
                ),
                ("keyword", models.CharField(max_length=200, verbose_name="Keyword")),
                (
                    "engagement",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="configuration.engagement",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ChannelType",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        primary_key=True,
                        serialize=False,
                        verbose_name="Channel Type Id",
                    ),
                ),
                (
                    "channel_type",
                    models.CharField(max_length=50, verbose_name="Channel Type"),
                ),
                (
                    "channel_type_weightage",
                    models.FloatField(default=1.0, null=True, verbose_name="Weightage"),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Is Active"),
                ),
                (
                    "engagement",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="engagement_details",
                        to="configuration.engagement",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ChannelName",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "channel_name",
                    models.CharField(max_length=70, verbose_name="Channel Name"),
                ),
                (
                    "channel_type_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="configuration.channeltype",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Channel",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        primary_key=True,
                        serialize=False,
                        verbose_name="Channel Id",
                    ),
                ),
                (
                    "channel_title",
                    models.CharField(
                        max_length=200, null=True, verbose_name="channel_Title"
                    ),
                ),
                ("url", models.URLField(verbose_name="Channel Url")),
                ("is_active", models.BooleanField(default=True)),
                (
                    "compliance_score",
                    models.FloatField(
                        default=0, verbose_name="Present Compliance Score"
                    ),
                ),
                (
                    "previous_compliance_score",
                    models.FloatField(
                        default=-1, verbose_name="Previous Compliance Score"
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "channel_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="configuration.channelname",
                    ),
                ),
                (
                    "engagement",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="configuration.engagement",
                    ),
                ),
                (
                    "type_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="configuration.channeltype",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AuditParameter",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        primary_key=True,
                        serialize=False,
                        verbose_name="Audit Parameter Id",
                    ),
                ),
                (
                    "parameter",
                    models.CharField(max_length=200, verbose_name="Parameter Name"),
                ),
                (
                    "audit_weightage",
                    models.FloatField(
                        default=1.0, null=True, verbose_name="Audit Weightage"
                    ),
                ),
                ("keyword", models.CharField(max_length=200, verbose_name="Keyword")),
                (
                    "engagement",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="configuration.engagement",
                        verbose_name="Engagement Details",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ChannelTypeParameter",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("weight", models.FloatField()),
                (
                    "parameters",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="configuration.auditparameter",
                    ),
                ),
                (
                    "type_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="configuration.channeltype",
                    ),
                ),
            ],
            options={
                "unique_together": {("type_name", "parameters")},
            },
        ),
        migrations.CreateModel(
            name="ChannelSourceParameter",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("weight", models.FloatField()),
                (
                    "channel",
                    models.ForeignKey(
                        max_length=200,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="configuration.channel",
                        verbose_name="Channel Url",
                    ),
                ),
                (
                    "parameters",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="configuration.auditparameter",
                    ),
                ),
            ],
            options={
                "unique_together": {("channel", "parameters")},
            },
        ),
        migrations.CreateModel(
            name="ChannelParameter",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("weight", models.FloatField()),
                (
                    "channel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="channel",
                        to="configuration.channel",
                    ),
                ),
                (
                    "parameters",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="configuration.auditparameter",
                    ),
                ),
            ],
            options={
                "unique_together": {("channel", "parameters")},
            },
        ),
    ]
