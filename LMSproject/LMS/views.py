from django.shortcuts import render, redirect, get_object_or_404
from .models import Member
from .forms import MemberForm
from django.http import HttpResponse

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
        member = get_object_or_404(Member, id=member_id)
        member.delete()  # Delete the member
        return redirect('list_members')  # Redirect to the member list page
    except Member.DoesNotExist:
        return HttpResponse("Member ID invalid!", status=404)
