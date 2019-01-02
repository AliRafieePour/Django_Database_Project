from django.db import models

# Create your models here.

dept_id = (
        ('ece', 'Electrical and Computer engineering department'),
        ('mec', 'Mechanical Engineering Departement'),
        ('ind', 'Industrial Engineering Department'),
        ('mat', 'Department of Mathematiques'),
        ('phy', 'Department of Physics')
        )



majorss = (
        ('ee', 'Electrical Engineering'),
        ('ce', 'Computer Engineering'),
        ('me', 'Mechanical Engineering'),
        ('ie', 'Industrial Engineering'),
        ('ma', 'Mathematiues'),
        ('ph', 'Physics')
        )




sex = (
       ('fe', 'female'),
       ('ma', 'male')
       )




rolls = (
        ('pr', 'Professor'),
        ('mr', 'Mester'),
        ('ms', 'miss')
        )





types = (
        ('bs', 'bacholers'),
        ('ms', 'masters'),
        ('dr', 'phd')
        )


       
class dept(models.Model):
    name = models.CharField(max_length=300)
    phonenum= models.CharField(max_length=110)
    def __str__(self):
        return self.name
    
        
class majors(models.Model):
    major_id = models.CharField(max_length=2, choices=majorss)
    dept = models.ForeignKey(dept, on_delete=models.CASCADE)
    def __str__(self):
        return self.major_id
    
    
    
class admins(models.Model):
    name = models.CharField(max_length=300)
    major = models.ForeignKey(majors, on_delete=models.CASCADE)
    dept = models.ForeignKey(dept, on_delete=models.CASCADE)
    roll = models.CharField(max_length=300, choices=rolls)
    def __str__(self):
        return self.name
    
   
    

class students(models.Model):
    student_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    major = models.ForeignKey(majors, on_delete=models.CASCADE)
    type_degree = models.CharField(max_length=300, choices = types)
    def __str__(self):
        return (self.first_name+' '+self.last_name)
    
    
    

    
    
class dorms(models.Model):
    dorm_id = models.IntegerField(primary_key=True)
    dorm_name = models.CharField(max_length=300)
    num_rooms = models.IntegerField()
    num_facil = models.IntegerField()
    dorm_admin = models.ForeignKey(admins, on_delete=models.DO_NOTHING)
    phonenum = models.CharField(max_length=11)
    def __str__(self):
        return self.dorm_id
    
    
    
    
  
class rooms(models.Model):
    room_id = models.IntegerField(primary_key=True)
    room_statue = models.BooleanField()
    room_admin = models.ForeignKey(students, on_delete=models.DO_NOTHING, null=True, blank=True)
    def __str__(self):
        return str(self.room_id)
    
 
    
    
    
class workers(models.Model):
    worker_id = models.IntegerField(primary_key=True)
    worker_name = models.CharField(max_length=300)
    worker_duty = models.CharField(max_length=300)
    worker_age = models.IntegerField()
    worker_sex = models.CharField(max_length=2, choices = sex)
def __str__(self):
        return self.worker_name

    
    
    
    
