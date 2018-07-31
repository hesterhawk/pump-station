from app import app
from app.config.app import Config

app.run(host='0.0.0.0', port=8080, threaded=True, debug=Config.DEBUG_APP)