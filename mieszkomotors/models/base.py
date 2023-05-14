import os

from django.db import models


RENEWAL_INTERVAL = 30

def get_upload_path_enterprise_owner(instance, filename):
    return os.path.join("documents",
            f"{instance.customer}", filename
        )

def get_upload_path(instance, filename):
    return os.path.join("documents",
            f"{instance.customer}", filename
        )

def get_file_name(filename):
    return os.path.basename(filename)
             

class PublicationTracker(models.Model):
    publication_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey("auth.User", on_delete=models.PROTECT, default=1)

    class Meta:
        abstract = True
