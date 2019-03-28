import webbrowser, requests

archivo = open("index.html", "w")
html = """<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>LSV TEAM</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Ubuntu">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
    <link rel="stylesheet" type="text/css" media="screen" href="main.css">
</head>

<body>
    <h1>LSV TEAM</h1>
    <h2>Fotos</h2>
    <hr>
    <center>
        <div class="padre">"""
response = requests.get('https://jsonplaceholder.typicode.com/photos')
fotos = response.json()
agregar = ""

for i in range(5):
    agregar += """<div class="card">
                <img src="{}" alt="Avatar" style="width:100%">
            </div>""".format(fotos[i]['thumbnailUrl'])
html += agregar
html += """
            <br>"""
agregar = ""

for i in range(5, 10):
    agregar += """<div class="card">
                <img src="{}" alt="Avatar" style="width:100%">
            </div>""".format(fotos[i]['thumbnailUrl'])
html += agregar
html += """
        </div>
        <hr>
        <h2>Users</h2>
        <div class="padre">
            <div class="container">
                <table class="table table-dark table-striped">
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Name</th>
                            <th>Username</th>
                            <th>Email</th>
                            <th>Phone</th>
                            <th>Website</th>
                        </tr>
                    </thead>
                    <tbody>"""
response = requests.get('https://jsonplaceholder.typicode.com/users')
users = response.json()
agregar = ""

for i in range(9):
    agregar += """<tr>
                            <td>{}</td>
                            <td>{}</td>
                            <td>{}</td>
                            <td>{}</td>
                            <td>{}</td>
                            <td>{}</td>
                        </tr>""".format(users[i]['id'], users[i]['name'], users[i]['username'], users[i]['email'],
                                        users[i]['phone'], users[i]['website'])
html += agregar
html += """
                    </tbody>
                </table>
            </div>
        </div>
        <hr>
        <h2>To dos</h2>
        <div class="padre">
            <div class="container">
                <table class="table table-dark table-striped">
                    <thead>
                        <tr>
                            <th>UserID</th>
                            <th>ID</th>
                            <th>Title</th>
                            <th>Completed</th>
                        </tr>
                    </thead>
                    <tbody>"""
response = requests.get('https://jsonplaceholder.typicode.com/todos')
todos = response.json()
agregar = ""

for i in range(9):
    agregar += """<tr>
                            <td>{}</td>
                            <td>{}</td>
                            <td>{}</td>
                            <td>{}</td>
                        </tr>""".format(todos[i]['userId'], todos[i]['id'], todos[i]['title'], todos[i]['completed'])
html += agregar
html += """
                        <tr>
                            <td>1</td>
                            <td>John</td>
                            <td>Doe</td>
                            <td>john@example.com</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
        <hr>
        <h2>Comments</h2>
        <div class="padre">
            <div class="container">
                <table class="table table-dark table-striped">
                    <thead>
                        <tr>
                            <th>PostID</th>
                            <th>ID</th>
                            <th>Name</th>
                            <th>email</th>
                            <th>body</th>
                        </tr>
                    </thead>
                    <tbody>"""
response = requests.get('https://jsonplaceholder.typicode.com/comments')
comments = response.json()
agregar = ""

for i in range(9):
    agregar += """<tr>
                            <td>{}</td>
                            <td>{}</td>
                            <td>{}</td>
                            <td>{}</td>
                            <td>{}</td>
                        </tr>""".format(comments[i]['postId'], comments[i]['id'], comments[i]['name'],
                                        comments[i]['email'], comments[i]['body'])
html += agregar
html += """

                    </tbody>
                </table>
            </div>
        </div>
    </center>
</body>

</html>"""
archivo.write(html)
archivo.close()
webbrowser.open_new_tab('index.html')
