from fontTools.ttLib import TTFont #pip install fontTools

t = TTFont('3944c230.woff')
t.saveXML('3944c230.xml')

# best_map = t['cmap'].getBestCmap()
# print(best_map)
#
# new_best_map = {}
# for key,value in best_map.items():
#     new_best_map[hex(key)] = value
# print(new_best_map)
#
new_map = {
    '0xee82':'1',
    '0xe2c5':'2',
    '0xe32e': '3',
    '0xeff7': '4',
    '0xf5a0': '5',
    '0xe463': '6',
    '0xea1c': '7',
    '0xed5a': '8',
    '0xebca': '9',
    '0xeac6': '0'
}
#
# new_data = {}
# for k,v in new_best_map.items():
#     new_data[k] = new_map[v]
rs = {}
for k,v in new_map.items():
    rs['&#' + k[1:] + ';'] = v
print(rs)

# req = requests.get('www.baidu.com')
#
# for k,v in rs.items():
#     req = req.replace(k,v)
