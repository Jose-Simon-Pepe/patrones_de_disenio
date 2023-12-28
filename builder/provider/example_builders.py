from .comps import *
"""
Patron de diseño Builder

Ejemplo:

Construir un componente de Application

Nota: Las llamadas a los builders/directors estan en ../consumer/
"""

# Basico
    # En caso de tener valores obligatorios, pueden escribirse desde el builder
    # Caso contrario, se obviaran

class application:
    def __init__(self,repo=None,context=None,optional=None,config=None): 
        self._repo = repo
        self._context:str = context
        self._another_optional_thing:str = optional
        self._config =config 

class Builder:

    def __init__(self):
        self._repo = repo1() #si el cliente no indica uno diferente, se usara este
        self._another_optional_thing:str = None
        self._config = None

    def with_this_repo(self,repo):
        self._repo=repo 
        return self

    def with_context(self,context):
        self._context = context
        return self

    def with_optional(self,optional:str):
        self._another_optional_thing = optional 
        return self
    
    def build(self):
        return application(repo=self._repo,context=self._context,config=self._config)

# Se puede escribir una interfaz para el builder con los pasos
#
# ¿No seria mejor usar herencia si los withs simplemente requieren inicializar una variable?
class APPBUILDER:
    def with_this_repo(self,repo):
        pass

    def with_context(self,context):
        pass
    
    def with_optional(self,optional:str):
        pass

    def with_config(self,config_source:str):
        pass

class ImpBuilder(APPBUILDER):

    def __init__(self):
        super().__init__()
        self._repo = repo1() #si el cliente no indica uno diferente, se usara este
        self._another_optional_thing:str = None 
        self._config = None
 
    def with_this_repo(self,repo):
        self._repo=repo 
        return self

    def with_context(self,context):
        self._context = context
        return self
    
    def with_optional(self,optional:str):
        self._another_optional_thing = optional 
        return self
    
    def build(self):
        return application(repo=self._repo,context=self._context,optional=self._another_optional_thing,config=self._config)

         
# Se puede utilizar implementaciones en concreto para especificos tipos de instancia
# En este ejemplo with_config DIFIERE su implementacion 
#NOTE: Lo ideal seria instanciar diferentes TIPOS de objeto entre builders, por ejemplo AppMobile() y AppDesktop() sin embargo no lo incorporo al ejemplo para hacerlo rapido

class ImpBuilder1(APPBUILDER):
    # Builder para app mobile con config en variables de entorno 

    def __init__(self):
        super().__init__()
        self._repo = repo1() #si el cliente no indica uno diferente, se usara este
        self._another_optional_thing:str = None 
        self._context = "MOBILE"
        self._config = None

    def with_config(self,var_name=None):
        #vars = os.environ[var_name]
        vars = ["one","two","three"]
        self._config = vars
        return self

    def build(self):
        return application(repo=self._repo,context=self._context,optional=self._another_optional_thing,config=self._config)
         
    def with_this_repo(self,repo):
        self._repo=repo 
        return self

    def with_optional(self,optional:str):
        self._another_optional_thing = optional 
        return self
    

class ImpBuilder2(APPBUILDER):
    # Builder para app desktop con config en file 

    def __init__(self):
        super().__init__()
        self._repo = repo1() #si el cliente no indica uno diferente, se usara este
        self._another_optional_thing:str = None 
        self._context = "DESKTOP"
        self._config = None
         
    def with_config(self,config_path:str=None):
        # config_from_toml= toml(config_path)
        config_from_toml = {
            "database":"mysql",
            "restart_service":True
        }
        self._config =config_from_toml
        return self
         
    def with_this_repo(self,repo):
        self._repo=repo 
        return self


    def with_optional(self,optional:str):
        self._another_optional_thing = optional 
        return self
    
    def build(self):
        return application(repo=self._repo,context=self._context,optional=self._another_optional_thing,config=self._config)
         

# Se puede obtener un orden de construccion con un Director

# Seria una especie de factory?
# Puedo pasarle valores desde consumer?

#NOTE: Lo ideal seria instanciar diferentes TIPOS de objeto entre builders, por ejemplo AppMobile() y AppDesktop() sin embargo no lo incorporo al ejemplo para hacerlo rapido

class AppBuildDirector:
    def __init__(self):
        super().__init__()
        self._repo = repo2() 
        self._another_optional_thing:str = None 
        self._context = "DESKTOP"
        self._config = None

    def build_desktop_app(self,builder:APPBUILDER):
        """
        builder de apps desktop 
        usa repo 2
        """
        return builder.with_config(config_path="/this/path/file.toml").with_this_repo(self._repo).build()
        

    def build_mobile_app(self,builder:APPBUILDER):
        """
        builder de apps desktop 
        usa repo 1 
        usa another optional thing
        """
        return builder.with_config(var_name="this").with_optional("hola").build()



