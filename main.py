import core
import ctypes
import sys
import pymsgbox
import os
import tkinter as tk
import pandas as pd
import numpy as np
from tkinter.filedialog import askopenfilename
from pathlib import Path
from pprint import pprint

def run(file, download):

    reader = core.Reader(file)
    reader.read_all()

    # pprint(reader.courses_list)
    # pprint(reader.grades_list)
    # print(len(reader.courses_list), len(reader.grades_list))

    if len(reader.courses_list) != len(reader.grades_list):
        print(len(reader.courses_list), len(reader.grades_list))
        raise ValueError('Regex value error, cannot find all corresponding courses and grades.')

    unique_list = reader.get_unique_list(reader.courses_list)

    hash_grade = reader.get_hashed_grade_list(unique_list, reader.courses_list)

    p = core.Process(4)
    avg_list = p.cal_avg(hash_grade)

    gpa_list = p.cal_gpa(avg_list)

    np.warnings.filterwarnings('ignore', category=np.VisibleDeprecationWarning)
    compiled_array = np.column_stack((unique_list, hash_grade, avg_list, gpa_list))

    df = pd.DataFrame(compiled_array)
    filepath = f'{download}/{fileName[:-4]}.xlsx'
    df.to_excel(filepath, index=False, header= ["Course Name", "Grades", "Average", "GPA"])

    return filepath


if __name__ == "__main__":

    try:
        tk.Tk().withdraw()
        file = askopenfilename()
        fileBase, fileName = os.path.split(file)
        downloadpath = str(os.path.join(Path.home(), "Downloads"))
        filepath = run(file, downloadpath)
        pymsgbox.alert(f"{fileName[:-4]}'s pdf located at {file} has been processed. Find the outputted excel sheet at {filepath}", "Complete!")

    except ValueError:
        ctypes.windll.user32.MessageBoxW(0, "ValueError encountered.", (sys.exc_info()[1]), "Warning!", 16)