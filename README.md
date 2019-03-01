# jupyterhub-passthroughauth
Pass-through authentication for jupyterhub, enabling direct access to the session of a particular locked down user.

The plugin (if installed and configured) could disable the standard form-based authentication of jupyterhub and provides direct access to the session from a particular user specified via config.
Think of this as a jupyterhub-singleuser functionality on a standard jupyterhub without the requirement of using tokens or passwords to gain access.
This kind of module is very useful if you like to provide guest access to your jupyterhub from a particular user or continue to use the standard PAM authentication just by flipping a switch in the config

### Installation

* ```pip(3) install jupyterhub-passthroughauth```

### Configuration

* jupyterhub_config.py
```python
c.JupyterHub.authenticator_class = 'passthroughauth.PassThroughAuthenticator'
c.PassThroughAuthenticator.guest_user = 'ubuntu'
c.Authenticator.auto_login = True # Disables PAM login completely, use False otherwise
```

### Access

If the regular path ```/``` is accessed:
* Login page will be displayed if auto_login flag is set to ```False```
* Guest session page will be displayed if auto_login flag is set to ```True```
