from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ("paperless", "0006_alter_aimodel_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="applicationconfiguration",
            name="vlm_analysis_enabled",
            field=models.BooleanField(
                verbose_name="Enable VLM image understanding",
                null=True,
                blank=True,
            ),
        ),
    ]
