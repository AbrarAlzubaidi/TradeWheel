# Media folder

- `upload_to` properity pass to it the path that want to upload to
- inside `settings.py` add this `MEDIA_ROOT = os.path.join(BASE_DIR,'assets')` and also this `MEDIA_URL = '/media/'`
- at the end add into `urls.py` inside your project add this (this happen when we in debuging mood not in production mood)
```python
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```

