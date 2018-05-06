#!/usr/bin/env python3

import registrar
import pickle
from pathlib import Path

instructors={}
students={}
courses={}

def main_menu():
	print('Select an option')
	nav_num=input('1: Create a course \n2: Schedule a course offering \n3: List course catalog \
		\n4: List course schedule \n5: Hire an instructor \n6: Assign an instructor to a course \
		\n7:Enroll a student \n8: Register a student for a course \n9: List enrolled students \
		\n10: List students registered for a course \n11: Submit student grade\n12: Get student records \
		\n13: Exit\n')
	if nav_num=='1':
		create_a_course()
	elif nav_num=='2':
		schedule()
	elif nav_num=='3':
		list_catalog()
	elif nav_num=='4':
		list_schedule()
	elif nav_num=='5':
		hire()
	elif nav_num=='6':
		assign()
	elif nav_num=='7':
		enroll()
	elif nav_num=='8':
		register_student()
	elif nav_num=='9':
		list_students()
	elif nav_num=='10':
		registered()
	elif nav_num=='11':
		grade()
	elif nav_num=='12':
		get_records()
	elif nav_num=='13':
		end()

def create_a_course():
	department=input('Enter the department the course will belong to:\n')
	name=input('Enter the course name:\n')
	number=input('Enter the course number:\n')
	credits=input('Enter how many credits the course will be worth:\n')
	c=registrar.Course(department,number,name,credits)
	theInstitute.courseCatalog.append(c)
	courses[number]=c
	main_menu()

def schedule():
	course_num=input('Enter the course number:\n')
	section_number=input('Enter a section number:\n')
	instructor=input('Enter an instructor\'s username:\n')
	year=input('Enter a year:\n')
	quarter=input('Enter a quarter (WINTER, FALL, SUMMER, SPRING):\n')
	o=registrar.CourseOffering(courses[course_num],section_number,instructors[instructor],year,quarter)
	theInstitute.courseOfferings.append(o)
	main_menu()

def list_catalog():
	for course in theInstitute.courseCatalog:
		print(course.name)
	main_menu()

def list_schedule():
	year=input('Enter year:\n')
	quarter=input('Enter quarter:\n')
	for course in theInstitute.courseOfferings:
		if year==course.year and quarter==course.quarter:
			print(course.course.name+': '+course.instructor.last_name+', '+course.instructor.first_name)
	main_menu()

def hire():
	print('Enter the following details for the instructor:')
	last_name=input('Last name:\n')
	first_name=input('First name:\n')
	date_of_birth=input('Date of birth:\n')
	username=input('Username:\n')
	i=registrar.Instructor(last_name,first_name,theInstitute,date_of_birth,username,'Instructor')
	theInstitute.insList.append(i)
	instructors[username]=i
	main_menu()

def assign():
	username=input('Enter instructor username:\n')
	department=input('Enter course department:\n')
	number=input('Enter course number:\n')
	section_number=input('Enter course section_number:\n')
	year=input('Enter year:\n')
	quarter=input('Enter quarter:\n')
	for course in theInstitute.courseOfferings:
		if department==course.course.department and number==course.course.number and section_number==course.section_number and year==course.year and quarter==course.quarter:
			course.instructor=instructors[username]
			#checks for the right course offering then replaces instructor
	main_menu()

def enroll():
	print('Enter the following details for the student:')
	last_name=input('Last name:\n')
	first_name=input('First name:\n')
	date_of_birth=input('Date of birth:\n')
	username=input('Username:\n')
	s=registrar.Student(last_name,first_name,theInstitute,date_of_birth,username,'Student')
	theInstitute.stuList.append(s)
	students[username]=s
	main_menu()

def register_student():
	username=input('Enter student username:\n')
	department=input('Enter course department:\n')
	number=input('Enter course number:\n')
	section_number=input('Enter course section_number:\n')
	year=input('Enter year:\n')
	quarter=input('Enter quarter:\n')
	for course in theInstitute.courseOfferings:
		if department==course.course.department and number==course.course.number and section_number==course.section_number and year==course.year and quarter==course.quarter:
			course.register_students(students[username])
			#checks for right course offering then inserts student
	main_menu()

def list_students():
	for student in theInstitute.stuList:
		print(student.username+': '+student.last_name+', '+student.first_name+'   '+student.date_of_birth+'   '+student.email)
	main_menu()

def registered():
	department=input('Enter course department:\n')
	number=input('Enter course number:\n')
	section_number=input('Enter course section_number:\n')
	year=input('Enter year:\n')
	quarter=input('Enter quarter:\n')
	for course in theInstitute.courseOfferings:
		if department==course.course.department and number==course.course.number and section_number==course.section_number and year==course.year and quarter==course.quarter:
			students=course.get_students()
			for student in students:
				print(student.last_name+','+student.first_name)
	main_menu()

def grade():
	department=input('Enter course department:\n')
	number=input('Enter course number:\n')
	section_number=input('Enter course section_number:\n')
	year=input('Enter year:\n')
	quarter=input('Enter quarter:\n')
	username=input('Enter student username:\n')
	grade=input('Enter letter grade:\n')
	for course in theInstitute.courseOfferings:
		if department==course.course.department and number==course.course.number and section_number==course.section_number and year==course.year and quarter==course.quarter:
			course.submit_grade(students[username],grade)
	main_menu()

def get_records():
	username=input('Enter student username:\n')
	s=students[username]
	print(s.last_name+', '+s.first_name)
	print('GPA: '+s.gpa())
	print('Credits earned: '+s.credits())
	print('Courses taken:')
	for course in s.list_courses():
		print(course.course.number+'-'+course.section_number+': '+course.quarter+' '+course.year)
		print(course.stuDict[s])
	main_menu()

def end():
	pickle.dump(instructors, ins_out)
	pickle.dump(students, stu_out)
	pickle.dump(courses, cou_out)
	pickle.dump(theInstitute, sch_out)	
	exit()

print('Welcome')
name=input('Enter institution name:\n')
theInstitute=registrar.Institution(name)
filecheck=Path(theInstitute.name+'.pickle')
#load previous info
if filecheck.is_file():
	ins_in=open(theInstitute.name+'Instructors.pickle','rb')
	stu_in=open(theInstitute.name+'Students.pickle','rb')
	cou_in=open(theInstitute.name+'Courses.pickle','rb')
	sch_in=open(theInstitute.name+'.pickle','rb')
	instructors=pickle.load(ins_in)
	students=pickle.load(stu_in)
	courses=pickle.load(cou_in)
	theInstitute=pickle.load(sch_in)
#save output of dictionaries and institute to load later
ins_out=open(theInstitute.name+'Instructors.pickle','wb')
stu_out=open(theInstitute.name+'Students.pickle','wb')
cou_out=open(theInstitute.name+'Courses.pickle','wb')
sch_out=open(theInstitute.name+'.pickle','wb')

main_menu()