import logging
#配置logging
logging.basicConfig(filename="logging_file.txt", level = logging.INFO
            ,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#输出日志信息
logging.debug("调试信息")
logging.info("一般信息")
logging.warning("警告信息")
logging.error("错误信息")
logging.critical("严重错误")
