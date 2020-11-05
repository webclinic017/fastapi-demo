import json
from pathlib import Path
import os
config_path= Path(__file__).with_name("config.json")

class Config:
    '''
    配置文件类
    '''
    @classmethod
    def load(cls):
        with open(config_path) as config_file:
            config = json.load(config_file)
            cur_used = config.get('USED','')
            if cur_used:
                config = config.get(cur_used,{})
                env = config.get('env', {})
                if env:
                    for k, v in env.items():
                        os.environ[k] = v
            return config


    @classmethod
    def init_app(cls,app):
        config = cls.load()
        return app.config


fs_config = Config.load()


