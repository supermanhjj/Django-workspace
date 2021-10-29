#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_project import app, db

@app.before_first_request
def init_db():
    """Create tables before first request"""
    try:
        db.create_all()
        app.logger.error('Active db.create_all')
    except Exception as e:
        print('Connect db error: %s' % e)
        app.logger.error('Connect db error: %s' % e)

if __name__ == "__main__":
    # 将host设置为0.0.0.0，则外网用户也可以访问到这个服务
    app.logger.info('Start app.run')
    app.run(host="0.0.0.0", port=5000, debug=True, processes=True)