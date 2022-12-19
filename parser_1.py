import requests
from bs4 import BeautifulSoup

def load_shedule_data(session, group):
    url = ''
    if group == 1:
        url = 'https://lks.bmstu.ru/schedule/a98e624a-81ca-11eb-9739-005056960017'
    elif group == 2:
        url = 'https://lks.bmstu.ru/schedule/a990b73e-81ca-11eb-bb1b-005056960017'
    elif group == 3:
        url = 'https://lks.bmstu.ru/schedule/a98e3af4-81ca-11eb-9f8f-005056960017'
    elif group == 4:
        url = 'https://lks.bmstu.ru/schedule/a98ddaaa-81ca-11eb-a4e2-005056960017'
    else:
        url = 'https://lks.bmstu.ru/schedule/a9a1cbe6-81ca-11eb-b2e0-005056960017'
    request = session.get(url)
    return request.text

def read_file(filename):
    with open(filename) as input_file:
        text = input_file.read()
    return text


def parse_user_datafile_bs(filename, group):
    s = requests.Session() 
    s.headers.update({
        'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0'
    })
    data = load_shedule_data(s, group)

    with open('./page.html', 'w', encoding='utf-8') as output_file:
        output_file.write(data)

    days = []
    text = read_file(filename)
    soup = BeautifulSoup(text)
    days_list = soup.find_all('div', {'class': "col-lg-6 d-none d-md-block"})
    for day in days_list:

        subj_list = day.find_all('tr')
        day_tmp = []

        for i in range(2, len(subj_list)):
            
            sb_tmp = dict()
            
            if subj_list[i].find('td', {'class': "text-info-bold"}) and subj_list[i].find('td', {'class': "text-info-bold"}).text != ' ':
                sb_tmp['chisl'] = subj_list[i].find('td', {'class': "text-info-bold"}).text
            if subj_list[i].find('td', {'class':"text-primary"}) and subj_list[i].find('td', {'class':"text-primary"}).text != ' ':
                sb_tmp['znam'] = subj_list[i].find('td', {'class':"text-primary"}).text
            if subj_list[i].find('td', {'colspan':"2"}):
                sb_tmp['gen'] = subj_list[i].find('td', {'colspan':"2"}).text 
            if len(sb_tmp) != 0:
                sb_tmp['time'] = subj_list[i].find('td', {'class': "bg-grey text-nowrap"}).text
                day_tmp.append(sb_tmp)
            
            
        days.append(day_tmp)
    return days


