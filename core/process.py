import core

class Process(object):

    def __init__(self, scale: int):
        """Class in charge of processing the hash list given to it and converting it accordingly.

        :param scale: GPA conversion selector
        :type scale: int
        """
        
        self.scale = scale

    def cal_avg(self, _list: list) -> list:
        """Calculates average grades from given tuple hash lists.

        :param _list: hashed list of values (grades)
        :type _list: list
        :return: list of values averaged and rounded down
        :rtype: list
        """

        avg_list = [] # empty list

        for items in _list: # hashed tuples in given list
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
    
    def cal_gpa(self, _list: list) -> list:
        """Automatically processes avg_list through the Class GPAT.

        :param list: hashed list of values (averaged grades)
        :type list: list
        :return: list of values converted via GPA scale
        :rtype: list
        """

        gpa_list = [] # empty list

        if self.scale == 4: # 4.0 scale
            for item in _list:
                g = core.GPAT(int(item), self.scale) # returns a converted avg into gpa based on scale. Ex: 90 -> 3.5
                gpa_list.append(g.conv_value())

        return gpa_list
