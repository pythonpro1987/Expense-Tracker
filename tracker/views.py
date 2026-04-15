from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Transaction
from .forms import TransactionForm

class TransactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'dashboard.html'

    def get_queryset(self):
        return Transaction.objects.filter(user = self.request.user)
    

class TransactionCreateView(LoginRequiredMixin, CreateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'add_transaction.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# Create your views here.
