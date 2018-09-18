from preparation.init import app, db, list_code
from models.info import info, info_schema
from flask import request, jsonify
import random

ifs = info_schema()
ifss = info_schema(many = True)

@app.route("/info", methods=["GET"])
def get_all_info():
    try:
        all_info = info.query.all()
        result = ifss.dump(all_info)
        return jsonify(
            error_code = 0,
            message = "Query Execute Completely.",
            data = result.data
        )
    except:
        return jsonify(
            error_code = 1,
            message = "Database Error."
        )

@app.route("/info", methods=["POST"])
def add_info():
    try:
        name = request.json.get('name')
        is_student = request.json.get('is_student')
        phone = request.json.get('phone')
        need = request.json.get('need')

        code = str(random.randint(1000, 9999))
        while list_code.count(code) > 0:
            code = str(random.randint(1000, 9999))



        print(list_code)
        new_info = info(name, is_student, phone, need)

        db.session.add(new_info)
        db.session.commit();
        list_code.append(code)

    except:
        return jsonify(
            error_code="2",
            message="Adding failed."
        )

    # tien hanh gui den so nguoi dung thong qua tin nhan
    return jsonify(
        error_code=0,
        message="Adding completed.",
        validate_code=code

    )

@app.route("/check", methods=["POST"])
def check_number():
    vali_number = str(request.json.get('validate_number'))
    print(list_code)
    if list_code.count(vali_number) > 0:
        #so dien thoai chinh xac
        return jsonify(
            error_code = 0,
            message = 'Success'
        )
    else:
        #so dien thoai khong chinh xac
        return jsonify(
            error_code = 3,
            message = 'Fail'
        )

