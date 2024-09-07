from curl_cffi import requests


cookies = {
    'cf_clearance': 'cf_clearance=D_ijuJHFQO3q9YWWxYMa8RViioJdJfDed8hZVPE8GRM-1725725281-1.2.1.1-BOP6X2_qLQjXsnj6KpphINva8IFGm6O3wKm1UkdYa9kKNJMrDmtEwjFSKGbY.Y.QeYOE9.83ZjkcLQ0trCqvpT727mjLwx5BG_nTI_gV_OAJus9hoDQ239wol0vlCavXHUJo7VmOhF5GEyc8BoxF9bDyKayTCylehVm7bRAt7k7P10rLAkHhVbewflRiEpJhoNZpjlaaNlQsTRkfdPVP3I3F_sr7ruvB2ghzCrNUxJesrt9559IFWT4cVOLXafZjny6RY17gkA1iuGPlKDiWGI1ei_f0K76kAgg6j2y8DtQ9_iIPJtHHyHh3g9fpwU5Fil15_ZdTyj0g6G1L9Xxww8n659jITaB8Ftn8Sr1uOYZJrckQhnQmCwam4Y014wEQcg9W3AMDyQfm5eloclWUQhTcVYwUNwT0gbuukVTrSBkQR8uxg82.9fDnP3vlO4DvpHM2lY0MJ1b2B5.SqiwrXg',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'cookie': 'cf_clearance=D_ijuJHFQO3q9YWWxYMa8RViioJdJfDed8hZVPE8GRM-1725725281-1.2.1.1-BOP6X2_qLQjXsnj6KpphINva8IFGm6O3wKm1UkdYa9kKNJMrDmtEwjFSKGbY.Y.QeYOE9.83ZjkcLQ0trCqvpT727mjLwx5BG_nTI_gV_OAJus9hoDQ239wol0vlCavXHUJo7VmOhF5GEyc8BoxF9bDyKayTCylehVm7bRAt7k7P10rLAkHhVbewflRiEpJhoNZpjlaaNlQsTRkfdPVP3I3F_sr7ruvB2ghzCrNUxJesrt9559IFWT4cVOLXafZjny6RY17gkA1iuGPlKDiWGI1ei_f0K76kAgg6j2y8DtQ9_iIPJtHHyHh3g9fpwU5Fil15_ZdTyj0g6G1L9Xxww8n659jITaB8Ftn8Sr1uOYZJrckQhnQmCwam4Y014wEQcg9W3AMDyQfm5eloclWUQhTcVYwUNwT0gbuukVTrSBkQR8uxg82.9fDnP3vlO4DvpHM2lY0MJ1b2B5.SqiwrXg',
    'origin': 'https://openchat.team',
    'prefer': 'safe',
    'priority': 'u=1, i',
    'referer': 'https://openchat.team/',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Microsoft Edge";v="128"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"128.0.2739.63"',
    'sec-ch-ua-full-version-list': '"Chromium";v="128.0.6613.120", "Not;A=Brand";v="24.0.0.0", "Microsoft Edge";v="128.0.2739.63"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"15.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0',
    'x-kl-kis-ajax-request': 'Ajax_Request',
}
prompt = str(input("Enter A prompt: "))
json_data = {
    'model': {
        'id': 'openchat_3.6',
        'name': 'OpenChat 3.6 (latest)',
        'maxLength': 24576,
        'tokenLimit': 8192,
    },
'messages': [
        {
            'role': 'user',
            'content': 'hi',
        },
        {
            'role': 'assistant',
            'content': 'Hello! How can I help you today?',
        },
        {
            'role': 'user',
            'content': prompt,
        },
    ],
    'key': '',
    'prompt': ' ',
    'temperature': 0.5,
}

response = requests.post('https://openchat.team/api/chat', cookies=cookies, headers=headers, json=json_data)

print(response.text)