from django.shortcuts import render
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.edit import FormView

from .models import DeviceInfo, AclInfo, PortsInfo, BgpInfo, LagInfo, VlanInfo, VrfInfo, BoardsInfo
from .forms import BtsForm
from .config_generator import generator


# Dashboard Home Page
class Index(LoginRequiredMixin, View):
    template = 'dashboard/index.html'
    login_url = '/login'

    def get(self, request):
        # TYPE PIE CHART
        type_labels = ['Router', 'Switch', 'Firewall']
        type_data = []

        for type in type_labels:
            type_data.append(DeviceInfo.objects.filter(type=f'{type}').count())

        # MODEL BAR CHART
        model_labels = ['NE40E-X8A', 'NE40E-X8', 'CX600-X3', 'ATN950B', 'S6348-EI', 'S6324-EI', 'S5352C-EI',
                        'S5328C-EI', 'S3328TP-EI', 'CE6851-48S6Q-HI', 'CE5855-48T4S2Q-EI', 'AR2220E', 'AR2220']
        model_data = []

        for model in model_labels:
            model_data.append(DeviceInfo.objects.filter(model=f'{model}').count())

        # CITY BAR CHART
        city_labels = ['Almaty', 'Astana', 'Aktobe', 'Shymkent', 'Taraz', 'Kyzylorda', 'Atyrau',
                       'Aktau', 'Uralsk', 'Kokshetau', 'Kostanay', 'Petropavlovsk', 'Karaganda',
                       'Semey', 'Pavlodar', 'Ust-Kamenogorsk']
        city_data = []

        for city in city_labels:
            city_data.append(DeviceInfo.objects.filter(city=f'{city}').count())

        # # APPS AREA CHART
        # apps_labels = ['Jan 1', 'Jan 2', 'Jan 3', 'Jan 4', 'Jan 5', 'Jan 6']
        # apps_data = [1, 2, 3, 4, 5, 6]

        return render(request, self.template, {
            'type_labels': type_labels,
            'type_data': type_data,
            'model_labels': model_labels,
            'model_data': model_data,
            'city_labels': city_labels,
            'city_data': city_data,
            # 'apps_labels': apps_labels,
            # 'apps_data': apps_data,
        })


# Authentication
class Login(View):
    template = 'dashboard/accounts/login.html'

    def get(self, request):
        form = AuthenticationForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return render(request, self.template, {'form': form})


# Scripts Pages
class SendCommand(LoginRequiredMixin, PermissionRequiredMixin, FormView):
    permission_required = 'memos.can_change_memo'
    model = Memo
    template = 'dashboard/scripts/send_commands.html'
    login_url = '/login'

    def get(self, request):
        return render(request, self.template)


class NetworkAudit(LoginRequiredMixin, View):
    template = 'dashboard/scripts/network_audit.html'
    login_url = '/login'

    def get(self, request):
        return render(request, self.template)


class ScriptsTable(LoginRequiredMixin, View):
    template = 'dashboard/scripts/scripts_table.html'
    login_url = '/login'

    def get(self, request):
        return render(request, self.template)


class NewVolume(LoginRequiredMixin, View):
    template = 'dashboard/scripts/new_volume.html'
    login_url = '/login'

    def get(self, request):
        return render(request, self.template)


class Cron(LoginRequiredMixin, View):
    template = 'dashboard/scripts/cron.html'
    login_url = '/login'

    def get(self, request):
        return render(request, self.template)


# Database tables
class DevicePage(LoginRequiredMixin, View):
    template = 'dashboard/tables/device-info.html'
    login_url = '/login'

    def get(self, request):
        devices = DeviceInfo.objects.all()
        return render(request, self.template, {'devices': devices})


class AclPage(LoginRequiredMixin, View):
    template = 'dashboard/tables/acl-info.html'
    login_url = '/login'

    def get(self, request):
        acls = AclInfo.objects.all()
        return render(request, self.template, {'acls': acls})


class BgpPage(LoginRequiredMixin, View):
    template = 'dashboard/tables/bgp-info.html'
    login_url = '/login'

    def get(self, request):
        bgps = BgpInfo.objects.all()
        return render(request, self.template, {'bgps': bgps})


class BoardsPage(LoginRequiredMixin, View):
    template = 'dashboard/tables/boards-info.html'
    login_url = '/login'

    def get(self, request):
        boards = BoardsInfo.objects.all()
        return render(request, self.template, {'boards': boards})


class LagPage(LoginRequiredMixin, View):
    template = 'dashboard/tables/lag-info.html'
    login_url = '/login'

    def get(self, request):
        lags = LagInfo.objects.all()
        return render(request, self.template, {'lags': lags})


class PortsPage(LoginRequiredMixin, View):
    template = 'dashboard/tables/ports-info.html'
    login_url = '/login'

    def get(self, request):
        ports = PortsInfo.objects.all()
        return render(request, self.template, {'ports': ports})


class VrfPage(LoginRequiredMixin, View):
    template = 'dashboard/tables/vrf-info.html'
    login_url = '/login'

    def get(self, request):
        vrfs = VrfInfo.objects.all()
        return render(request, self.template, {'vrfs': vrfs})


class VlanPage(LoginRequiredMixin, View):
    template = 'dashboard/tables/vlan-info.html'
    login_url = '/login'

    def get(self, request):
        vlans = VlanInfo.objects.all()
        return render(request, self.template, {'vlans': vlans})


# Overview
class Overview(LoginRequiredMixin, View):
    template = 'dashboard/overview.html'
    login_url = '/login'

    def get(self, request):
        return render(request, self.template)


# Feedback
class Feedback(LoginRequiredMixin, View):
    template = 'dashboard/feedback.html'
    login_url = '/login'

    def get(self, request):
        return render(request, self.template)


# Page 404
def handler404(request, exception):
    return render(request, 'dashboard/404.html')


# Config config_templates
class BtsConfig(LoginRequiredMixin, View):
    template = 'dashboard/config_templates/bts-config.html'
    template_with_result = 'dashboard/config_templates/bts-config-result.html'
    login_url = '/login'
    initial = {'key': 'value'}
    form_class = BtsForm

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            bts = form.cleaned_data['bts']
            interface = form.cleaned_data['interface']
            vlans = form.cleaned_data['vlans']
            ip_abis = form.cleaned_data['ip_abis']
            ip_iub = form.cleaned_data['ip_iub']
            ip_om = form.cleaned_data['ip_om']
            ip_relay1 = form.cleaned_data['ip_relay1']
            ip_relay2 = form.cleaned_data['ip_relay2']
            giaddr = form.cleaned_data['giaddr']
            ip_s1c = form.cleaned_data['ip_s1c']
            ip_s1u = form.cleaned_data['ip_s1u']
            ip_x2 = form.cleaned_data['ip_x2']

            # process the data in form.cleaned_data as required
            vlan_abis, vlan_iub, vlan_om, vlan_s1c, vlan_s1u, vlan_x2 = vlans.split()
            data = {
                'bts': bts,
                'interface': interface,
                'vlan_abis': vlan_abis,
                'vlan_iub':vlan_iub,
                'vlan_om': vlan_om,
                'vlan_s1c': vlan_s1c,
                'vlan_s1u': vlan_s1u,
                'vlan_x2': vlan_x2,
                'ip_abis': ip_abis,
                'ip_iub': ip_iub,
                'ip_om': ip_om,
                'ip_relay1': ip_relay1,
                'ip_relay2': ip_relay2,
                'giaddr': giaddr,
                'ip_s1c': ip_s1c,
                'ip_s1u': ip_s1u,
                'ip_x2': ip_x2
            }

            result = generator('bts_config.txt', data)

            # redirect to a new URL:
            return render(request, self.template_with_result, {'result': result})

        return render(request, self.template, {'form': form})