from trajectory.handlers import *



### 创建日志操作对象
logger = logging.getLogger()
### 设置日志操作对象的日志等级
logger.setLevel(logging.INFO)
### 创建一个mongodb处理器，指定log_collection
# mongohandler = MongoHandler(log_database='trajectory',log_collection='testlog')
mongohandler = MongoHandler(log_database='drip',log_collection='log_info') # trajectory
### 设置mongodb处理器的日志等级
mongohandler.setLevel(logging.INFO)
### 向日志操作对象添加mongodb处理器
logger.addHandler(mongohandler)
logger.info('this is a info log')
logger.warning('this is a warning log')


