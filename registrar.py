#!/usr/bin/env python3

class Course:
	def __init__(self, department, number, name, credits):
		self.department=department
		self.number=number
		self.name=name
		self.credits=credits

class CourseOffering:
	def __init__(self, course, section_number, instructor, year, quarter):
		self.course=course
		self.section_number=section_number
		self.instructor=instructor
		instructor.courseList.append(self)
		self.year=year
		self.quarter=quarter
		self.stuDict={} #keys are students, values are grades
		self.userDict={} #keys are students, values are usernames
		self.forSort=self.for_sort() #number for sorting by quarter within years

	def register_students(self, *students):
		for student in students:
			self.stuDict[student]='N' #N represents no grade
			self.userDict[student.username]=student
			student.courseList.append(self)

	def get_students(self):
		return list(self.stuDict.keys())

	def submit_grade(self, student, grade):
		if isinstance(student, Student):
			self.stuDict[student]=grade
		else: #username supplied, not instance of student
			for username in self.userDict:
				if username==student:
					instance=self.userDict[username]
					self.stuDict[instance]=grade

	def get_grade(self,student):
		if isinstance(student, Student):
			return self.stuDict[student]
		else: #username supplied
			for username in self.userDict:
				if username==student:
					instance=self.userDict[username]
					return self.stuDict[instance]

	def for_sort(self):
		qnum=0
		if self.quarter=='WINTER':
			qnum=1
		elif self.quarter=='SPRING':
			qnum=2
		elif self.quarter=='SUMMER':
			qnum=3
		elif self.quarter=='FALL':
			qnum=4
		return int(self.year)*10+qnum #returns a number we can use to sort by quarter within years

class Institution:
	def __init__(self,name):
		self.name=name
		self.stuList=[]
		self.insList=[]
		self.courseCatalog=[]
		self.courseOfferings=[]

	def list_students(self):
		return self.stuList

	def enroll_student(self, student):
		self.stuList.append(student)

	def list_instructors(self):
		return self.insList

	def hire_instructor(self, instructor):
		self.insList.append(instructor)

	def list_course_catalog(self):
		return self.courseCatalog

	def list_course_schedule(self, year, quarter, department_name='All'):
		schedule=[]
		for course in self.courseOfferings:
			if department_name=='All':
				if year==course.year and quarter==course.quarter:
					schedule.append(course)
			else: #department_name specified
				if year==course.year and quarter==course.quarter and department_name==course.course.department:
					schedule.append(course)
		return schedule

	def add_course(self, course):
		self.courseCatalog.append(course)

	def add_course_offering(self, course_offering):
		#instances of the class CourseOffering hold all the information we need
		self.courseOfferings.append(course_offering)

class Person:
	def __init__(self, last_name, first_name, school, date_of_birth, username, affiliation):
		self.last_name=last_name
		self.first_name=first_name
		self.school=school
		self.date_of_birth=date_of_birth
		self.username=username
		self.affiliation=affiliation
		self.email=str(self.username)+'@'+str(self.school.name)+'.edu'
		self.courseList=[] #list of course offerings

class Instructor(Person):
	def list_courses(self, year=None, quarter=None):
		result=[]
		if year is None and quarter is None:
			result=self.courseList
		elif year is not None and quarter is None:
			for course in self.courseList:
				if year==course.year:
					result.append(course)
		elif year is None and quarter is not None:
			for course in self.courseList:
				if quarter==course.quarter:
					result.append(course)
		else: #both year and quarter supplied
			for course in self.courseList:
				if year==course.year and quarter==course.quarter:
					result.append(course)
		#sort the list by the number we calculate in CourseOffering that sorts by quarter within years
		result.sort(key=lambda x: x.forSort,reverse=True)
		return result

class Student(Person):
	def list_courses(self):
		result=[]
		result=self.courseList
		result.sort(key=lambda x: x.forSort,reverse=True)
		return result

	def credits(self):
		creditsum=0
		for course in self.courseList:
			creditsum+=int(course.course.credits)
		return creditsum

	def gpa(self):
		gpasum=0
		for course in self.courseList:
			gpasum+=self.convert_grade(course.stuDict[self])*int(course.course.credits)
		return gpasum/self.credits()

	def convert_grade(self, grade):
		if grade=='N':
			return 0.0
		elif grade=='A+' or grade=='A':
			return 4.0
		elif grade=='A-':
			return 3.7
		elif grade=='B+':
			return 3.3
		elif grade=='B':
			return 3.0
		elif grade=='B-':
			return 2.7
		elif grade=='C+':
			return 2.3
		elif grade=='C':
			return 2.0
		elif grade=='C-':
			return 1.7
		elif grade=='D+':
			return 1.3
		elif grade=='D':
			return 1.0
		elif grade=='D-':
			return 0.7
		elif grade=='F+':
			return 0.3
		elif grade=='F':
			return 0