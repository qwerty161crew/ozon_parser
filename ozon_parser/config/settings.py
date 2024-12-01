from pydantic_settings import BaseSettings, SettingsConfigDict

ENV_PREFIX = ".env"


class ServerSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix=ENV_PREFIX)
    host: str = "localhost"
    port: int = 8000
    debug: bool = True
    reload: bool = True
    app_name: str = "My Application"


class RabbitmqSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix=ENV_PREFIX)
    host: str = "localhost"
    port: int = 5672
    user: str = "guest"
    password: str = "guest"


class PostgresSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix=ENV_PREFIX)
    db_name: str = "parser"
    db_user: str = "postgres"
    db_host: str = "127.0.0.1"
    db_port: int = 5431
    db_password: str = "1917"

    @property
    def db_url(self):

        return f"postgresql+asyncpg://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"


class Config(BaseSettings):
    """Describes application config."""

    class Config:
        env_file: str = ENV_PREFIX

    app: ServerSettings
    postgresql: PostgresSettings
    rabbig_mq: RabbitmqSettings

    @classmethod
    def create(cls) -> "Config":
        return Config(
            app=ServerSettings(),
            rabbig_mq=RabbitmqSettings(),
            postgresql=PostgresSettings(),
            # # security=Security(),
        )
