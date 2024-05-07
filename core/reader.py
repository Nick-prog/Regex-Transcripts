import re
from PyPDF2 import PdfReader

class Reader():

    def __init__(self, file: str):
        """Class in charge of scarping data from the given PDF based on the pattern given in get_courses and get_grades. Increments through all pages
        and returns lists associated with the given student's grades and courses

        :param file: input file picked through dialog box
        :type file: str
        """

        self.file = file
        self.courses_list = [] # empty list that holds the general list of courses found.
        self.grades_list = [] # empty list that holds the general list of grades found.
        self.reader = PdfReader(file) # PyPDF2 object from PdfReader method that allows manipulating of the PDF data.

    def get_courses(self, _str: str) -> str:
        """Regex pattern finder for all known courses possible

        :param _str: input string
        :type _str: str
        :return: filtered string
        :rtype: str
        """

        return re.findall(r'\b(?:\d{8}|\d{5,6}[A-Z]{2,3}\d{0,1}|[A-Z]{1,3}\d{3,7})\s.{10}|(?:1111|1112)\s{5}\/.{10}', _str)
    
    def get_grades(self, _str: str) -> str:
        """Regex pattern finder for all known grades possible

        :param _str: input string
        :type _str: str
        :return: filtered string
        :rtype: str
        """

        return re.findall(r'(?:0\.0 0\.0|0\.5 0\.5|1\.0 1\.0|1\.5 1\.5|2\.0 2\.0).*?(\d{1,3}|I|P|APr|Pr|W)|\s(IP)\s', _str)

    def read_page(self, select: int) -> None:
        """Single page captured and data collection stored in self.course_list and self.grades_list

        :param select: page selector index
        :type select: int
        """

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

    def read_all(self) -> None:
        """All pages captured and data collection stored in self.course_list and self.grades_list
        """

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
                
    def get_unique_list(self, _list: list) -> list:
        """Creates a hashed list of unique courses found in self.courses_list

        :param _list: list of values found (courses)
        :type _list: list
        :return: unique list
        :rtype: list
        """

        unique = []

        for items in _list:
            if items not in unique:
                unique.append(items)

        return unique

    def get_hash_list(self, unique: list, _list: list) -> list:
        """Creates a hashed list of tupled indexed grades from self.grades_list 
        for each unique course found in self.courses_list

        :param unique: list of unique values (coruses)
        :type unique: list
        :param _list: list of values (grades)
        :type _list: list
        :return: hashed list of grades to unique courses
        :rtype: list
        """

        hash_list = []

        for idx in range(len(unique)):
            hash_list.append([i for i, x in enumerate(_list) if x == unique[idx]])
            
        return hash_list
    
    def get_hashed_grade_list(self, unique: list, _list: list) -> list:
        """Creates hashed list of tupled grades from self.grades_list for each unique course 
        found in self.courses_list

        :param unique: list of unique values (courses)
        :type unique: list
        :param _list: list of values (grades)
        :type _list: list
        :return: hashed list of grades to unique courses
        :rtype: list
        """
        hash_grade = []

        for idx in range(len(unique)):
            hash_grade.append([str(self.grades_list[i]).strip() for i, x in enumerate(_list) if x == unique[idx]])

        return hash_grade