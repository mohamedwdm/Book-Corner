from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Signup 
from .models import books
from .models import borrowedbooks
from django.contrib import messages

from django.contrib.auth import authenticate , login
from django.db.models import Q
from django.core import serializers



def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        email = request.POST.get('email')
        role = request.POST.get('role')
        
        if   not password or not email or not role or not cpassword :
            return HttpResponse("comblete the data.", status=400)

        # Check if passwords match
        if password != cpassword:
            return HttpResponse("Passwords do not match.", status=400)
        
        # Check if username or email already exists
        existing_user = Signup.objects.filter(
            Q(username=username) |
            Q(email=email)
        ).exists()

        if existing_user:
            return HttpResponse("Username or email already exists.", status=400)
        
        # Check if role is valid
        if role not in ['admin', 'user']:
            return HttpResponse("The role must be 'admin' or 'user'.", status=400)

        # Create and save Signup object
        data = Signup(username=username, password=password, cpassword=cpassword, email=email, role=role)
        data.save()
        
        return redirect('index.html')
    else:
        return render(request, 'pages/signup.html')






def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        check = False
        users = Signup.objects.all()
        for x in users:
            if x.username == username and x.password == password:
                if x.role == 'admin':
                  return redirect('adminlist.html')
                else:
                    return redirect('userList.html')


       
        # if check is True:
        #     return redirect('adminlist.html')
        

        else:
            return HttpResponse("username or password not correct")
        

  
    return render(request, 'pages/index.html')


def adminlist(request):

    book = {'book':books.objects.all()}
    return render(request, 'pages/adminlist.html' , book)


def userList(request):
    book = {'book':books.objects.all()}
    return render(request, 'pages/userList.html' , book)



    

def adminAdd(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        book_name = request.POST.get('book_name')
        book_author = request.POST.get('book_author')
        book_category = request.POST.get('book_category')
        
        # Check if a book with the same details already exists
        existing_book = books.objects.filter(
           Q(book_id=book_id)
        #    ( Q(book_name=book_name) &
        #     Q(book_author=book_author) &
        #     Q(book_category=book_category))
        ).exists()

        if existing_book:
            return HttpResponse("the book id is already exist", status=400)
            

        # If the book doesn't exist, save it
        data = books.objects.create(
            book_id=book_id,
            book_name=book_name,
            book_author=book_author,
            book_category=book_category
        )
        data.save()
        return redirect('adminlist.html')
        
    else:
        return render(request, 'pages/adminAdd.html')

def adminEdit(request, book_id):
    book = books.objects.get(id=book_id)
    if request.method == 'POST':
        book.book_id = request.POST.get('book_id')
        book.book_name = request.POST.get('book_name')
        book.book_author = request.POST.get('book_author')
        book.book_category = request.POST.get('book_category')
        
        
        # Check if password is provided
        if   not book.book_id and not book.book_name and not book.book_author  :
            return HttpResponse("comblete the data.", status=400)
        

        # Create and save Signup object
        book.save()
        return redirect('/adminlist.html')
    
    
    context = {'book': book}
    return render(request, 'pages/adminEdit.html', context)




def borrowedBooks(request  ):

    borrowbook = {'book':borrowedbooks.objects.all()}
    return render(request, 'pages/borrowedBooks.html' , borrowbook)


def deletebook(request, pk):
    book = books.objects.filter(id=pk)
    book.delete()
    messages.success(request , 'Book deleted successfully')
    return redirect('/adminlist.html')


def borrowebook(request, book_id):
    # Get the book object
    book = books.objects.get(id=book_id)
    
    # Check if the user has already borrowed the book
    existing_borrowed_book = borrowedbooks.objects.filter(
        book_id=book.book_id
    ).exists()

    # If the book is already borrowed, redirect with a message
    if existing_borrowed_book:
        
        return HttpResponse("You have already borrowed this book.", status=400)

   

    # If the book is not already borrowed, proceed to borrow it
    data = borrowedbooks(book_id=book.book_id, book_name=book.book_name, book_author=book.book_author, book_category=book.book_category)
    data.save()
    return redirect('/userList.html')


# search bar for admin list with ajax


def ajax_view(request):
 if request.method == 'POST':
    my_input = request.POST.get('search')
        
    mybooks = books.objects.filter(Q(book_name__contains=my_input))

        
    response_data ={
        'message': 'Success',
        'input_value': serializers.serialize('json',mybooks)

    }
    return JsonResponse(response_data, safe=False)


# search bar for user list with ajax

def ajax_view_foruser(request):
 if request.method == 'POST':
    my_input = request.POST.get('bsearch')
        
    mybooks = books.objects.filter(Q(book_name__contains=my_input))

        
    response_data ={
        'message': 'Success',
        'input_value': serializers.serialize('json',mybooks)

    }
    return JsonResponse(response_data, safe=False)


# search bar for borrowed books list with ajax


def ajax_view_forBorrowed(request):
 if request.method == 'POST':
    my_input = request.POST.get('bsearch')
        
    mybooks = borrowedbooks.objects.filter(Q(book_name__contains=my_input))

        
    response_data ={
        'message': 'Success',
        'input_value': serializers.serialize('json',mybooks)

    }
    return JsonResponse(response_data, safe=False)
# def adminAdd(request):
    
#     if request.method == 'POST':
#         book_id = request.POST.get('book_id')
#         book_name = request.POST.get('book_name')
#         book_author = request.POST.get('book_author')
#         book_category = request.POST.get('book_category')
        
        
#         # Check if password is provided
#         if   not book_id and not book_name and not book_author  :
#             return HttpResponse("comblete the data.", status=400)
        



#         # Create and save Signup object
#         data = books(book_id = book_id, book_name = book_name, book_author = book_author, book_category = book_category)
#         data.save()
#         return redirect('adminlist.html')
    
    
    
#     else:
#       return render(request, 'pages/adminAdd.html' )


# def borrowebook(request ,book_id ):
#      borrwbook = books.objects.get(id=book_id)
#      data = borrowedbooks(book_id = borrwbook.book_id, book_name = borrwbook.book_name, book_author = borrwbook.book_author, book_category = borrwbook.book_category)
#      data.save()
#      return redirect('/borrowedBooks.html')

    

# def signup(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         cpassword = request.POST.get('cpassword')
#         email = request.POST.get('email')
#         role = request.POST.get('role')
        
#         # Check if password is provided
#         if   not password or not email or not role or not cpassword :
#             return HttpResponse("comblete the data.", status=400)
        
#         # Check if passwords match
#         if password != cpassword:
#             return HttpResponse("Passwords do not match.", status=400)
        
#         if role != 'admin' and role != 'user':
#             return HttpResponse("the role must be admin or user in lower case", status=400)


#         # Create and save Signup object
#         data = Signup(username=username, password=password, cpassword=cpassword, email=email, role=role)
#         data.save()
        
#         return redirect('index.html')
#     else:
#         return render(request, 'pages/signup.html')