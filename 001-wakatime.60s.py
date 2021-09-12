#!/usr/bin/python
# coding=utf-8

# <xbar.title>Wakatime</xbar.title>
# <xbar.version>v1.0</xbar.version>
# <xbar.author>Suwardhan</xbar.author>
# <xbar.author.github>Suwardhana</xbar.author.github>
# <xbar.desc>Displays today's productive time and other</xbar.desc>
# <xbar.image>https://i.imgur.com/zJsoTl8.jpg</xbar.image>
# <xbar.dependencies>python</xbar.dependencies>

import json
from urllib import urlopen


wakatime_icon='iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7MK6iAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAWJQAAFiUBSVIk8AAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAALVSURBVEiJrdfLi5ZVHAfwz7xjOlMLdaBwQhGTLrQxsE05s2udqQhCQSX1B4R5mVyE2CyCNl28tI9EUUM3bgRdlURRoCYYRHaZSzgZk6mJM9PinCfOe97neeZ9fecLD/Nyzu/7/f7O7XfO9GgPvdiAF7EeD2MQS/Ar/sDXOI0vMdOmbiX6sScKz7X5TWJX5N4Xtgqjadcw/37Blirx3pK2BkbxIZaW9F/EVzgrTO8Y7uGRLG5pTP4BnJtvlA0cKcn+OnZjTQ13DUYwVcL/PGpXYrSE9JHykVdhGQ6U6OyvImzFbBL4L17vwDDH9qhR6M1icx7UL2yGNMM3uzAt8Gqm+RseTAP2aJ3ehUI+7TuLjl7N5/S6ztY0R4+wzgWWad5wE9HTcJbR7i5M4QT+xgtJ20jmMdTASxnxWBemL0fDOaGsFjiaxW2E80kmFysEz+GC+jK4En8Kdfo7ref2cuJzFq4mDcdLBB/CDdzC4QrThlDFZqL56pKYk4nPpQZWJJ0TJYR/8FkkbMNQYlbgbTwprO0OXCvRGUt+D9K84z6pGNES/BRjfsdTMclvsA5/4S7OVPBF7cJnGi4lDSdriM9EgzvCLNyLI7wpVKVJDNTwv0h8rjSEM1zgiRri9/g4GvbjNvqESjSNV4T1rUKqPQYfaD5jdTfQImF3zuAHYZlu4dMaDqzNPN6ntYCMzCPyKPbFv8N4C4vn4ezNPJ4nlK/JpHFKc8nrFsuFJSj0xyUnYleW0cEFND6Uae9IO/uEs7fQ1+JrmebPwtFswhatD4HtXZi+ofUhkN8L/+O9LMM54T7tZM0HhNKa6+yrI1U99qaE3f5YDXetsHvTjZQ+9nrS4J6cHdv2452K/sv4UXjGwCo8jqdLYueEWXw3/m4Lm7VuuE6+a9jUrlmOPuGNNNGB4bhwW/XVCZdNZRkaeE54OTwrXGsrhRtpXChA3+KU8F/G7HyC/wEyZS3znAni/QAAAABJRU5ErkJggg=='

######## edit here
api_key = "######"
username = "#####"
######## end of edit here

url='https://wakatime.com/api/v1/users/{}/summaries?range=today&api_key={}'.format(username, api_key)
url_y='https://wakatime.com/api/v1/users/{}/stats/last_7_days?api_key={}'.format(username, api_key)
url_l='https://wakatime.com/api/v1/users/{}/leaderboards/86675656-28dd-4a1b-a2d2-572134f14fa9?api_key={}'.format(username, api_key)

payload=urlopen(url)
data = json.load(payload)
payload_y=urlopen(url_y)
data_y = json.load(payload_y)
payload_l=urlopen(url_l)
data_l = json.load(payload_l)

duration = 1
duration_today=data['cummulative_total']['digital']
duration_in_second=data['cummulative_total']['seconds']
second_daily_average=data_y['data']['daily_average_including_other_language']
l_name = [data_l['data'][0]['user']['display_name'],data_l['data'][1]['user']['display_name'],data_l['data'][2]['user']['display_name']]
l_average = [data_l['data'][0]['running_total']['human_readable_daily_average'],data_l['data'][1]['running_total']['human_readable_daily_average'],data_l['data'][2]['running_total']['human_readable_daily_average']]
l_desc = data_l['range']['text']

percentage = int(100 * (float(duration_in_second)-float(second_daily_average))/float(second_daily_average))
if percentage > 0 :
  percentage = '+'+str(percentage)
percentage = str(percentage)+'%'
#    print('{} - {} : {} | templateImage={}'.format(coin_symbol, last_price, price_variation, bitcoin_icon))
print('{} ({}) | templateImage={}'.format(duration_today, percentage, wakatime_icon))
print('---')
print('Total productive compared to daily average')
print('Daily Coding Average | color=#808080')
print('{} - {} | color=#808080').format(l_name[0],l_average[0])
print('{} - {} | color=#808080').format(l_name[1],l_average[1])
print('{} - {} | color=#808080').format(l_name[2],l_average[2])
print(l_desc)
# print('{} : {}'.format(duration_today, percentage))
# print('asdf')
