from django.forms import ModelForm
from . import models

class studentinsertion(ModelForm):
    class Meta:
        model = models.students
        fields = ['student_id', 'first_name', 'last_name', 'major', 'type_degree']
class admininsertion(ModelForm):
    class Meta:
        model = models.admins
        fields = ['name','major','dept','roll']
        
class dorminsertion(ModelForm):
    class Meta:
        model = models.dorms
        fields = ['dorm_id','dorm_name','num_rooms','num_facil', 'dorm_admin', 'phonenum']
        
        
class roominsertion(ModelForm):
    class Meta:
        model = models.rooms
        fields = ['room_id','room_statue','room_admin']
        
        
class majorinsertion(ModelForm):
    class Meta:
        model = models.majors
        fields = ['major_id','dept']

class addadmin(ModelForm):
    class Meta:
        model = models.admins
        fields = ['name','major','dept', 'roll']
        

class updatestudent(ModelForm):
    class Meta:
        model = models.students
        fields = ['student_id','first_name','last_name','major', 'type_degree']
       
class updateroom(ModelForm):
    class Meta:
        model = models.rooms
        fields = ['room_id','room_statue','room_admin']       
