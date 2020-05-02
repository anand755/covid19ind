import requests

resp = requests.get('https://api.covid19india.org/data.json')
records = resp.json()

cases_time_series_data = records['cases_time_series']

recent_update = cases_time_series_data[len(cases_time_series_data) - 1]

print(recent_update)
confirmed_count = recent_update['totalconfirmed']
death_count = recent_update['totaldeceased']
recovered_count = recent_update['totalrecovered']
active_count = int(confirmed_count) - (int(death_count) + int(recovered_count))

last_updated_time = recent_update['date'] + "2020"
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
