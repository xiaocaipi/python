import web
def _create_db():
    host = '192.168.1.32'
    db = 'test'
    port = 3306
    user = 'root'
    pw = ''
    try:
        import sae.const
        db = sae.const.MYSQL_DB
        user = sae.const.MYSQL_USER
        pw = sae.const.MYSQL_PASS
        host = sae.const.MYSQL_HOST
        port = int(sae.const.MYSQL_PORT)
    except ImportError:
        pass
    return web.database(dbn='mysql', host=host, port=port, db=db, user=user, pw=pw)