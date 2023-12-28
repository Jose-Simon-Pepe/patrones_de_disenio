from . import *

"""
Cliente del builder

Instanciar una app
"""

# Basico

builder = Builder()

app = builder.with_this_repo(repo2).with_context("server").build()

# Instancias especificas

builder_mobile = ImpBuilder1()
builder_desktop = ImpBuilder2()
app_mobile = builder_mobile.with_config(var_name="this").build()
app_desktop = builder_desktop.with_config(config_path="/this/path/file.toml").build()







