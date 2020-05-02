import requests

resp = requests.get('https://api.covid19api.com/live/country/india/status/confirmed')
records = resp.json()

recent_update = records[len(records) - 1]
print(recent_update)
confirmed_count = recent_update['Confirmed']
death_count = recent_update['Deaths']
recovered_count = recent_update['Recovered']
active_count = recent_update['Active']

last_updated_time = recent_update['Date'][0:10]
print(str(confirmed_count) + " " + str(death_count) + " " + str(recovered_count) + " " + str(active_count))

file_data = ""
with open('public/index_helper.html', 'r') as file:
    file_data = file.read()

file_data = file_data \
    .replace('confirmed_case_count_ind', str(confirmed_count)) \
    .replace('active_case_count_ind', str(active_count)) \
    .replace('recovered_case_count_ind', str(recovered_count)) \
    .replace('death_case_count_ind', str(death_count)) \
    .replace('last_updated_time', str(last_updated_time))

with open('public/index.html', 'w') as file:
    file.write(file_data)
