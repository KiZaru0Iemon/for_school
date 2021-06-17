import json
import glob

# /jsonファイル検索/
json_file_names = glob.glob('json_data/*.json')

# === 変数定義 ===
mother_data = []  #母データ
range_files_num = range(len(json_file_names))  #for分簡略用変数
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
        elif protocol == 'http/2.0':
            http20_counts[i] += 1
        elif protocol == 'http/3.0':
            http30_counts[i] += 1
        elif protocol == 'h3-29':
            h3_29_counts[i] += 1

# print(http10_counts)
# print(http11_counts)
# print(http20_counts)
# print(http30_counts)
# print(h3_29_counts)

# for i in range_files_num:
#     print(use_protocol_names[i])

for i in range_files_num:
    http10_percent.append(
        str(http10_counts[i] / use_protocol_num[i] * 100) + '%')
    http11_percent.append(
        str(http11_counts[i] / use_protocol_num[i] * 100) + '%')
    http20_percent.append(
        str(http20_counts[i] / use_protocol_num[i] * 100) + '%')
    http30_percent.append(
        str(http30_counts[i] / use_protocol_num[i] * 100) + '%')
    h3_29_percent.append(
        str(h3_29_counts[i] / use_protocol_num[i] * 100) + '%')

# /確認用/
print('=========================================')
for i in range_files_num:
    url_start = json_file_names[i].rfind('\\') + 1
    url_end = json_file_names[i].rfind('.json')
    print('url : ' + json_file_names[i][url_start:url_end] + '\n')
    print('protocol sum : ' + str(use_protocol_num[i]) + '\n')
    print('http/1.0 : ' + str(http10_counts[i]) + ' /' +
          str(use_protocol_num[i]) + '  ' + http10_percent[i])
    print('http/1.1 : ' + str(http11_counts[i]) + ' /' +
          str(use_protocol_num[i]) + '  ' + http11_percent[i])
    print('http/2.0 : ' + str(http20_counts[i]) + ' /' +
          str(use_protocol_num[i]) + '  ' + http20_percent[i])
    print('http/3.0 : ' + str(http30_counts[i]) + ' /' +
          str(use_protocol_num[i]) + '  ' + http30_percent[i])
    print('h3-29    : ' + str(h3_29_counts[i]) + ' /' +
          str(use_protocol_num[i]) + '  ' + h3_29_percent[i])
    print('\n=========================================')
