from collections import OrderedDict

class first_sunday():
    
    def __init__(self):
        
        self.month_day = OrderedDict()
        month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        for month, day in zip(month_list, day_list):
            self.month_day[month] = day

    def __call__(self, start, end):
        
        cnt = 1
        first_sunday = 1 # Janunary, 1st
        first_day_of_month = first_sunday
        
        for year in range(start, end):
            if (year % 4 == 0  & year % 100 != 0) or (year % 400 == 0):
                self.month_day['Feb'] = 29        

            for month, day in self.month_day.items():

                if (year == start) & (month == 'Jan'):
                    continue

                first_day_of_month += day

                if first_day_of_month % 7 == 0: 
                    cnt += 1

            self.month_day['Feb'] = 28

        return cnt

def main():
    sunday_on_the_first_day_of_month = first_sunday()
    print(sunday_on_the_first_day_of_month(1901, 2001))

if __name__ == "__main__":
    main()
