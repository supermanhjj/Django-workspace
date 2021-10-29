from flask import abort, request, jsonify, make_response,\
    redirect, url_for, session
from flask_project import app, db
from flask_project.models.my_models import Note, Face_Image_Store

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

@app.route('/img/upload_img', methods=['POST'])
def upload_image():
    try:
        file = request.files['file']
        image_data = file.read()
        image_name = file.filename
        people_name = request.files['people_name'].read()
    except Exception as e:
        return jsonify((dict(zip(("status", "message"), [1, 'decode request error: %s' % e]))))

    try:
        insert_image = Face_Image_Store(imageData=image_data, imageName=image_name, peopleName=people_name)
        db.session.add(insert_image)
        db.session.commit()
    except Exception as e:
        return jsonify((dict(zip(("status", "message"), [1, 'insert image to db error: %s' % e]))))

    return jsonify((dict(zip(("status", "message"), [0, 'upload image success']))))


@app.route('/img/get_images_from_store')
def get_images_from_store():
    all_store_images = Face_Image_Store.query.all()

    #offset+limit
    all_store_images = Face_Image_Store.query.offset(2).limit(2).all()

    #slice(start, end)
    all_store_images = Face_Image_Store.query[2, 2]

    #paginate
    # pn.items 获取该页的数据
    # pn.page 获取当前的页码
    # pn.pages 获取总页数
    all_store_images = Face_Image_Store.query.paginate(2, 3)

    res = []
    for i in all_store_images:
        res.append(i.body)
    return "{note all is : '%s'}" % res


# @app.route('/face_task_result')
# def face_task_result():
#     res = request.args.get('res')
#     if res is None:
#         name = request.cookies.get('name', 'Human')
#         response = "{'name':'%s'}" % name
#     if 'logged_in' in session:
#         response += '[Authenticated]'
#     else:
#         response += '[Not Authenticated]'
#     return response
#     # return jsonify({'name':'hjj', 'gender':'swf', 'default_name':'%s' % name})

@app.route("/insert_img")
def insert_img():
    fp = open("C://Download//620644_14.jpg", "rb")
    imageData = fp.read()
    imageName = "620644_14.jpg"
    peopleName = "hjjj"

    insert_image = Face_Image_Store(imageData=imageData, imageName=imageName, peopleName=peopleName)
    db.session.add(insert_image)
    db.session.commit()

    aa = {'name': 'hjj',
          'gender': 'swf',
          'default_name': '666',
          'info': {
              'aa': 'aa',
              'bb': 'bb'
          }}

    # return jsonify((dict(zip(("status", "message"), [0, 'success']))))
    return jsonify(aa)