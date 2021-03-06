from django.db import models

class devices(models.Model):
    device_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    user_email = models.CharField(max_length=100)
    local_ip= models.CharField(max_length=100,null=True)
    mac_address=models.CharField(max_length=100,null=True)

    def __str__(self):
          return self.mac_address

    def save(self, *args, **kwargs):
        #Check the MAC address and update database
        flag = devices.objects.all().filter(mac_address=self.mac_address)
        if not flag:
            temp = True
        else:
            temp = False
        if not flag:
            # Calling the superclass method to save data
            super().save(*args, **kwargs)
            print ("Device registered successfully.")
        else:
            print ("Device already registered.")
            return temp
        print (temp)

class data(models.Model):
    device = models.ForeignKey(devices, on_delete=models.CASCADE)
    values = models.FileField(blank=True, null=True)
    created_date = models.DateTimeField(null=True,auto_now_add=True)

    def __str__(self):
        return str(self.device)

class real_time_data(models.Model):
    device = models.ForeignKey(devices, on_delete=models.CASCADE)
    created_date = models.DateTimeField(null=True,auto_now_add=True)
    heart_rate = models.IntegerField(default=0)
    EEG_reading = models.IntegerField(default=0)

    def __str__(self):
        return str(self.created_date)
