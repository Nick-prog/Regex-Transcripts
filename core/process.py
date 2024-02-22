import core
from pprint import pprint

class Process(object):
    '''
    Class in charge of processing the hash list given to it and converting it accordingly.
    '''

    def __init__(self, scale):
        self.scale = scale # GPA conversion selector

    def cal_avg(self, list):
        '''
        Calculates average grades from given tuple hash lists. Returns an avg_list, rounds all values.
        Return list.
        '''
        avg_list = [] # empty list

        for items in list: # hashed tuples in given list
            total = 0
            skip_flag = 0 # prevent unneccesary dividing when averaging
            for values in items: # hashed items in given tuples
                if values == 'IP' or values == "I": # In progress class, no value. Skip.
                    skip_flag = skip_flag + 1
                    pass
                elif values == 'P' or values == 'Pr': # Passed class, set to 85.
                    total = total + 85
                elif values == 'W': # Waived class, set to 0. Find out actual grade from HS.
                    skip_flag = skip_flag + 1
                    pass
                elif values == 'APr': # Passed class, set to 75.
                    total = total + 75
                else:
                    total = int(values) + total

                if len(items) == skip_flag: # only IP classes
                    avg = 0
                else:
                    avg = total/(len(items) - skip_flag)

            avg_list.append(round(avg, 0))

        return avg_list
    
    def cal_gpa(self, list):
        '''
        Automatically processes avg_list through the Class GPAT. Returns a gpa_list, containing values between 0-4.0.
        Return list.
        '''
        gpa_list = [] # empty list

        if self.scale == 4: # 4.0 scale
            for item in list:
                g = core.GPAT(int(item), self.scale) # returns a converted avg into gpa based on scale. Ex: 90 -> 3.5
                gpa_list.append(g.conv_value())

        return gpa_list
