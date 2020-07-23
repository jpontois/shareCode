from flask import Flask, request, render_template, \
    redirect

from model_sqlite import createTables, \
    createCode, \
    getCode, \
    getAllCode, \
    updateCode, \
    createEdition, \
    getEdition

app = Flask(__name__)
createTables()

# ---------------------------------------------------------

@app.route('/')
def index():
    d = getAllCode()
    return render_template('index.html',**d)

# ---------------------------------------------------------

@app.route('/create')
def create():
    uid = createCode()
    return redirect("{}edit/{}".format(request.host_url,uid))

# ---------------------------------------------------------

@app.route('/edit/<string:uid>/')
def edit(uid):
    row = getCode(uid)

    if row is None:
        return render_template('error.html',uid=uid)

    d = dict(
        uid=row[0][0],
        code=row[0][1],
        language=row[0][2],
        url="{}view/{}".format(request.host_url,uid)
    )

    return render_template('edit.html', **d) 

# ---------------------------------------------------------

@app.route('/publish',methods=['POST'])
def publish():
    code = request.form['code']
    uid  = request.form['uid']
    language  = request.form['language']
    updateCode(uid, code, language)
    return redirect("{}{}/{}".format(request.host_url,
                                     request.form['submit'],
                                     uid))

# ---------------------------------------------------------

@app.route('/view/<string:uid>/')
def view(uid):
    row = getCode(uid)

    if row is None:
        return render_template('error.html',uid=uid)

    d = dict(
        uid=row[0][0],
        code=row[0][1],
        language=row[0][2],
        url="{}view/{}".format(request.host_url,uid)
    )

    return render_template('view.html', **d)

# ---------------------------------------------------------

@app.route('/admin/')
def admin():
    pass

# ---------------------------------------------------------

if __name__ == '__main__':
    app.run()

