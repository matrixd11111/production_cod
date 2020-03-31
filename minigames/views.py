from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.base import RedirectView
from .settings.loto_game import Ticket, BarrelBag


ticket = Ticket()
barrel = BarrelBag()

def index(request):
    return render(request, 'minigames/index.html')


def lotogame(request):

    if len(ticket.ticket_list) > 4:
        ticket.ticket_list.clear()

    context = {'ticket': ticket, 'barrel': barrel}

    return render(request, 'minigames/loto/lotogame.html', context)


class GameMenuViews(RedirectView):

    pattern_name = 'minigames/loto/lotogame.html'

    def get_redirect_url(self, *args, **kwargs):

        if kwargs.get('menu') == 1:
            ticket.create_ticket()

        if kwargs.get('menu') == 2:
            if len(barrel.barrel_list) == 0:
                barrel.create_barrel()
            else:
                print('Delete barrel')

        if kwargs.get('menu') == 3:
            barrel.barrel_list.clear()
            ticket.ticket_list.clear()

# данное условие временно. Эту ссылку необходимо
# переделать на автоматичесскую в javascript

        if kwargs.get('menu') == 15:
            barrel.get_barrel()

        return super().get_redirect_url(*args, **kwargs)


class ChengeTicketViews(RedirectView):

    pattern_name = 'minigames/loto/lotogame.html'

    def get_redirect_url(self, *args, **kwargs):

        if kwargs.get('pk') in barrel.barrel_pop:
            ticket.cross_it_uot((kwargs.get('ticket')-1),
                                kwargs.get('pk'),)

        return super().get_redirect_url(*args, **kwargs)


def test(request):
    ticket.check_ticket(check_num=barrel.barrel_other)
    barrel.get_barrel()
    return HttpResponseRedirect('/minigame/lotogame')
