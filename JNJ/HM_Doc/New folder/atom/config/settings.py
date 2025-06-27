from typing import Optional, List

from dynaconf import Dynaconf

from argument_constants import PATH_TO_DEFAULT_CONFIG
from utilities.configuration_models import EnvironmentType


def get_settings(env: EnvironmentType, extra_configs: Optional[List[str]] = None, **kwargs):
    config_files = [PATH_TO_DEFAULT_CONFIG]
    config_files.extend(extra_configs or [])
    config_files.append("config/.secrets.toml")
    return Dynaconf(
        envvar_prefix="ATOM",
        # settings_files=[PATH_TO_DEFAULT_CONFIG, PATH_TO_TEMP_CONFIG, "config/.secrets.toml"],
        settings_files=config_files,
        environments=True,
        default_env="DEFAULT",
        merge_enabled=True,
        env=env.name,
        **kwargs
    )
