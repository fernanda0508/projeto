from django.contrib import admin
from projeto_saas.models import Sensor, Topicos, Wifi, Mqtt, Placa


# Opcional: Personalizar a aparência no admin
class SensorAdmin(admin.ModelAdmin):
    list_display = ("tipo", "pino_gpio", "intervalo_leitura", "placa")
    list_filter = ("tipo", "placa")
    search_fields = ("tipo",)


class TopicosAdmin(admin.ModelAdmin):
    list_display = ("topico", "mqtt")
    list_filter = ("mqtt",)
    search_fields = ("topico",)


class WifiAdmin(admin.ModelAdmin):
    list_display = ("ssid", "senha")
    search_fields = ("ssid",)


class MqttAdmin(admin.ModelAdmin):
    list_display = ("host", "porta", "usuario")
    list_filter = ("usuario",)
    search_fields = ("host",)


class PlacaAdmin(admin.ModelAdmin):
    list_display = ("modelo", "wifi", "mqtt")
    list_filter = ("modelo",)
    search_fields = ("modelo",)


# Registrar modelos com a personalização, se houver
admin.site.register(Sensor, SensorAdmin)
admin.site.register(Topicos, TopicosAdmin)
admin.site.register(Wifi, WifiAdmin)
admin.site.register(Mqtt, MqttAdmin)
admin.site.register(Placa, PlacaAdmin)
