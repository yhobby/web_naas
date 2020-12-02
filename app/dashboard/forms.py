from django import forms


class BtsForm(forms.Form):
    bts = forms.CharField()
    interface = forms.CharField()
    vlans = forms.CharField()
    ip_abis = forms.CharField()
    ip_iub = forms.CharField()
    ip_om = forms.CharField()
    ip_relay1 = forms.CharField()
    ip_relay2 = forms.CharField()
    giaddr = forms.CharField()
    ip_s1c = forms.CharField()
    ip_s1u = forms.CharField()
    ip_x2 = forms.CharField()


# class BtsResultForm(forms.Form):
#     bts_config_result = forms.CharField(widget=forms.Textarea)