import win32api
from datetime import datetime, time


# время неактивности в секундах
inactive_time = 60

# время последней активности
last_activity = win32api.GetLastInputInfo()
glt = win32api.GetLocalTime()
lt = win32api.GetLocalTime()
datetime.


print(win32api.GetLocalTime())
# GetSystemDirectory
#     Returns the Windows system directory.



# while True:
#     # проверяем, прошло ли время неактивности
#     print(datetime(win32api.GetLocalTime()) - datetime(glt))
#     new_activity = win32api.GetLastInputInfo()
    # if last_activity + 10000 < new_activity:
    #     print('--10!!!')
    #     break


    # print(win32api.GetLastInputInfo())
    # if win32api.GetLastInputInfo() - last_activity > inactive_time * 100:
    #     print(111)

