import config
from app import create_app

# 创建应用 1
app = create_app(config)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
