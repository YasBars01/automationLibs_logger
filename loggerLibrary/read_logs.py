from datetime import date, datetime, timedelta
from . import log_config
from os.path import exists, join


class ReadLogs:

    def help(self):
        return ("""
        Function that returns data from log files
        :param date: accepts date value (yyyy-mm-dd) and looks for log file with that date
        :param *args: accepts lists of important words separated by comma, function will find line items with to those words in it
        """)

    def read_log(self, date, keep_phrases=None):
        """Function that returns data from log files
        :param date: accepts date value (yyyy-mm-dd) and looks for log file with that date
        :param *args: accepts lists of important words separated by comma, function will find line items with to those words in it
        """
        try:
            month = datetime.strptime(date[5:7], "%m")
            path_exists = exists(join(log_config.BASE_DIR, 'logs/', date[:-6], month.strftime('%B')))
            print(join(log_config.BASE_DIR, 'logs/', date[:-6], date[5:7]))
            print(path_exists)
            important = []
            if path_exists:
                file = join(log_config.CURRENT_LOG_DIR, log_config.APP_NAME + '_log_' + date + '.log')
                print('keep phrases: ', keep_phrases)
                with open(file) as f:
                    f = f.readlines()

                for line in f:
                    if keep_phrases:
                        for phrase in keep_phrases:
                            if phrase in line:
                                important.append(line)
                                break
                    else:
                        important.append(line)

            print(' '.join([str(elem) for elem in important]))
            return important

        except Exception as e:
            log_config.logger.error(e)

    def filter_range(self, start, end, time=None, keep_phrases=None):
        """
            yung search pwede syang maglagay ng date range, 
            time range, para mafilter nya as a support yung kelangan nya lang kunin, 
            baka mamaya kasi sobrang dami and irelevant na sa kelangan nyan date or time
        """

        # for time filter, we need to parse line, split on ':', get last index then split again for " " then look for first 2 digits
        important = []

        try:
            for single_date in self.daterange(start, end):
                print(single_date.strftime("%Y-%m-%d"))
                # path_exists = exists(join(log_config.BASE_DIR, 'logs/', date[:-3], date[:-3]))
                CURRENT_LOG_DIR = join(log_config.BASE_DIR, 'logs', single_date.strftime('%Y'),
                                       single_date.strftime('%B'))
                file = join(CURRENT_LOG_DIR, log_config.APP_NAME + '_log_' + single_date.strftime("%Y-%m-%d") + '.log')

                print('curr file is: ', file)
                with open(file) as f:
                    f = f.readlines()

                for line in f:
                    if time and self.get_time(time, line):
                        important.append(line)

                    if keep_phrases:
                        for phrase in keep_phrases:
                            if phrase in line:
                                important.append(line)
                                break
                    # else:
                    # important.append(line)

            print(' '.join([str(elem) for elem in important]))
            return important

        except Exception as e:
            print(e)

        return important

    @staticmethod
    def daterange(start_date, end_date):
        format = '%Y-%m-%d'
        start_date, end_date = datetime.strptime(start_date, format), datetime.strptime(end_date, format)
        for n in range(int((end_date - start_date).days) + 1):
            yield start_date + timedelta(n)

    @staticmethod
    def get_time(time, line):
        datetime = line.split(': ')
        time_in_line = datetime[len(datetime) - 2]

        if time in time_in_line.split(':')[0]:
            return True

        return False
