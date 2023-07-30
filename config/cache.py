from config import DEBUG

if DEBUG:
    HOST = '127.0.0.1'
    PORT = 6379
    PASSWORD = None
    DB = 0
else:
    HOST = 'r-wz98cz6to7n535qmokpd.redis.rds.aliyuncs.com'
    PORT = 6379
    PASSWORD = 'Acs123456'
    DB = 7
