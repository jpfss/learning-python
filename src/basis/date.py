# -*- coding: utf-8 -*-
import time;      # This is required to include time module.
import calendar;

ticks = time.time()
print ("Number of ticks since 12:00am, January 1, 1970:", ticks)
localtime = time.localtime(time.time())
print ("Local current time :", localtime);

# =============================================================================
# Getting formatted time
# =============================================================================
localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)
# =============================================================================
# Getting calendar for a month
# =============================================================================
cal = calendar.month(2016, 2)
print ("Here is the calendar:")
print (cal)