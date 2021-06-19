#仕様については，README.mdファイルを確認してください。(errorについても少し書いてあります。)

import json
import glob

# /jsonファイル検索/
json_file_names = glob.glob('json_data/*.json')

# === 変数定義 ===
mother_data = []  #母データ
files_num = len(json_file_names)
range_files_num = range(files_num)  #for分簡略用変数
http10_counts = [0 for i in range_files_num]
http11_counts = [0 for i in range_files_num]
http20_counts = [0 for i in range_files_num]
http30_counts = [0 for i in range_files_num]
h3_29_counts = [0 for i in range_files_num]
http10_percent = []
http11_percent = []
http20_percent = []
http30_percent = []
h3_29_percent = []
http10_average = 0
http11_average = 0
http20_average = 0
http30_average = 0
h3_29_average = 0

# /json読み込み/
for fname in json_file_names:
    open_file = open(fname, 'r')
    mother_data.append(json.load(open_file))

# /使っている総プロトコル数計算/
use_protocol_num = [len(num['log']['entries']) for num in mother_data]
range_use_protocol_num = [range(num) for num in use_protocol_num]

# /使用プロトコル名抽出/
use_protocol_names = [[] for i in range_files_num]
for i in range_files_num:
    for j in range_use_protocol_num[i]:
        use_protocol_names[i].append(
            mother_data[i]['log']['entries'][j]['response']['httpVersion'])

# /使用している各プロトコル数計算/
for i, protocols in enumerate(use_protocol_names):
    for protocol in protocols:
        protocol = protocol.lower()
        if protocol == 'http/1.0':
            http10_counts[i] += 1
        elif protocol == 'http/1.1':
            http11_counts[i] += 1
        elif protocol == 'http/2.0' or protocol == 'h2' or protocol == 'h2c':
            http20_counts[i] += 1
        elif protocol == 'http/3.0':
            http30_counts[i] += 1
        elif protocol == 'h3-29':
            h3_29_counts[i] += 1

# /各プロトコルの使用率/
for i in range_files_num:
    http10_percent.append(http10_counts[i] / use_protocol_num[i] * 100)
    http11_percent.append(http11_counts[i] / use_protocol_num[i] * 100)
    http20_percent.append(http20_counts[i] / use_protocol_num[i] * 100)
    http30_percent.append(http30_counts[i] / use_protocol_num[i] * 100)
    h3_29_percent.append(h3_29_counts[i] / use_protocol_num[i] * 100)

# /全体の平均計算/
for i in range_files_num:
    http10_average += http10_percent[i]
    http11_average += http11_percent[i]
    http20_average += http20_percent[i]
    http30_average += http30_percent[i]
    h3_29_average += h3_29_percent[i]
http10_average /= files_num
http11_average /= files_num
http20_average /= files_num
http30_average /= files_num
h3_29_average /= files_num

# /確認用/
print('=========================================')
for i in range_files_num:
    url_start = json_file_names[i].rfind('\\') + 1
    url_end = json_file_names[i].rfind('.json')
    print('url : ' + json_file_names[i][url_start:url_end] + '\n')
    print('protocol sum : ' + str(use_protocol_num[i]) + '\n')
    print('http/1.0 : ' + str(http10_counts[i]) + ' /' +
          str(use_protocol_num[i]) + '  ' + str(http10_percent[i]) + '%')
    print('http/1.1 : ' + str(http11_counts[i]) + ' /' +
          str(use_protocol_num[i]) + '  ' + str(http11_percent[i]) + '%')
    print('http/2.0 : ' + str(http20_counts[i]) + ' /' +
          str(use_protocol_num[i]) + '  ' + str(http20_percent[i]) + '%')
    print('http/3.0 : ' + str(http30_counts[i]) + ' /' +
          str(use_protocol_num[i]) + '  ' + str(http30_percent[i]) + '%')
    print('h3-29    : ' + str(h3_29_counts[i]) + ' /' +
          str(use_protocol_num[i]) + '  ' + str(h3_29_percent[i]) + '%')
    print('\n=========================================')

print('\n[the whole average]')
print('http/1.0 : ' + str(http10_average) + ' %')
print('http/1.1 : ' + str(http11_average) + ' %')
print('http/2.0 : ' + str(http20_average) + ' %')
print('http/3.0 : ' + str(http30_average) + ' %')
print('h3-29    : ' + str(h3_29_average) + ' %')
