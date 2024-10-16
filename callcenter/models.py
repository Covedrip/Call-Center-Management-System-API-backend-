from django.db import models

# Create your models here.

class Agent(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    department = models.CharField(max_length=50, choices=[('Customer Service', 'Customer Service'), ('Sales', 'Sales'), ('Tech Support', 'Tech Support')])
    role = models.CharField(max_length=50, choices=[('Admin', 'Admin'), ('Supervisor', 'Supervisor'), ('Agent', 'Agent')])
    status = models.CharField(max_length=50, choices=[('active', 'Active'), ('inactive', 'Inactive')])

class Shift(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    shift_type = models.CharField(max_length=50, choices=[('morning', 'Morning'), ('evening', 'Evening'), ('night', 'Night')])
    status = models.CharField(max_length=50, choices=[('assigned', 'Assigned'), ('completed', 'Completed'), ('missed', 'Missed')], default='assigned')

class Availability(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    available_from = models.DateTimeField()
    available_to = models.DateTimeField()
    notes = models.TextField(null=True, blank=True)

class TimeOff(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    request_date = models.DateField(auto_now_add=True)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending')

class ShiftSwap(models.Model):
    agent_requesting = models.ForeignKey(Agent, related_name='agent_requesting', on_delete=models.CASCADE)
    agent_accepting = models.ForeignKey(Agent, related_name='agent_accepting', on_delete=models.CASCADE)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending')
    request_date = models.DateTimeField(auto_now_add=True)

class ShiftLog(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    clock_in_time = models.DateTimeField(null=True, blank=True)
    clock_out_time = models.DateTimeField(null=True, blank=True)
    total_hours_worked = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def calculate_worked_hours(self):
        if self.clock_in_time and self.clock_out_time:
            time_diff = self.clock_out_time - self.clock_in_time
            self.total_hours_worked = time_diff.total_seconds() / 3600
            self.save()


