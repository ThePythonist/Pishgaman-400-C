info = [
    {'name':'sorena','age':17,'job':'backend-developer'},
    {'name':'mohammad','age':24,'job':'backend-developer'},
    {'name':'ali','age':21,'job':'frontend-developer'},
    {'name':'navid','age':21,'job':'db-man'},
]

html = """
<!DOCTYPE html>
<html>
<head>
<style>
#customers {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

#customers td, #customers th {
  border: 1px solid #ddd;
  padding: 8px;
}

#customers tr:nth-child(even){background-color: #f2f2f2;}

#customers tr:hover {background-color: #ddd;}

#customers th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #40aa77;
  color: white;
}
</style>
</head>
<body>

<table id="customers">
    <tr>
    <th>Name</th>
    <th>Job Title</th>
    <th>Age</th>
    </tr>
"""

for person in info :
    html += f"""
    <tr>
    <td>{person["name"]}</td>
    <td>{person["age"]}</td>
    <td>{person["job"]}</td>
    </tr>
    """

html += """
</table>
</body>
</html>
"""

open('info.html','w').write(html)
print('Done')
