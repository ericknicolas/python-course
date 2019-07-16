import time
from datetime import datetime as dt

hosts_path = "./hosts"
redirect = "127.0.0.1"

site_black_list = ["marca.com", "wwww.marca.com", "as.com", "wwww.as.com"]

start_working_time = dt(dt.now().year, dt.now().month, dt.now().day, 9)
end_working_time = dt(dt.now().year, dt.now().month, dt.now().day, 10)

while True:
    if (start_working_time < dt.now() < end_working_time):
        print("It's working time...")

        with open(hosts_path, "+r") as f:
            content = f.read()
            
            for site in site_black_list:
                if site in content:
                    pass
                else:
                    f.write(redirect + " " + site + "\n")

    else:
        print("F u N t I m E")

        with open(hosts_path, "+r") as f:
            lines = f.readlines()

            for site in site_black_list:
                for i, line in enumerate(lines):
                    if site in line:
                        del lines[i]
            
            f.seek(0)
            f.writelines(lines)
            f.truncate() #truncate remainig lines

    time.sleep(5)
