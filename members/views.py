from django.shortcuts import render


def member_list_view_handler(request):
    return render(request, "screens/member_list.html")
