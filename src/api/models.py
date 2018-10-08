from django.db import models
from django.core.validators import *

class JobDetail(models.Model):
	JOBTYPE=(('FULL-TIME EMPLOYMENT','Full-time employment'),('SHORT-TERM CONTRACT','Short-term contract'),('INTERNSHIP','Internship'),('FREELANCE OR CONSULTING','Freelance or consulting'),('VOLUNTEER CONTRIBUTOR','Volunteer contributor'),('PARTNER FOR A VENTURE','Partner for a venture'))
	JOBCATEGORY = (('PROGRAMMING','Programming'),('GRAPHIC DESIGN','Graphic Design'),('ELECTORINCS','Electornics'),('TESTING','Testing'))
	JOBLOCATION = (('ANYWHERE','Anywhere'),('BANGLORE','Banglore, IN'),('CHENNAI','Channai, IN'),('MUMBAI','Mumbai, IN'),('PUNE','Pune, IN'))
	job_title 			= models.CharField(max_length = 100)
	job_type  			= models.CharField(max_length=50,choices= JOBTYPE, blank=True,null=False)
	job_category		= models.CharField(max_length=50,choices=JOBCATEGORY, null=False ,blank=True)
	job_location 		= models.CharField(max_length=50,choices=JOBLOCATION, null=True, blank=True)
	job_description 	= models.TextField(null=False,blank=True)
	salary				= models.PositiveIntegerField(validators=[MaxValueValidator(9999999999,message='Enter correct salary')])
	skill_requirements 	= models.TextField(null=True, blank=True)
	job_preks 			= models.TextField(null=True,blank=True)
	company_name 		= models.CharField(max_length=80)
	date_of_post 		= models.DateField(auto_now_add=True,null=False)
	Employee_Detail 	= models.TextField(null=False,blank=False)

	def __str__(self):
		return self.job_title

class User(models.Model):
	GENDER 					= (('MALE','Male'),('FEMALE','Female'),('OTHER','Other'))
	first_name 				= models.CharField(max_length=50)
	last_name 				= models.CharField(max_length=50)
	dob						= models.DateField(null=False,blank=True)
	gender					= models.CharField(max_length=50, choices=GENDER,null=False,blank=True)
	contact_number 			= models.PositiveIntegerField(null=False,validators=[MaxValueValidator(999999999999,message='Please enter correct Mobile number')])
	email_id				= models.EmailField()
	address					= models.TextField(null=False,max_length=500,blank=True)
	experience				= models.CharField(max_length=30, default='Fresher')
	resume_url				= models.URLField(null=False)
	proffession 			= models.CharField(null=False,max_length=100)
	current_or_pervious_company_name = models.CharField(max_length=50,null=True)

	def __str__(self):
		return self.first_name


class JobApplications(models.Model):
	job_id 					= models.ForeignKey(JobDetail,on_delete= 'CASCADE'),
	user_id 				= models.ForeignKey(User,on_delete= 'CASCADE'),
	expected_salary 		= models.PositiveIntegerField(validators=[MaxValueValidator(9999999999,message='Please Check you Enter Correct Salary or not')])
	job_related_experince 	= models.TextField(null=True,blank=True)

	def __str__(self):
		return self.user_id