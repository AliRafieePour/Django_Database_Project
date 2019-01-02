import django_tables2 as tables
from .models import students, admins, dept, dorms, rooms, majors

class studentsTable(tables.Table):
    class Meta:
        model = students
        template_name = 'django_tables2/bootstrap.html'

class adminsTable(tables.Table):
    class Meta:
        model = admins
        template_name = 'django_tables2/bootstrap.html'

class deptTable(tables.Table):
    class Meta:
        model = dept
        template_name = 'django_tables2/bootstrap.html'

class dormsTable(tables.Table):
    class Meta:
        model = dorms
        template_name = 'django_tables2/bootstrap.html'

class roomsTable(tables.Table):
    class Meta:
        model = rooms
        template_name = 'django_tables2/bootstrap.html'
        
        
class majorsTable(tables.Table):
    class Meta:
        model = majors
        template_name = 'django_tables2/bootstrap.html'