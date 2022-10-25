import requests

url = "https://russianwarship.rip/api/v1/statistics/latest"
response = requests.get(url)
json = response.json()
data = json['data']
increase = data['increase']
stats = data['stats']
personnel, tanks, armoured_fighting_vehicles, artillery_systems, mlrs, aa_warfare_systems, warships_cutters, special_military_equip, atgm_srbm_systems = stats['personnel_units'], stats['tanks'], stats['armoured_fighting_vehicles'], stats['artillery_systems'], stats['mlrs'], stats['aa_warfare_systems'], stats['warships_cutters'], stats['special_military_equip'], stats['atgm_srbm_systems']
personnel_increase = increase['personnel_units']
tanks_increase = increase['tanks']
armoured_fighting_vehicles_increase = increase['armoured_fighting_vehicles']
artillery_systems_increase = increase['artillery_systems']
mlrs_increase = increase['mlrs']
aa_warfare_systems_increase = increase['aa_warfare_systems']
warships_cutters_increase = increase['warships_cutters']
special_military_equip_increase = increase['special_military_equip']
atgm_srbm_systems_increase = increase['atgm_srbm_systems']

war_stats_txt = f"за час повномасштабного вторгнення chamr на територію України:\n \nЗнищено, кількість, (\"поповнення\") \n \n chamriv {personnel}  (+{personnel_increase}) \nчмоня 1 (0) \nтанки {tanks}  (+{tanks_increase}) \n бібіки {armoured_fighting_vehicles}  (+{armoured_fighting_vehicles_increase}) \nартилерійські устаговки {artillery_systems}  (+{artillery_systems_increase}) \nРеактивні системи залпового вогню {mlrs}  (+{mlrs_increase}) \nППО {aa_warfare_systems}  (+{aa_warfare_systems_increase}) \nРПГ {atgm_srbm_systems}  (+{atgm_srbm_systems_increase}) \nспец. спорядження {special_military_equip}  (+{special_military_equip_increase}) \n , бойові дельфіни {warships_cutters} (+{warships_cutters_increase})) "