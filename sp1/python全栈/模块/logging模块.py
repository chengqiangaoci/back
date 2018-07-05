import logging
# -*- encoding:"utf-8" -*-
#以下是五个级别，重要级别依次递增，默认warning级别及以上
# logging.debug("debug message")
# logging.info("info message")
# logging.warning("warning message")
# logging.error("error message")
# logging.critical("critical message")

#进行参数设定，调整级别
# logging.basicConfig(
# 	level = logging.DEBUG)#这样就全部打印了
# logging.debug("debug message")
# logging.info("info message")
# logging.warning("warning message")
# logging.error("error message")
# logging.critical("critical message")

#将日志放在文件里:追加模式
# logging.basicConfig(
# 	level = logging.DEBUG,
# 	filename = "logger.log")#生成一个文本，信息存在这
# logging.debug("debug message")
# logging.info("info message")
# logging.warning("warning message")
# logging.error("error message")
# logging.critical("critical message")

#将日志放在文件里：w模式(覆盖删除)
# logging.basicConfig(
# 	level = logging.DEBUG,
# 	filename = "logger.log",
# 	filemode = "w")#生成一个文本，信息存在这
# logging.debug("debug message")
# logging.info("info message")
# logging.warning("warning message")
# logging.error("error message")
# logging.critical("critical message")

#显示时间
# logging.basicConfig(
# 	level = logging.DEBUG,
# 	filename = "logger.log",
# 	filemode = "w",
# 	format = "%(asctime)s")#显示时间
# logging.debug("debug message")
# logging.info("info message")
# logging.warning("warning message")
# logging.error("error message")
# logging.critical("critical message")

#显示文件中的行数内容，文件名(中文的话就很麻烦)
# logging.basicConfig(
# 	level = logging.DEBUG,
# 	filename = "logger.log",
# 	filemode = "w",
# 	format = "%(asctime)s %(filename)s %(lineno)d %(message)s")#打印在第多少行，警告的内容
# logging.debug("debug message")
# logging.info("info message")
# logging.warning("warning message")
# logging.error("error message")
# logging.critical("critical message")



#logger同时打印在屏幕和日志文件里里
# def logger():
# 	logger = logging.getLogger()
# 	fh = logging.FileHandler("test.log")#向文件发送内容
# 	ch = logging.StreamHandler()#向屏幕发送内容
# 	fm = logging.Formatter("%(asctime)s %(message)s")#定义格式
# 	fh.setFormatter(fm)
# 	ch.setFormatter(fm)
# 	logger.addHandler(fh)
# 	logger.addHandler(ch)
# 	logger.setLevel("DEBUG")#设置优先级别
# 	return logger

# logger = logger()
# logger.debug("debug message")
# logger.info("info message")
# logger.warning("warning message")
# logger.error("error message")
# logger.critical("critical message")














