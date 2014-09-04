#!/usr/bin/python
# -*- coding:utf-8 -*-
from pprint import pprint
from datetime import datetime;
from datetime import timedelta;
from calendar import calendar;
from calendar import isleap as c_isleap;


__all__ = ['now', 'year'];


CUR_YEAR = datetime.now().year;
newyear = (9,3); # 新年是特殊的日期和闰年的2月29日的星期是星期日；
    # 在下面算法中，新年可以是3月1日到12月31日的任何一天，
    # 但如果是1月1日到2月28（29）日的一天，则isleap的算法需要修改。
    # 两个候选值：
    # 9月3日 能保证1月1日是周一
    # 9月6日 能保证闰年2月29日是接在周日后面的一天
leapday = (2,29);
holidays = {(9,3):"新年",(1,1):"元旦"};


def now():
    return 'now';

class eracalendar:
    pass;

class eradatetime:
    pass;

def firstday(year):
    return datetime(year, newyear[0], newyear[1]);

def lastday(year):
    return datetime(year + 1, newyear[0], newyear[1]) - timedelta(days=1);

def isleap(year):
    #return calendar.isleap(year + 1);
    return c_isleap(year + 1);

def year(date):
    assert isinstance(date, datetime);
    return date.year if date >= datetime(date.year, newyear[0], newyear[1]) else date.year - 1;

def week(date):
    assert isinstance(date, datetime); # Python程序员推荐"鸭子准则"，
        # 而不推荐"Any type check"，如Python没有const是一样的；
        # Pythoner认为程序员自己足够聪明知道函数需要什么样的对象，
        # 而type check只会降低程序的复用性以及运行时效率。
        # **但这里我还是先加上，防止不合适的调用。
    _year = year(date);
    _firstday = firstday(_year);
    if _firstday == date:
        return 0;
    i = (date - _firstday).days - 1; # 新年的第二天是周一，周数也记为1。所以一年的周数为0~52。
        # **这里用到了datetime的"-"运算符重载，要求输入项也提供这个功能未免过于苛刻。
    return i/7 + 1 if not isleap(_year) or date < datetime(_year+1, 2, 29) else (i-1)/7 + 1; #若2月29日因newyear(例如：9月6日)的改变恰好是周日，则周数归属上一周算周日。

def weekday(date):
    assert isinstance(date, datetime);
    month_day = date.month, date.day
    if newyear == month_day or (2, 29) == month_day:
        #return 7;
        return 6; # 新年和闰日是周日。
    _year = year(date);
    _firstday = firstday(_year);
    i = (date - _firstday).days - 1;
    return i%7 if not isleap(_year) or date < datetime(_year+1, 2, 29) else (i-1)%7; # 0=周一 ... 6=周日

def test():
    print week(datetime(2014, 9, 4));
    print year(datetime(2014, 9, 4));
    print year(datetime(2014, 9, 3));
    print year(datetime(2014, 9, 2));
    print firstday(2014);
    print lastday(2014);
    print isleap(2014);
    print isleap(2015);

def testWeek():
    def helpweek(date):
        return "%s %s" % (week(date), weekday(date))
    print "2014 9 4  week %s" % helpweek(datetime(2014, 9, 4));
    print "2014 9 3  week %s" % helpweek(datetime(2014, 9, 3));
    print "2014 9 2  week %s" % helpweek(datetime(2014, 9, 2));
    print "2015 12 31 week %s" % helpweek(datetime(2015, 12, 31));
    print "2016 1 1  week %s" % helpweek(datetime(2016, 1, 1));
    print "2016 1 2  week %s" % helpweek(datetime(2016, 1, 2));
    print "2016 1 3  week %s" % helpweek(datetime(2016, 1, 3));
    print "2016 2 25 week %s" % helpweek(datetime(2016, 2, 25));
    print "2016 2 26 week %s" % helpweek(datetime(2016, 2, 26));
    print "2016 2 27 week %s" % helpweek(datetime(2016, 2, 27));
    print "2016 2 28 week %s" % helpweek(datetime(2016, 2, 28));
    print "2016 2 29 week %s" % helpweek(datetime(2016, 2, 29));
    print "2016 3 1  week %s" % helpweek(datetime(2016, 3, 1));
    print "2016 3 2  week %s" % helpweek(datetime(2016, 3, 2));
    print "2016 3 3  week %s" % helpweek(datetime(2016, 3, 3));

def testAllDay():
    for i in range(0, 366 if isleap(CUR_YEAR + 1) else 365): # 如果有闰年其实是包含在下一个自然年里面。
        print datetime(CUR_YEAR, 9, 4) + timedelta(days=i);

if __name__ == '__main__':
    print '-*- __main__ : running test -*-';
    #test();
    testWeek();
    #testAllDay();
