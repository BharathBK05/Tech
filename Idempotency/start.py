from controller.controller import app

PORT = 8085

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=PORT, threaded=True)
