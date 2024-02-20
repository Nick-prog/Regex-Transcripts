import core

class GPAT():
    '''
    Class in charge of converting given values from avg_list into assoicated GPA values based on scale selected.
    '''

    def __init__(self, value, type):
        self.value = value # passed value for converting

        if type == 4: # 4-point scale
            self.list = self.four_point_list() # generated scale list, used to find the index of the avg value (self.value) given
        elif type == 5: # 5-point scale
            self.list = self.five_point_list() # generated scale list, used to find the index of the avg value (self.value) given

    def four_point_list(self):
        '''
        Creates a list of 100 indicies for four-point-scale starts at 0-59 -> 0 and ends at 95-100 -> 4.0. 
        Returns list.
        '''
        conv_list = [] # empty list
        point = 0 # current value

        for x in range(100): # list of 100 entries
            if x <= 59: # 0-59 -> 0
                conv_list.append(0)
            elif x == 60: # 60, start count at 0.5
                point = 0.5
                conv_list.append(point)
            elif x >= 95: # 95-100 -> 4.0
                conv_list.append(4.0)
            else: # increment by 0.1 per index
                point = point + 0.1
                conv_list.append(round(point, 1))

        return conv_list
    
    def five_point_list(self):
        '''
        Creates a list of 100 indicies for five-point-scale starts at 0-59 -> 0 and ends at 95-100 -> 4.0, incrementing .15 per avg. 
        Returns list.
        '''
        conv_list = []
        point = 0

        for x in range(100):
            if x <= 59: # 0-59 -> 0
                conv_list.append(0)
            elif x == 60: # 60, start count at 0.15
                point = 0.15
                conv_list.append(point)
            elif x >= 95: # 95-100 -> 4.0
                conv_list.append(4.0)
            else: # increment by 0.15 per index
                point = point + 0.15
                conv_list.append(round(point, 2))

        return conv_list
    
    def conv_value(self):
        '''
        Uses generated list to return a single value based on index selected (self.value).
        Returns int.
        '''
        if self.value == 100: # out of bounds, set to final index value
            return self.list[99]
        else:
            return self.list[self.value]


if __name__ == '__main__':
    grade = GPAT(59, 4)
    print(grade.conv_value())