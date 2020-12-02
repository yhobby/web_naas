# Network as a Service
Using django + docker + nginx + uwsgi

A shell for running scripts for the subsequent management of the entire network in plans to use its web application as an orchestrator for the network infrastructure, from where it will be possible to manage all switches and routers

The application uses as a backend to the maximum all existing scripts and developments.

Two databases are used, one for the admin panel, the second database for storing information about our existing network, which is filled with existing scripts.

Also, all scripts that are launched directly from the web application are reused from existing developments and are launched via a request in Jenkins

In production:
- running scripts
- generation of configs (Jinja2 templates)
- Database access
- Database visualization
- Access to other Open Source projects

![naas-demo-gif](https://github.com/yhobby/web_naas/blob/master/naas.gif)