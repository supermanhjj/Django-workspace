#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_project import app, db
from flask_project.api import my_apis, face_recognition_apis

if __name__ == "__main__":
    # 将host设置为0.0.0.0，则外网用户也可以访问到这个服务
    app.logger.info('Start app.run')
    app.run(host="0.0.0.0", port=5000, debug=True, processes=True)