from django.contrib import messages
from core.models import *
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import PermissionRequiredMixin,LoginRequiredMixin
from django.views.generic import CreateView, ListView,TemplateView,UpdateView, DeleteView,DetailView
from django.urls import reverse_lazy
from ..models import Book, BookImage
from ..form import BookForm, BookImageForm,BookImageFormSet
from django.db import transaction
from core.form import CustomUserCreationForm
from django.contrib.auth.mixins import PermissionRequiredMixin,LoginRequiredMixin
from ..form import ProfileUpdateForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from core.utility.send_email import *
from ..form import AddressForm


class CustomPermissionMixin(PermissionRequiredMixin):
    def has_permission(self):
        if super().has_permission():
            return True
        # Check individual user permissions
        user_permissions = self.request.user.get_all_permissions()
        try:
            if self.permission_required in user_permissions:
                return True

            user_groups = self.request.user.groups.all()
            for group in user_groups:
                if self.request.user.has_perm(self.permission_required, group=group):
                    return True
        except:
            pass
        return False
    
    def handle_no_permission(self):
        """
        Handles the case when the user doesn't have permission to access the view.
        """
        return HttpResponseForbidden(self.permission_denied_message)


class UserRegisterView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login_user')
    template_name = 'core/register.html'
    
    def form_valid(self, form):
        messages.success(self.request, "Your account has been created successfully")
        return super().form_valid(form)

class DashboardView(TemplateView):
    template_name = 'home.html'
    context_object_name = 'feedbacks'
    success_url = 'dashboard'

    def get_context_data(self, **kwargs):
        gallery = MediaGallery.objects.all()
        context = super().get_context_data(**kwargs)
        context['medias'] = gallery
        return context
    

    def get_success_url(self):
        return self.success_url


class ProductListView(TemplateView):
    template_name = 'core/product_list.html'
    paginate_by = 20  # Number of items per page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_permissions = self.request.user.get_all_permissions()
        context['user_permissions'] = user_permissions

        search_term = self.request.GET.get('search', '')

        if search_term:
            books = Book.objects.filter(
                Q(title__icontains=search_term) |
                Q(author__name__icontains=search_term) |
                Q(publisher__name__icontains=search_term) |
                Q(category__name__icontains=search_term) |
                Q(description__icontains=search_term)
            )
        else:
            books = Book.objects.all()

        # Get the books list with images
        book_list = []
        for book in books:
            book_image = BookImage.objects.filter(book=book).first()
            book_dict = {
                'book': book,
                'image': book_image
            }
            book_list.append(book_dict)

        paginator = Paginator(book_list, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            books_paginated = paginator.page(page)
        except PageNotAnInteger:
            books_paginated = paginator.page(1)
        except EmptyPage:
            books_paginated = paginator.page(paginator.num_pages)

        context['books'] = books_paginated
        context['search_term'] = search_term
        return context


class BookListView(LoginRequiredMixin,TemplateView):
    template_name = 'bookadmin/book_lists.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_permissions = self.request.user.get_all_permissions()
        context['user_permissions'] = user_permissions
        books = self.get_books_list()
        context['books'] = books
        return context
    
    def get_books_list(self):
        book_list =[]
        books = Book.objects.all()
        for book in books:
            book_image = BookImage.objects.filter(book=book).first()
            book_dict = {
                'book':book,
                'image':book_image
            }
            book_list.append(book_dict)
        return book_list

class OrderListView(LoginRequiredMixin,CustomPermissionMixin,ListView):
    template_name = 'bookadmin/orders_recieved.html'
    model = Order
    context_object_name = 'orders'
    permission_required = ['core.view_orders']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url'] = reverse_lazy('order_list')
        return context


class OrderDetailsView(LoginRequiredMixin,DetailView):
    template_name = 'core/order_details.html'
    model = Order
    context_object_name = 'order'


class MyOrderListView(LoginRequiredMixin,ListView):
    template_name = 'bookadmin/orders_recieved.html'
    model = Order
    context_object_name = 'orders'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url'] = reverse_lazy('my_order_list')
        return context

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


from django.views.generic.detail import DetailView

class BookDetailView(DetailView):
    model = Book
    template_name = 'core/book_detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.get_object()
        book_images = BookImage.objects.filter(book=book)
        context['book_images'] = book_images
        context['related_books'] = self.get_related_book()
        return context
    
    def get_related_book(self):
        book_list =[]
        books = Book.objects.all()[:5]
        for book in books:
            book_image = BookImage.objects.filter(book=book).first()
            book_dict = {
                'book':book,
                'image':book_image
            }
            book_list.append(book_dict)
        return book_list

class BookCreateView(LoginRequiredMixin, CustomPermissionMixin,CreateView):
    model = Book
    form_class = BookForm
    template_name = 'bookadmin/book_form.html'
    success_url = reverse_lazy('book_list')  # assuming you have a URL named 'book_list' for listing books
    permission_required = 'core.add_book'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['image_formset'] = BookImageFormSet(self.request.POST, self.request.FILES)
        else:
            context['image_formset'] = BookImageFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        image_formset = context['image_formset']
        with transaction.atomic():
            self.object = form.save()
            if image_formset.is_valid():
                image_formset.instance = self.object
                image_formset.save()
        return super().form_valid(form)

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

@login_required
def add_to_cart_view(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        quantity = request.POST.get('quantity')
        # Retrieve the book from the database
        try:
            book = Book.objects.get(id=book_id)
            added = book.add_to_cart(user=request.user,quantity=quantity)
            if added:
                book.save()
            else:
                messages.error(request, 'Book quantity not available')
                return redirect(request.META.get('HTTP_REFERER'))
        except Book.DoesNotExist:
            messages.error(request, 'Book does not exists')
            return redirect(request.META.get('HTTP_REFERER'))
        messages.success(request, 'Book added to the cart')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect(request.META.get('HTTP_REFERER'))

@login_required
def remove_from_cart_view(request):
    if request.method == 'POST':
        # Retrieve book ID and quantity from request data
        book_id = request.POST.get('book_id')
        # Retrieve the book from the database
        try:
            book = Book.objects.get(id=book_id)
            book.remove_from_cart(user=request.user)
        except Book.DoesNotExist:
            return JsonResponse({'error': 'Book not found'}, status=404)
        messages.success(request, "Item removed from cart")
        return redirect(request.META.get('HTTP_REFERER'))

    return redirect(request.META.get('HTTP_REFERER'))


class BookUpdateView(LoginRequiredMixin, CustomPermissionMixin,UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'bookadmin/book_form.html'  # Your template name

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['form'] = BookForm(self.request.POST, instance=self.object)
            context['formset'] = BookImageFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            context['form'] = BookForm(instance=self.object)
            context['formset'] = BookImageFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        form = context['form']
        formset = context['formset']
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse_lazy('book_detail', kwargs={'pk': self.object.pk})  # Redirect to book detail page after updating


class UserCartView(LoginRequiredMixin,TemplateView):
    template_name = 'core/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_permissions = self.request.user.get_all_permissions()
        context['user_permissions'] = user_permissions
        return context


def place_order(request):
    if request.method == 'POST':
        address_id = request.POST.get('address_id')
        payment_method_id = request.POST.get('payment_method_id')
        comments = request.POST.get('comments')
        cart_items = CartItem.objects.filter(user=request.user)
        order = Order.objects.create(user = request.user,address_id=address_id,payment_method_id=payment_method_id,order_comment = comments)
        for item in cart_items:
            OrderItem.objects.create(order=order,book=item.book,quantity=item.quantity)
        messages.success(request,"Your order has been placed successfully")
        cart_items.all().delete()
        try:
            send_order_placed_email(user=request.user,order=order)
        except Exception as e:
            messages.error(request,"Failed to send email. Please check your email")
        return redirect(reverse('order_success'))
    return redirect(reverse_lazy('order_success'))


class OrderSuccessView(LoginRequiredMixin,TemplateView):
    template_name = 'core/order_success.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_permissions = self.request.user.get_all_permissions()
        context['user_permissions'] = user_permissions
        return context
    
class UserCheckoutView(LoginRequiredMixin,TemplateView):
    template_name = 'core/checkout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        payment_method = PaymentMethod.objects.all()
        context['payment_method'] = payment_method
        context['form'] = AddressForm
        return context
    
class AddressListView(LoginRequiredMixin, ListView):
    model = Address
    template_name = 'core/address_list.html'
    context_object_name = 'addresses'

    def get_queryset(self):
        # Retrieve addresses specific to the logged-in user
        return Address.objects.filter(user=self.request.user)


class AddressDetailView(LoginRequiredMixin,DetailView):
    model = Address
    template_name = 'core/address_detail.html'
    context_object_name = 'address'


class AddressCreateView(LoginRequiredMixin, CreateView):
    model = Address
    form_class = AddressForm    
    template_name = 'core/address_form.html'
    success_url = reverse_lazy('address_list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text_label'] = 'Add Address'
        return context
    
    def get_success_url(self):
        return self.get_redirect_url() or self.success_url
    
    def get_redirect_url(self):
        return self.request.GET.get('next', '')
    
class AddressUpdateView(LoginRequiredMixin,UpdateView):
    model = Address
    form_class = AddressForm
    template_name = 'core/address_form.html'
    success_url = reverse_lazy('address_list')
    
    def get_queryset(self):
        # Get the queryset for the model
        queryset = super().get_queryset()
        # Filter the queryset to get only the addresses associated with the logged-in user
        return queryset.filter(user=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text_label'] = 'Update Address'
        return context

class AddressDeleteView(LoginRequiredMixin,DeleteView):
    model = Address
    template_name = 'confirm_delete.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('address_list')


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = 'core/profile_form.html'
    form_class = ProfileUpdateForm
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user.user_profile
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text_label'] = 'Update Profile'
        return context

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        user = self.request.user
        form.initial.update({
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
        })
        return form
        
    def form_valid(self, form):
        profile = form.save(commit=False)
        user = self.request.user
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.email = form.cleaned_data['email']
        user.save()
        profile.save()
        return super().form_valid(form)


def media_gallery(request):
    media_items = MediaGallery.objects.all()
    return render(request, 'gallery.html', {'media_items': media_items})
