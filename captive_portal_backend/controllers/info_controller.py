from preparation.init import app, db, list_code, list_phone
from models.info import info, info_schema
from flask import request, jsonify
import random
import requests

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
        current_class = request.json.get('current_class')
        address = request.json.get('address')

        code = str(random.randint(1000, 999999))
        while list_code.count(code) > 0:
            code = str(random.randint(1000, 999999))



        print(list_code)
        new_info = info(name, is_student, current_class, address, phone, need)

        db.session.add(new_info)
        db.session.commit();
        list_code.append(code)
        list_phone.append(phone[1:len(phone)])

    except:
        return jsonify(
            error_code="2",
            message="Thông tin chưa đầy đủ"
        )

    # tien hanh gui den so nguoi dung thong qua tin nhan

    data = {
        'u': 'cdsaigon',
        'pwd': 'vaysb',
        'from': 'CDSG',
        'phone': '84'+phone[1:len(phone)],
        'sms': 'Ma xac nhan cua ban la:' + code,
        'bid': '1234'
    }

    r = requests.post(url = 'https://cloudsms.vietguys.biz:4438/api/index.php', data = data)

    return jsonify(
        error_code=0,
        message="Thành Công",
        validate_code=code

    )

@app.route("/check", methods=["POST"])
def check_number():
    vali_number = str(request.json.get('validate_number'))
    print(list_code)
    print(list_phone)
    if list_code.count(vali_number) > 0:
        #so dien thoai chinh xac
        return jsonify(
            error_code = 0,
            message = 'Thành Công'
        )
    else:
        #so dien thoai khong chinh xac
        return jsonify(
            error_code = 3,
            message = 'Thất Bại'
        )

@app.route("/send", methods = ["POST"])
def send_validate_code_again():
    try:
        phone = request.json.get('phone_number')
        phone = phone[1:len(phone)]
        print(phone)
        code = str(list_code[list_phone.index(phone)])
    except:
        return jsonify(
            errorCode = 4,
            message = "Hãy đăng kí lại!"
        )

    data = {
        'u': 'cdsaigon',
        'pwd': 'vaysb',
        'from': 'CDSG',
        'phone': '84' + phone,
        'sms': 'Day la ma xac nhan cua ban:' + code,
        'bid': '1234'
    }

    r = requests.post(url='https://cloudsms.vietguys.biz:4438/api/index.php', data=data)

    return jsonify(
        errorCode = 0,
        message = "Đoạn mã đã được gửi",
        validateCode = str(code)
    )

