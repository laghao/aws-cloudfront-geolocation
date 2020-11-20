import re,os,json
from configparser import ConfigParser
from ip2geotools.databases.noncommercial import DbIpCity

config = ConfigParser()
config.read('config.ini')

class ExctractClient:

    # TODO Replace CONFIG.ini with yaml
    folder=(config['DEFAULT']['FOLDER'])
    output=(config['DEFAULT']['OUTPUT'])
    IP_MATCHER = re.compile(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})")
    DATE_MATCHER = re.compile(r"([0-9]{4}\-[0-9]{2}\-[0-9]{2})")

    def __init__(self):
        self.lst = []

    def parser(self):
        folder = self.folder
        output = self.output
        lst = self.lst
        self._reader(folder,lst) 
        return self._writer(output,lst) 

    def _writer(self,output,lst):
        with open(output, 'w') as f:
            for item in lst:
                f.write("%s\n" % item)

    # TODO Add parallel requests
    def _reader(self,folder,lst):
        try:
            for filename in os.listdir(os.getcwd()+"/"+folder):
                try:
                    with open(os.path.join(os.getcwd(),folder,filename), 'r') as fh:
                        for line in fh:
                            if self.IP_MATCHER.findall(line): 
                                    lst.append([self.IP_MATCHER.search(line).group(1) ,
                                            self.DATE_MATCHER.search(line).group(1),
                                            DbIpCity.get((self.IP_MATCHER.search(line).group(1)), api_key = 'free').country,
                                            DbIpCity.get((self.IP_MATCHER.search(line).group(1)), api_key = 'free').city])
                                            # DbIpCity.get((self.IP_MATCHER.search(line).group(1)), api_key = 'free').region,
                                            # DbIpCity.get((self.IP_MATCHER.search(line).group(1)), api_key = 'free').longitude,
                                            # DbIpCity.get((self.IP_MATCHER.search(line).group(1)), api_key = 'free').latitude])
                except IOError:
                    print("File cannot be accessed")
        except IOError:
            print("No such folder directory") 
        try:
            lst[0]
        except IndexError:
            print("Couldn't find IP or Date. Please verify log files content.") 
        else:
            return lst