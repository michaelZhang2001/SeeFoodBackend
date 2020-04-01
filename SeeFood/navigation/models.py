from django.db import models

# Create your models here.

class Restaurant(models.Model):
	res_type = [('FF','Fast Food'),('CD','Casual Dining'),('ET','Ethnic'),('NA','Not Indicated')]
	name = models.CharField(max_length=100)
	restaurant_type = models.CharField(choices = res_type, default = 'NA', max_length = 2)
	description = models.TextField(max_length = 10000, default = 'A SeeFood restaurant')
	seefood_rating = models.DecimalField(max_digits = 3,decimal_places = 1, help_text = 'the rating uniquely given by SeeFood', default = 5)
	class Meta:
		ordering = ["name"]

	def __str__(self):
		return self.name


class Allergen(models.Model):

	name = models.CharField(max_length = 50)

	def __str__(self):
		return self.name


class FoodItem(models.Model):

	food_type = [('B','Beef'),('C','Chicken'),('P','Pork')]	#list of tuples, in the form of (reference name/abbr., full name)
	classifications = [('VE','Vegan'),('GF','Gluten Free'),('DF','Not Specified')]	#same as above
	name = models.CharField(max_length = 100)
	generic_name = models.CharField(choices= food_type, max_length=2)	#max_length for the max length of the reference name, default using reference name
	calories = models.IntegerField()
	fat = models.IntegerField()
	carb = models.IntegerField()
	protein = models.IntegerField()
	restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)	#foreign key to create restaurant menu
	classification = models.CharField(choices = classifications, max_length=3, default = 'DF')
	allergen = models.ManyToManyField(Allergen,blank = True)

	def __str__(self):
		return self.name
