from pydantic_settings import BaseSettings, SettingsConfigDict

ENV_PREFIX = ".env"


class ServerSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix=ENV_PREFIX)
    host: str = "localhost"
    port: int = 8000
    debug: bool = True
    reload: bool = True
    app_name: str = "My Application"


class PostgresSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix=ENV_PREFIX)
    db_name: str = "parser"
    db_user: str = "postgres"
    db_host: str = "localhost"
    db_port: int = 5432
    db_password: str = "1917"

    @property
    def db_url(self):
        return f"postgresql+asyncpg://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"


class Config(BaseSettings):
    """Describes application config."""

    class Config:
        env_file: str = ENV_PREFIX

    app: ServerSettings
    # prefixes: APIPrefixes
    postgresql: PostgresSettings
    # security: Security

    @classmethod
    def create(cls) -> "Config":
        return Config(
            app=ServerSettings(),
            # prefixes=APIPrefixes(),
            postgresql=PostgresSettings(),
            # # security=Security(),
        )
