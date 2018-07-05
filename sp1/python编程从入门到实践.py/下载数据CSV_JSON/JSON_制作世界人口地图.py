#Pygal中的国别码储存在模块il8n中，population数据集中是三个字母的国别码，而pygal是两个字母，因此需要写个函数
from pygal_maps_world.i18n import COUNTRIES
def get_country_code(country_name):
	for code,name in COUNTRIES.items():
		if name == country_name:
			return code
			#如果没有找到指定国家，则返回NONE
	return None

import json
#将数据加载进来
with open("population_data.json") as f:
	pop_data = json.load(f)
	print(pop_data)
#打印每个国家2010年的人口
#创建一个包含人口数量的字典
# import pygal.maps.world
# cc_populations = {}
# for pop_dict in pop_data:
# 	if pop_dict["Year"] == "2010":
# 		country_name = pop_dict["Country Name"]
# 		population = int(pop_dict["Value"])#将人口转换为数字
# 		code = get_country_code(country_name)
# 		if code:
# 			cc_populations[code] = population
# wm = pygal.maps.world.World()
# wm.title = "World Population in 2010"
# wm.add("2010",cc_populations)
# wm.render_to_file("test.svg")
