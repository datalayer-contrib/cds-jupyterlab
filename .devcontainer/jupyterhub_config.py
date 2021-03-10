c.JupyterHub.authenticator_class = "jupyterhub.auth.DummyAuthenticator"

c.DummyAuthenticator.password = "password"

c.Authenticator.admin_users = {"dan"}
c.DummyAuthenticator.allowed_users = {"dan", "bob"}

c.JupyterHub.spawner_class = (
    "cdsdashboards.hubextension.spawners.VariableLocalProcessSpawner"
)

c.CDSDashboardsConfig.builder_class = (
    "cdsdashboards.builder.processbuilder.ProcessBuilder"
)

c.LocalProcessSpawner.notebook_dir = "/home/{username}"

c.JupyterHub.allow_named_servers = True

from cdsdashboards.app import CDS_TEMPLATE_PATHS
from cdsdashboards.hubextension import cds_extra_handlers

c.JupyterHub.template_paths = CDS_TEMPLATE_PATHS
c.JupyterHub.extra_handlers = cds_extra_handlers

c.Spawner.default_url = "/lab"
c.Spawner.debug = True
