import configparser
import os


# 读取ini配置文件
class Config:
    def __init__(self):
        # 获取一个config对象
        self.config = configparser.ConfigParser()

    def read_config(self, config_filename, section, key):
        '''
        :param config_filename: 配置文件路径
        :param section: section
        :param key: key
        :return: 读取到的可以值
        '''
        # 获取需要读取的配置文件的路径
        config_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + r'\config\{}'.format(config_filename)
        # 读取配置文件
        self.config.read(config_path, encoding='utf-8')
        return self.config.get(section, key)


if __name__ == '__main__':
    myConfig = Config()
    print(myConfig.read_config('mysql_db.ini', 'mysql_db', 'charset'))