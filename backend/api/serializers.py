from .models import Cdr
from rest_framework import serializers

class CdrSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cdr
        fields=(
            'outbound_cid',
            'src',
            'dst',
            'diversion',
            'channel',
            'dst_channel',
            'start',
            'answer',
            'end',
            'duration',
            'billsec',
            'disposition',
            'uniquie_id',
            'pbx',
            'billsec',
            'recpath',
            )