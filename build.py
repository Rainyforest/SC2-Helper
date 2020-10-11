class Build:
    def __init__(self, build_info):
        self.time = build_info["time"]
        self.time_in_seconds = self.parse_time(build_info["time"])
        self.name = build_info["name"]
        self.supply = build_info["supply"]
        self.is_worker = build_info["is_worker"]
    
    def parse_time(self, str_time):
        [minutes,seconds] = str_time.split(":")
        # print(minutes+"\t==\t"+ seconds +"\t==\t"+ str(int(minutes)*60+int(seconds)))
        return int(minutes)*60+int(seconds)