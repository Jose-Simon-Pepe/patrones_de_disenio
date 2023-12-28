from provider.comps import *
import pytest
from provider.example_builders import *
from tests.helpers import build_desktop_app,build_mobile_app

repo = repo2
context = "server"




def test_basic_builder_should_build_an_app():
    builder = Builder()
    app = builder.with_this_repo(repo2).with_context(context).build()
    assert type(app) is application
    assert app._repo == repo
    assert app._context == context





def test_imp_builder_should_build_an_app():
    builder = ImpBuilder()
    app = builder.with_this_repo(repo2).with_context(context).build()
    assert type(app) is application
    assert app._repo == repo
    assert app._context == context 





def test_builder_1_and_2_should_build_different_apps(app_mobile,app_desktop):
    """
    Se construyen dos apps, una mobile y otra desktop
        Contexto esta predefinido, configuracion se carga de diferente manera
    """
    assert type(app_desktop) is application
    assert type(app_mobile) is application
    # ACA ES DONDE DIFIEREN
    assert not app_mobile._config == app_desktop._config





def test_desk_concrete_app_builded(app_desktop):
    assert type(app_desktop._config) is dict
    assert app_desktop._context is "DESKTOP"





def test_mobile_concrete_app_builded(app_mobile):
    assert type(app_mobile._config) is list
    assert app_mobile._context is "MOBILE"





def test_build_director_should_build_app():
    director = AppBuildDirector()
    app_mobile = director.build_mobile_app(ImpBuilder1())
    app_desktop = director.build_desktop_app(ImpBuilder2())
    assert type(app_mobile._config) is list
    assert type(app_desktop._config) is dict




