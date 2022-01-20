from dotenv import dotenv_values

class Env:
    
    def __init__(self, config_env: str) -> None:
        self.config_env = config_env

    def get(self):
        return dotenv_values(dotenv_path='.env')[self.config_env]