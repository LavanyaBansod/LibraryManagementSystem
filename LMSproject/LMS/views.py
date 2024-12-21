from django.shortcuts import render, redirect, get_object_or_404
from .models import Member
from .forms import MemberForm, UpdateMemberForm
from django.http import HttpResponse
from django.contrib import messages

def home(request):
    return render(request, 'index.html')

def list_members(request):
    members = Member.objects.all()  # Retrieve all members
    return render(request, 'library/list_members.html', {'members': members})

def create_member(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_members')
    else:
        form = MemberForm()
    return render(request, 'library/create_member.html', {'form': form})

def delete_member(request, member_id):
    try:
        # Attempt to retrieve the member
        member = get_object_or_404(Member, membership_no=member_id)
        member.delete()  # Delete the member
        return redirect('list_members')  # Redirect to the member list page
    except Member.DoesNotExist:
        return HttpResponse("Member ID invalid!", status=404)

def update_member(request, member_id):
    # Get the member object to edit (use the Member model)
    member = get_object_or_404(Member, membership_no=member_id)

    # If the request is POST, handle the form submission
    if request.method == 'POST':
        # Get updated values from the form
        address = request.POST.get('address')
        email = request.POST.get('email')
        phone_no = request.POST.get('phone_no')
        account_no = request.POST.get('account_no')

        # Update the member's attributes
        member.address = address
        member.email = email
        member.phone_no = phone_no
        member.account_no = account_no

        # Save the updated member object
        member.save()

        # Show success message
        messages.success(request, f"Member {member.first_name} {member.last_name}'s information updated successfully!")

        # Redirect to the member list page or any other page
        return list_members(request)

    # If GET request, display the current member's information in the form
    return render(request, 'library/update_member.html', {'member': member})
