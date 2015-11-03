from django.db import models



class Good(models.Model):

    
	name = models.CharField(max_length=125, null=True, blank= True)
	description = models.TextField(null=True, blank= True)
	available_q = models.IntegerField(default=0)
	price = models.IntegerField(default=0, null=True, blank= True)
	add_date = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)
	slug = models.SlugField()
	active = models.BooleanField(default=True)
	
	def __unicode__(self):
		return self.name
	class Meta:
		ordering = ["name",]




class Photo(models.Model):
    
	product = models.ForeignKey(Good)
	image = models.ImageField(upload_to='photos', blank=True, null=True, default=None)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __unicode__(self):
		return '%s' % self.image 

