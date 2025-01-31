from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict
from supabase import create_client, Client, ClientOptions

from logger import get_logger

logger = get_logger(__name__)


class SupabaseSettings(BaseSettings):
    model_config = SettingsConfigDict(validate_default=False, env_file='.env', env_file_encoding='utf-8', extra='ignore')
    supabase_url: str = None
    supabase_key: str = None


settings = SupabaseSettings()
_supabase_client: Optional[Client] = None


def get_supabase_client() -> Client:
    global _supabase_client
    if _supabase_client is None:
        _supabase_client = create_client(
            settings.supabase_url,
            settings.supabase_key,
        )
    return _supabase_client
