#!/usr/bin/env python

from time import strftime, localtime
import urllib2
import json
f = urllib2.urlopen('http://api.wunderground.com/api/eaff9c7196a8cdc9/conditions/q/CO/80836.json')
json_string = f.read()
parsed_json = json.loads(json_string)
#location = parsed_json['location']['city']
local_time_rfc822 = parsed_json['current_observation']['local_time_rfc822']
temp_f = parsed_json['current_observation']['temp_f']
feelslike_f = parsed_json['current_observation']['feelslike_f']
wind_degrees = parsed_json['current_observation']['wind_degrees']
wind_mph = parsed_json['current_observation']['wind_mph']
wind_gust_mph = parsed_json['current_observation']['wind_gust_mph']
relative_humidity = parsed_json['current_observation']['relative_humidity']
pressure_in = parsed_json['current_observation']['pressure_in']
pressure_trend = parsed_json['current_observation']['pressure_trend']
datetime = strftime("%d, %b, %Y, %H:%M", localtime())
t=open('/home/test/weather/strattondata.csv', 'a')
t.write("%s,%s,%s,%s,%s,%s,%s,%s,%s" % (datetime, temp_f, feelslike_f, relative_humidity, wind_degrees, wind_mph, wind_gust_mph, pressure_in, pressure_trend))
t.write("\n")
t.close()
f.close()

f = urllib2.urlopen('http://api.wunderground.com/api/eaff9c7196a8cdc9/conditions/q/TX/77301.json')
json_string = f.read()
parsed_json = json.loads(json_string)
#location = parsed_json['location']['city']
local_time_rfc822 = parsed_json['current_observation']['local_time_rfc822']
temp_f = parsed_json['current_observation']['temp_f']
feelslike_f = parsed_json['current_observation']['feelslike_f']
wind_degrees = parsed_json['current_observation']['wind_degrees']
wind_mph = parsed_json['current_observation']['wind_mph']
wind_gust_mph = parsed_json['current_observation']['wind_gust_mph']
relative_humidity = parsed_json['current_observation']['relative_humidity']
pressure_in = parsed_json['current_observation']['pressure_in']
pressure_trend = parsed_json['current_observation']['pressure_trend']
datetime = strftime("%d, %b, %Y, %H:%M", localtime())
t=open('/home/test/weather/conroedata.csv', 'a')
t.write("%s,%s,%s,%s,%s,%s,%s,%s,%s" % (datetime, temp_f, feelslike_f, relative_humidity, wind_degrees, wind_mph, wind_gust_mph, pressure_in, pressure_trend))
t.write("\n")
t.close()
f.close()
