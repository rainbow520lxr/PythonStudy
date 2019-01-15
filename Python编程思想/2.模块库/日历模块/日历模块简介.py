import calendar

''''''
'''
日历模块

'''
'''
使用

'''
#返回指定某年某月的日历
print(calendar.month(2017, 7))

#返回指定年的日历
print(calendar.calendar(2017))

#闰年返回True, 否则返回False
print(calendar.isleap(2000))

#返回某个月的weekday的第一天和这个月的最后一天
print(calendar.monthrange(2017,6))

#返回某个月以每一周为元素的列表
print(calendar.monthcalendar(2017, 7))