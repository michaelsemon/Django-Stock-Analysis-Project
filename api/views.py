
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group


import yfinance as yf
import requests
#from pytickersymbols import PyTickerSymbols

from django.conf.urls import url
from django_filters.views import FilterView
from .models import *
from .filters import *
from .form import SymbolLookUp
#from .decorators import unauthenticated_user, allowed_users, admin_only

# Create your views here.

def home(request):

    default_symbol = 'MSFT'
    symbol = yf.Ticker(default_symbol)
    stock_info = symbol.info



    #User input Ticker Sybmol / Filter
    if request.method == 'POST':
        form = SymbolLookUp(request.POST)
        if form.is_valid():
            symbol_input = request.POST.get('symbol_input', None)
            stock_info =  yf.Ticker(symbol_input)
            stock_info = stock_info.info
            return(stock_info)

    #yfinance -- load stock data
        if (symbol_input == ''):
            default_symbol = 'TSLA'
            symbol = yf.Ticker(default_symbol)
            stock_info = symbol.info

        '''
        else:
            symbol = yf.Ticker(symbol_input)
            stock_info = symbol.info
        '''





    context = {'stock_info': stock_info, 'symbol': symbol}
    return render(request, 'home.html', context)
