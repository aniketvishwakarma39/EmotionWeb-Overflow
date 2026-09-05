from django.core.files.storage import Storage

from vercel.blob import BlobClient


class VercelBlobStorage(Storage):

    def __init__(self):
        self.client = BlobClient()

    def _save(self, name, content):
        file_data = content.read()

        result = self.client.put(
            name,
            file_data,
            access="public",
            add_random_suffix=True,
            content_type=getattr(content, "content_type", None),
        )

        return result.pathname

    def url(self, name):
        result = self.client.head(name)
        return result.url

    def exists(self, name):
        try:
            self.client.head(name)
            return True
        except Exception:
            return False

    def delete(self, name):
        try:
            self.client.delete(name)
        except Exception:
            pass