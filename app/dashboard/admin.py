from django.contrib import admin

import dashboard.models


my_tables = [cls for cls in dashboard.models.__dict__.values() if isinstance(cls, type)]

for table in my_tables:
    admin.site.register(table)