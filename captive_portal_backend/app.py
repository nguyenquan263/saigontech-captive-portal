from controllers.info_controller import app

if __name__ == '__main__':
    app.run(debug=True,port=8080 ,threaded=True, host='0.0.0.0')