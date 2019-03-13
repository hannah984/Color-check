#!/usr/local/bin/python3


import cgi, cgitb

form = cgi.FieldStorage()

v_name = form.getvalue('name')
v_color = form.getvalue('color')

color_list = []


with open("colors.csv", "r") as colors:
	readline = colors.readline()

	while readline:
		color_list.append(readline)
		readline = colors.readline()


for i in color_list:
	color_list[color_list.index(i)] = i.split(',')


for i in color_list:
	for j in i:
		if v_color == j:
			v_color = j
		else:
			pass




# send an html response.
print("""
<html>
<body>
<p>
Thanks, %s, %s
</p>
</body>
</html>
""" % (v_name, v_color))
