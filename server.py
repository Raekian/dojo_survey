from flask import Flask, render_template, request
app = Flask(__name__)





@app.route('/')
def index():
    return render_template("index.jinja")

from flask import Flask, render_template, request, redirect # added request

@app.route('/result', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    name_from_form = request.form['Name']
    fav_location_from_form = request.form['Dojo_Location']
    favorite_language = request.form['Favorite_Language']
    comments = request.form['Comment']
    return render_template("show.jinja", name_on_template=name_from_form, fav_location_from_form=fav_location_from_form, favorite_language = favorite_language, commentbox = comments)





if __name__ == "__main__":
    app.run(debug=True)

