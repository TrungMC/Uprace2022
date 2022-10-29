# This is a sample Python script.
import json

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests
import csv

def downloadTeamData(datestring):
    import requests

    headers = {
        'authority': 'api.uprace.vn',
        'accept': 'application/json',
        'accept-language': 'vi',
        'app-client-os': 'Web',
        'app-client-version': '977',
        'authorization': 'Bearer null',
        'content-type': 'application/json; charset=UTF-8',
        'origin': 'https://event.uprace.org',
        'referer': 'https://event.uprace.org/',
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    }

    json_data = {
        'trid': 'f3396668-e253-4bf1-947c-c572b1f12d6c',
        'trtm': 1667009897,
        'data': {
            'evid': '6',
            'type': 0,
            'value': 2,
            'from': 0,
        },
    }

    response = requests.post('https://api.uprace.vn/api/event/rank/list', headers=headers, json=json_data)
    data_file = open('data/teams/summary.csv','w',encoding='utf-8-sig',newline='')
    csv_writer=csv.writer(data_file)
    data=response.json()['data']['list']
    header="id,name,ava,act,dis,ddis"
    for team in data:
        csv_writer.writerow([team['id'],team['name'],team['ava'],team['act'],team['dis'],team['ddis']])
    data_file.close()
    return data


def downloadRunnerData(team_id, datestring):


    headers = {
        'authority': 'api.uprace.vn',
        'accept': 'application/json',
        'accept-language': 'vi',
        'app-client-os': 'Web',
        'app-client-version': '977',
        'authorization': 'Bearer null',
        'content-type': 'application/json; charset=UTF-8',
        'origin': 'https://event.uprace.org',
        'referer': 'https://event.uprace.org/',
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    }

    json_data = {
        'trid': '26090ab7-15be-4731-b7f3-926ad0d1c4eb',
        'trtm': 1667006965,
        'data': {
            'size': 200,
            'uid': None,
            'evid': '6',
            'type': 1,
            'sex': 0,
            'value': team_id,
            'from': 0,
            'day': '20221028',
        },
    }

    response = requests.post('https://api.uprace.vn/api/event/rank/list', headers=headers, json=json_data)
    data_file = open(f'data/runners/{datestring}.csv', 'a', encoding='utf-8-sig', newline='')
    csv_writer = csv.writer(data_file)
    data = response.json()['data']['list']
    fields=['id','code','name','sex','act','dis','ddis','ava']
    #csv_writer.writerow(fields)
    for r in data:
        csv_writer.writerow([r['id'],r['code'],r['name'],r['sex'],r['act'],r['dis'],r['ddis'],team_id])
    data_file.close()
    return data


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    datestring="20221028"
    team=downloadTeamData(datestring)

    #Clear the file and write header
    with open(f'data/runners/{datestring}.csv', 'w', encoding='utf-8-sig', newline='') as runner_file:
        csv_writer=csv.writer(runner_file)
        csv_writer.writerow(['id','code','name','sex','act','dis','ddis','team_id'])
    #Fetch data for 1st 16 teams
    for i in range(0,16):
        print(f'Download runner data for team {team[i]["name"]}')
        runner=downloadRunnerData(team[i]['id'],datestring)
        print(f'Finished runner data with {len(runner)} runners')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
