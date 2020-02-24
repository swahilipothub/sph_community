import csv
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import Http404
from .models import Contact, Group
from .forms import ContactForm, GroupForm, UploadFileForm


@login_required
def contact_list(request):
    contacts = Contact.objects.filter(user=request.user).order_by('-created')
    return render(request, 'contacts/contacts.html', {'contacts': contacts})

@login_required
def contact_count(request):
    contact_count = Contact.objects.filter(user=request.user).count()
    return render(request, 'contacts/contact_count.html',
                  {'contact_count': contact_count})

@login_required
def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.user, request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            if Contact.objects.filter(user=request.user,
                                      mobile=form.cleaned_data['mobile']).exists():
                messages.error(request, "Contact with that phone number Already Exists")
            else:
                contact.save()
                form.save_m2m()
                messages.success(request, "Contact Successfully Created")
                return redirect('contact_create')
    else:
        form = ContactForm(request.user)
    return render(request, "contacts/contact_create.html", {"form": form})

@login_required
def contact_detail(request, pk, template='contacts/contact_detail.html'):
    try:
        contact_detail = Contact.objects.get(pk__iexact=pk)
    except Contact.DoesNotExist:
        raise Http404("Contact does not exists.")

    kwvars = {
        'object': contact_detail,
    }
    return render(request, template, kwvars)

@login_required
def contact_update(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.user, request.POST, instance=contact)
        if form.is_valid():
            contact_update = form.save(commit=False)
            contact_update.user = request.user
            contact_update.save()
            messages.success(request, "Contact Successfully Updated")
    else:
        form = ContactForm(request.user, instance=contact)
    return render(request, 'contacts/contact_update.html', {'form': form})

@login_required
def contact_delete(request, pk, template_name='contacts/confirm_contact_delete.html'):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        messages.success(request, "Contact Successfully Deleted")
        return redirect('contact_list')
    return render(request, template_name, {'object': contact})

@login_required
def group_list(request):
    groups = Group.objects.filter(
        user=request.user).order_by('-created')
    return render(request, 'contacts/group_list.html', {'groups': groups})

@login_required
def group_count(request):
    group_count = Group.objects.filter(user=request.user).count()
    return render(request, 'contacts/group_count.html',
                  {'group_count': group_count})

@login_required
def group_create(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.user = request.user
            if Group.objects.filter(
                    user=request.user, name=form.cleaned_data['name']).exists():
                messages.error(request, "Contact with that phone number Already Exists")
            else:
                group.save()
                form = GroupForm()
                messages.success(request, "Group Successfully Created")
    else:
        form = GroupForm()
    return render(request, 'contacts/group_create.html', {'form': form})

@login_required
def group_update(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            group_update = form.save(commit=False)
            group_update.user = request.user
            group_update.save()
            messages.success(request, "Group Successfully Updated")
    else:
        form = GroupForm(instance=group)
    return render(request, 'contacts/group_update.html', {'form': form})


@login_required
def group_delete(request, pk, template_name='contacts/confirm_group_delete.html'):
    group = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        group.delete()
        messages.success(request, "Group Successfully Deleted")
        return redirect('group_list')
    return render(request, template_name, {'object': group})

@login_required
def export_contact_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="contacts.csv"'
    writer = csv.writer(response)
    writer.writerow(
        ['full_name', 'mobile',])
    contacts = Contact.objects.filter(user=request.user).values_list(
        'full_name', 'mobile',)
    for contact in contacts:
        writer.writerow(contact)
    return response