from django.urls import path

from . import views


urlpatterns = [
    # HOME
    # ex: /
    path('', views.Index.as_view(), name='index'),
    # ex: /table/*
    path('table/device_info', views.DevicePage.as_view(), name='device-info'),
    path('table/lag_info', views.LagPage.as_view(), name='lag-info'),
    path('table/vrf_info', views.VrfPage.as_view(), name='vrf-info'),
    path('table/vlan_info', views.VlanPage.as_view(), name='vlan-info'),
    path('table/acl_info', views.AclPage.as_view(), name='acl-info'),
    path('table/bgp_info', views.BgpPage.as_view(), name='bgp-info'),
    path('table/boards_info', views.BoardsPage.as_view(), name='boards-info'),
    path('table/ports_info', views.PortsPage.as_view(), name='ports-info'),
    # ex: /script/*
    path('script/send_commands', views.SendCommand.as_view(), name='send-commands'),
    path('script/network_audit', views.NetworkAudit.as_view(), name='network-audit'),
    path('script/scripts_table', views.ScriptsTable.as_view(), name='scripts-table'),
    path('script/new_volume', views.NewVolume.as_view(), name='new-volume'),
    path('script/cron', views.Cron.as_view(), name='cron'),
    # ex: /overview
    path('overview/', views.Overview.as_view(), name='overview'),
    # ex: /feedback
    path('feedback/', views.Feedback.as_view(), name='feedback'),
    # ex: /template/*
    path('template/bts_config', views.BtsConfig.as_view(), name='bts-config'),
]