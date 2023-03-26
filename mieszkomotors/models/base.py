from django.db import models
import os

RENEWAL_INTERVAL = 30

def get_upload_path(instance, filename):
	return os.path.join("documents",
        f"{instance.owner.first_name}_{instance.owner.last_name}", filename
    )

class PublicationTracker(models.Model):
    publication_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey("auth.User", on_delete=models.PROTECT)

    class Meta:
        abstract = True
