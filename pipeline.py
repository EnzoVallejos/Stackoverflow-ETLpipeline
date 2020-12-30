from Extract.Extract_module import Extract
from Transform.Transform_module import Transform
from Load.Load_module import Load
from pathlib import Path
import os
from rich import print
from rich.progress import track

cont = 0
cant_pag = 100
urls = ("https://es.stackoverflow.com/questions", 
		"https://es.stackoverflow.com/questions?tab=active&page=")
path = os.path.join(Path(__file__).resolve(strict=True).parent.parent, 'src/csv_generate')

for i in range(cant_pag):
	if cont < 1:
		url = urls[0]
	else:
		url = urls[1] + str(cont)

	print('[bold blue]Page {}:[/bold blue] getting html from url [blue]"{}"'.format(cont, url))
	html = Extract(url)

	print('[bold blue]Page {}:[/bold blue] get and transform html information'.format(cont))
	for step in track(range(3), description="[blue]transforming the data... "):
		data = Transform(html)
	
	print('[bold blue]Page {}:[/bold blue] saving in csv file the information in the path [bold green]{}\n'.format(cont, path+'/Stackoverflow_data.csv'))
	Load(data, path)

	cont += 1

print("[bold cyan]finished web scrapping!!!")