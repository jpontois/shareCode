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
    return render_template('index.html', data = getAllCode())

# ---------------------------------------------------------

@app.route('/create')
def create():
    uid = createCode()
    createEdition(uid, request.remote_addr, request.user_agent.string)
    return redirect("{}edit/{}".format(request.host_url,uid))

# ---------------------------------------------------------

@app.route('/edit/<string:uid>/')
def edit(uid):
    row = getCode(uid)

    if row is None:
        return render_template('error.html',uid = uid)

    d = dict(
        uid=uid,
        code=row[0],
        language=row[1],
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
    createEdition(uid, request.remote_addr, request.user_agent.string)

    return redirect(
        "{}{}/{}".format(request.host_url,
        request.form['submit'],
        uid)
    )

# ---------------------------------------------------------

@app.route('/view/<string:uid>/')
def view(uid):
    row = getCode(uid)

    if row is None:
        return render_template('error.html',uid = uid)

    d = dict(
        uid=uid,
        code=row[0],
        language=row[1],
        url="{}view/{}".format(request.host_url,uid)
    )

    return render_template('view.html', **d)

# ---------------------------------------------------------

@app.route('/admin/')
def admin():
    return render_template('admin.html', data = getEdition())

# ---------------------------------------------------------

if __name__ == '__main__':
    app.run()

