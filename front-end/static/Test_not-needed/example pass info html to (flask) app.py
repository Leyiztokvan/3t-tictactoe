

# html part

# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta http-equiv="X-UA-Compatible" content="IE=edge">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Document</title>
# </head>
# <body>
#         <form method="POST">
#             Location: <input name="location" type="text">
#             <input type="submit">
#         </form>
# </body>
# </html>



# app.py part

# @app.route('/form', methods=['GET', 'POST'])
# def form():
#     if request.method == 'POST':
#         print(request.form.get('location'))
        
#     return render_template("form.html")
