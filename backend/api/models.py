from django.db import models

class Cdr(models.Model):
    outbound_cid = models.fields.CharField(max_length=80,default='',)
    src = models.CharField(max_length=80)
    dst = models.fields.CharField(max_length=80)
    diversion = models.fields.CharField(max_length=64, default='')
    channel = models.fields.CharField(max_length=80)
    dst_channel = models.fields.CharField(max_length=80)
    start = models.fields.DateTimeField()
    answer = models.fields.DateTimeField(null=True)
    end = models.fields.DateTimeField(null=True)
    duration = models.fields.IntegerField(default=0)
    billsec = models.fields.IntegerField(default=0)
    disposition = models.fields.CharField(max_length=80)
    uniquie_id = models.fields.CharField(max_length=80, unique=True)
    pbx = models.fields.CharField(max_length=80, default='')
    recpath = models.CharField(max_length=80, blank=True)

    def to_dict(self):
        return {
            'outbound_cid': self.outbound_cid,
            'src': self.src,
            'dst': self.dst,
            'diversion': self.diversion,
            'channel': self.channel,
            'dst_channel': self.dst_channel,
            'start': self.start,
            'answer': self.answer,
            'end': self.end,
            'duration': self.duration,
            'billsec': self.billsec,
            'disposition': self.disposition,
            'uniquie_id': self.uniquie_id,
            'pbx': self.pbx,
            'recpath': self.recpath,
        }