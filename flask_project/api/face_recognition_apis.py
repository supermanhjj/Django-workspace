from flask import abort, request, jsonify, make_response,\
    redirect, url_for, session
from flask_project import app, db
from flask_project.models.my_models import Note
from flask_project.models.face_recognition_models import Face_Image_Store

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