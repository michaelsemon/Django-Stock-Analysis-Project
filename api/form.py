from django import forms

class SymbolLookUp(forms.Form):
    symbol_input = forms.CharField(max_length=5)
