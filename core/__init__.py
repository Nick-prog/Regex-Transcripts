from .reader import * # Class Reader created with methods for interacting/scraping information from transcript files (PDFs)
from .process import * # Class Process created with methods for converting extracted data list (hash_grades) into averaged values (avg_list) Automatically calls Class GPAT
from .grades import * # Class GPAT created with methods for converting extracted data list (avg_list) to associated GPAs (gpa_list)

from datetime import date

__title__ = "Regex Transcripts"
__author__ = 'Nickolas Rodriguez'
__date__ = f'{date.today()}'