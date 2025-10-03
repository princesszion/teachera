# # common/serializers.py
# class AbsoluteMediaURLMixin:
#     """
#     Automatically replaces relative /media/ paths in ALL string fields
#     with absolute URLs (using request.build_absolute_uri).
#     """

#     def to_representation(self, instance):
#         data = super().to_representation(instance)

#         request = self.context.get("request")  # ✅ DRF gives request if you pass context
#         if request:
#             base_url = request.build_absolute_uri("/")[:-1]  # e.g. http://127.0.0.1:8000
#         else:
#             # fallback (rare, if request missing)
#             from django.conf import settings
#             base_url = "http://127.0.0.1:8000" if settings.DEBUG else "https://teach-era.com"

#         def fix_value(value):
#             if isinstance(value, str) and "/media/" in value:
#                 return value.replace("/media/", f"{base_url}/media/")
#             return value

#         for key, value in data.items():
#             if isinstance(value, str):
#                 data[key] = fix_value(value)
#             elif isinstance(value, list):
#                 data[key] = [fix_value(v) for v in value]
#             elif isinstance(value, dict):
#                 data[key] = {k: fix_value(v) for k, v in value.items()}
#         print(">>> Serializer Output (after fix):", data)
#         return data


# common/serializers.py
import re

class AbsoluteMediaURLMixin:
    """
    Ensures:
    - File/ImageField values (e.g. 'nominations/APIs.jpeg') -> absolute URL
    - HTML fields with <img src="/media/..."> -> replace with absolute URL
    """

    def to_representation(self, instance):
        data = super().to_representation(instance)

        request = self.context.get("request")
        if request:
            base_url = request.build_absolute_uri("/")[:-1]  # e.g. http://127.0.0.1:8000
        else:
            from django.conf import settings
            base_url = "http://127.0.0.1:8000" if settings.DEBUG else "https://teach-era.com"

        def fix_file_field(value: str):
            """Handle real ImageField/FileField values."""
            if not value:
                return value
            if value.startswith("http://") or value.startswith("https://"):
                return value
            if value.startswith("/media/"):
                return f"{base_url}{value}"
            if value.startswith("media/"):
                return f"{base_url}/{value}"
            if value.startswith("nominations/"):
                return f"{base_url}/media/{value}"
            return value

        def fix_html(value: str):
            """Replace <img src="/media/..."> inside rich text HTML."""
            if not isinstance(value, str):
                return value
            return re.sub(
                r'src="(/media/[^"]+)"',
                lambda m: f'src="{base_url}{m.group(1)}"',
                value,
            )

        for key, value in data.items():
            if key == "photo":  # ✅ Only fix file/image fields here
                data[key] = fix_file_field(value)
            elif isinstance(value, str):  # ✅ For text/HTML fields
                data[key] = fix_html(value)
            elif isinstance(value, list):
                data[key] = [fix_html(v) for v in value]
            elif isinstance(value, dict):
                data[key] = {k: fix_html(v) for k, v in value.items()}

        return data
