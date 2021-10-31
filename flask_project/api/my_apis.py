from flask import abort, request, jsonify, make_response,\
    redirect, url_for, session
from flask_project import app, db
from flask_project.models.my_models import Note

@app.before_first_request
def init_db():
    """Create tables before first request"""
    try:
        db.create_all()
        app.logger.info('Active db.create_all')
    except Exception as e:
        print('Connect db error: %s' % e)
        app.logger.error('Connect db error: %s' % e)

@app.route('/apitest')
def apitest():
    app.logger.info('recv_api_req, /apitest')
    return "{api test ok!}"

@app.route('/login')
def login():
    #----add login success fun---
    #-----
    #----------------------------
    session['logged_in'] = True
    return redirect(url_for('hello'))

@app.route('/set/<name>')
def set_cookie(name):
    response = make_response(redirect(url_for('hello')))
    response.set_cookie('name', name)
    return response

@app.route('/')
@app.route('/hello')
def hello():
    name = request.args.get('name')
    if name is None:
        name = request.cookies.get('name', 'Human')
        response = "{'name':'%s'}" % name
    if 'logged_in' in session:
        response += '[Authenticated]'
    else:
        response += '[Not Authenticated]'
    return response
    # return jsonify({'name':'hjj', 'gender':'swf', 'default_name':'%s' % name})

@app.route('/add_note')
def add_note():
    note1 = Note(body='hjj11')
    note2 = Note(body='sjj11')
    db.session.add(note1)
    db.session.add(note2)
    db.session.commit()
    return "{'state':'%s'}" % 200

@app.route('/get_note_all')
def get_note_all():
    note_all = Note.query.all()
    res = []
    for i in note_all:
        res.append(i.body)
    return "{note all is : '%s'}" % res

@app.route('/get_note_by_id/<id>')
def get_note_by_id(id):
    note_info = Note.query.get(id)
    return "{note %s info is: %s}" % (id, note_info.body)

@app.route('/update_note_by_id/<id>')
def update_note_by_id(id):
    note = Note.query.get(id)
    note.body = "new sjj sjj"
    db.session.commit()
    note_info = Note.query.get(id)
    return "{note %s new info is: %s}" % (id, note_info.body)

@app.route('/delete_note_by_id/<id>')
def delete_note_by_id(id):
    note = Note.query.get(id)
    db.session.delete(note)
    db.session.commit()
    return "{delete ok}"