import re
from pprint import pprint
from PyPDF2 import PdfReader

class Reader():
    '''
    Class in charge of scarping data from the given PDF based on the pattern given in get_courses and get_grades. Increments through all pages
    and returns lists associated with the given student's grades and courses.
    '''

    def __init__(self, file):
        self.file = file # input file picked through dialog box.
        self.courses_list = [] # empty list that holds the general list of courses found.
        self.grades_list = [] # empty list that holds the general list of grades found.
        self.reader = PdfReader(file) # PyPDF2 object from PdfReader method that allows manipulating of the PDF data.

    def get_courses(self, text):
        '''
        Regex pattern finder for all known courses possible.
        Return list.
        '''
        return re.findall(r'\b(?:\d{8}|\d{5,6}[A-Z]{2,3}\d{0,1}|[A-Z]{1,3}\d{3,7})\s.{10}|(?:1111|1112)\s{5}\/.{10}', text)
    
    def get_grades(self,text):
        '''
        Regex pattern finder for all known grades possible.
        Return list.
        '''
        return re.findall(r'(?:0\.0 0\.0|0\.5 0\.5|1\.0 1\.0|1\.5 1\.5|2\.0 2\.0).*?(\d{1,3}|P)|\s(IP)\s', text)

    def read_page(self, select):
        '''
        Single page captured and data collection stored in self.course_list and self.grades_list. 
        No Returns.
        '''
        page = self.reader.pages[select]

        text = page.extract_text()

        courses = self.get_courses(text)
        grades = self.get_grades(text)

        for items in courses:
            if items.startswith("Semester") or len(items) >= 30:
                pass
            else:
                self.courses_list.append(items)

        for items in grades:
            self.grades_list.append(items)

    def read_all(self):
        '''
        All pages captured and data collection stored in self.course_list and self.grades_list. 
        No Returns.
        '''
        counter = 0

        for page in self.reader.pages:
            counter = counter + 1
            if counter == 0:
                pass
            else:
                text = page.extract_text()

                courses = self.get_courses(text)
                full = self.get_grades(text)
                grades = [tuple for items in full for tuple in items if tuple != ""]

                for items in courses:
                    if items.startswith("Semester") or len(items) >= 30:
                        pass
                    else:
                        self.courses_list.append(items)

                for items in grades:
                    self.grades_list.append(items)
                
    def get_unique_list(self, list):
        '''
        Hashed list of unique courses found in self.courses_list.
        Return hash list.
        '''
        unique = []

        for items in list:
            if items not in unique:
                unique.append(items)

        return unique

    def get_hash_list(self, unique, list):
        '''
        Hashed list of tupled indexed grades from self.grades_list for each unique course found in self.courses_list.
        Return nested list.
        '''
        hash_list = []

        for idx in range(len(unique)):
            hash_list.append([i for i, x in enumerate(list) if x == unique[idx]])
            
        return hash_list
    
    def get_hashed_grade_list(self, unique, list):
        '''
        Hashed list of tupled grades from self.grades_list for each unique course found in self.courses_list.
        Return nested list.
        '''
        hash_grade = []

        for idx in range(len(unique)):
            hash_grade.append([str(self.grades_list[i]).strip() for i, x in enumerate(list) if x == unique[idx]])

        return hash_grade