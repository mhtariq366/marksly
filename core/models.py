from django.db import models

class Institute(models.Model):
    institute_name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.institute_name

class Subject(models.Model):
    subject_name = models.CharField(max_length=250)
    total_marks = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject_name

class Group(models.Model):
    group_name = models.CharField(max_length=250)
    subjects = models.ManyToManyField(Subject)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.group_name

class Student(models.Model):
    student_name = models.CharField(max_length=250)
    roll_no = models.CharField(max_length=100)
    session = models.CharField(max_length=100)
    dob = models.DateField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.FloatField()

    def __str__(self):
        return f'{self.student.name} - {self.subject.name} - {self.marks}'



