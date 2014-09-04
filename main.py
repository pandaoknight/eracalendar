#!/usr/bin/python
# -*- coding:utf-8 -*-
from datetime import datetime
from datetime import timedelta
from era import *


date = datetime.now()
print "";
print "";
print "  今天是新世纪年 %s年 第%s周 %s 是新年后的第%s天" % (year(date), week(date), day_name[weekday(date)], (date - firstday(year(date))).days);
print "             公元 %s年%s月%s日 %s" % (date.year, date.month, date.day, day_name[date.weekday()]);
print "        今天也请努力过好充实、认真的一天";
print "";
print "";
