from django.shortcuts import render
from main.models import StudentStats
from datetime import datetime

# Create your views here.

def clicker(request):
    lastStat = StudentStats.objects.last()
    if lastStat:
        context = {
            'hp': lastStat.hp,
            'iq': lastStat.iq,
            'ha': lastStat.ha
            }
    else:
        context = {
            'hp': 0,
            'iq': 0,
            'ha': 0
            }
    if request.method == 'POST':
        hp = request.POST['hp_hidden']
        iq = request.POST['iq_hidden']
        ha = request.POST['ha_hidden']
        record = StudentStats(hp=hp, iq=iq, ha=ha, date=datetime.now())
        record.save()
    return render(request, 'pages/student.html', context)