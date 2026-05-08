from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    mongo_username: str
    mongo_password: str
    mongo_host: str
    mongo_port: int
    mongo_database: str

    @property
    def MONGO_URI(self):
        return (
            f"mongodb://{self.mongo_username}:{self.mongo_password}"
            f"@{self.mongo_host}:{self.mongo_port}/{self.mongo_database}?authSource=admin"
        )

    class Config:
        env_file = ".env"

settings = Settings()