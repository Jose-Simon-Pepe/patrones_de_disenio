import pytest
from provider.example_builders import ImpBuilder1, ImpBuilder2
@pytest.fixture(name="app_mobile")
def build_mobile_app():
    """
    crear una app mobile
    """
    builder_mobile = ImpBuilder1()
    return builder_mobile.with_config(var_name="this").build()

@pytest.fixture(name="app_desktop")
def build_desktop_app():
    """
    crear una app desktop
    """
    builder_desktop = ImpBuilder2()
    return builder_desktop.with_config(config_path="/this/path/file.toml").build()
