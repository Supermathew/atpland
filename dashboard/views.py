from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import Account,UserProfile
from django.contrib import messages, auth
from django.contrib.auth import update_session_auth_hash
from django.utils.text import slugify
from propertystore.models import Product
from category.models import Category
from .models import  Messagemodel
import os

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator




# Create your views here.



@login_required(login_url = 'login')
def dashboard(request):
    user = request.user
    context = {
        'user':user,
    }
    return render(request, 'dashboard/uploadpropertyy.html',context)


def upload(request):
    if request.method == 'POST':
        owner_type = request.POST.get('owner_type')
        property_name = request.POST.get('property_name')
        property_cents = request.POST.get('property_cents')
        property_sq_feet = request.POST.get('property_sq_feet')
        water_avl = request.POST.get('water_avl')
        Trans_avl = request.POST.get('Trans_avl')
        prop_add = request.POST.get('prop_add')
        price = request.POST.get('price')
        token_amount = request.POST.get('token_amount')
        property_discription = request.POST.get('property_discription')
        video_url = request.POST.get('video_url')
        videofile = request.FILES.get('pro_video')
        pro_image = request.FILES.get('pro_image')
        pro_image1 = request.FILES.get('pro_image1')
        pro_image2 = request.FILES.get('pro_image2')
        pro_image3 = request.FILES.get('pro_image3')
        pincode = request.POST.get('pincode')
        district = request.POST.get('district')
        phonenumber = request.POST.get('phone_number')

        property_cents = round(float(property_cents))
        property_sq_feet = round(float(property_sq_feet))
        # price = round(float(price))
        # token_amount = round(float(token_amount))
        # phonenumber = round(float(phonenumber))
        # pincode = round(float(pincode))


        if phonenumber is not None :
            number_str = str(phonenumber)
            if len(number_str)<10:
                messages.error(request,"phone number cannot be less that 10 digit")
                return redirect('upload')
        
        try:
          ans = Product.objects.get(property_name=property_name)
        except Product.DoesNotExist:
          ans = None
        if ans is not None:
           messages.error(request, "property with this name already exist")
           return redirect('upload')
        # Convert the title to a slug
        slug = slugify(property_name)

        category = request.POST.get('pro_cat')
        try:
         cat = Category.objects.get(category_name=category)
        except Category.DoesNotExist:
         cat = None   
        print("mathew")
        print(category)
        catslug = slugify(category)
        print(catslug)
        print(cat)
        if cat is None:
           cat = Category(category_name=category,slug=catslug)
           cat.save()

          
        user=request.user

        if videofile.name and videofile.name.endswith('.mp4') or uploaded_file.name.endswith('.avi') or uploaded_file.name.endswith('.mov'):
           new_instance = Product(property_name=property_name,category=cat,propertyowner=user,slug=slug,owner_type=owner_type, description=property_discription, property_cent=property_cents, property_squarefeet=property_sq_feet,property_Water_Availability=water_avl,property_transpaortation=Trans_avl,property_address=prop_add,price=price,tocken_amount=token_amount,video_url=video_url,video=videofile,images1=pro_image,images2=pro_image1,images3=pro_image2,images4=pro_image3,property_pincode=pincode,phonenumber=phonenumber,district=district)
           new_instance.save()
           messages.success(request, 'Property uploaded Successfully !! It will be visible To all User After Admin Approval')
        else:
            # Return an error message if the uploaded file is not a video file
            return HttpResponse('Please upload a video file.')

    return render(request, 'dashboard/uploadpropertyy.html')


        
        # Create a new instance of the model and save it to the database
        
def message(request):
    messagefrombuyerr = Messagemodel.objects.filter(seller=request.user)
    paginator = Paginator(messagefrombuyerr,1)
    page=request.GET.get('pg')
    messagefrombuyer = paginator.get_page(page)
    context = {
        'messagefrombuyer':messagefrombuyer,
    }
    return render(request, 'dashboard/buyermessage.html',context)


def Yourproperty(request):
    userpropertyy = Product.objects.filter(propertyowner=request.user)
    paginator = Paginator(userpropertyy,6)
    page=request.GET.get('pg')
    userproperty = paginator.get_page(page)
    context = {
        'userproperty':userproperty,
    }
    return render(request, 'dashboard/userproperty.html',context)

def wishlist(request):
    userwishlistt = Messagemodel.objects.filter(buyer=request.user)
    paginator = Paginator(userwishlistt,1)
    page=request.GET.get('pg')
    userwishlist = paginator.get_page(page)
    context = {
        'userwishlist':userwishlist,
    }
    return render(request, 'dashboard/userwishlistpropertyy.html',context)

def editproperty(request,pk):
    pro = Product.objects.get(id=pk)


    pass 
    return render(request, 'dashboard/userpropertyy.html',context)


def property_delete(request,product_slug):
    pro = Product.objects.get(slug=product_slug)
    pro.delete()
    messages.success(request, "Property deleted successfully")
    return redirect('Yourproperty')



def property_update(request,product_slug):
    try:
        if request.method == 'POST': 
            owner_type = request.POST.get('owner_type')
            property_name = request.POST.get('property_name')
            property_cents = request.POST.get('property_cents')
            property_sq_feet = request.POST.get('property_sq_feet')
            water_avl = request.POST.get('water_avl')
            Trans_avl = request.POST.get('Trans_avl')
            prop_add = request.POST.get('prop_add')
            price = request.POST.get('price')
            token_amount = request.POST.get('token_amount')
            property_discription = request.POST.get('property_discription')
            video_url = request.POST.get('video_url')
            videofile = request.FILES.get('pro_video')
            pro_image = request.FILES.get('pro_image')
            pro_image1 = request.FILES.get('pro_image1')
            pro_image2 = request.FILES.get('pro_image2')
            pro_image3 = request.FILES.get('pro_image3')
            pincode = request.POST.get('pincode')
            district = request.POST.get('district')
            phonenumber = request.POST.get('phone_number')
            print(phonenumber)
            try:
              ans = Product.objects.exclude(slug=product_slug).get(property_name=property_name)
            except Product.DoesNotExist:
                ans=None 
                print(ans)
            
            if phonenumber is not None :
               if len(phonenumber)<10:
                   messages.error(request,"phone number cannot be less that 10 digit")
                   return redirect('Yourproperty')
                   
            if ans is not None:
                messages.error(request, "property with this name already exist")
                return redirect('Yourproperty')

            
            else:
                
                single_product = Product.objects.get(slug = product_slug)
                print("mathewwwwww")
                if len(request.FILES) != 0:
                   print("mathew")
                   if len(single_product.images1)!=0 and pro_image:
                       print("mathew")
                       os.remove(single_product.images1.path)
                       single_product.images1 = pro_image
                   if single_product.images2 and pro_image1:
                      os.remove(single_product.images2.path)
                      print("mathe")
                      single_product.images2 = pro_image1
                   if single_product.images3 and pro_image2:
                      os.remove(single_product.images3.path)
                      single_product.images3 = pro_image2
                   if single_product.images4 and pro_image3:
                      os.remove(single_product.images4.path)
                      single_product.images4 = pro_image3
                   if single_product.video and videofile:
                      os.remove(asingle_product.video.path)
                      single_product.video = videofile
                single_product.owner_type = owner_type
                single_product.property_name = property_name
                single_product.property_cents = property_cents
                single_product.property_squarefeet = property_sq_feet
                single_product.property_Water_Availability= water_avl
                single_product.property_transpaortation = Trans_avl
                single_product.property_address = prop_add
                single_product.price = price
                single_product.token_amount = token_amount
                single_product.description = property_discription
                single_product.video_url = video_url
                single_product.property_pincode = pincode
                single_product.district = district
                single_product.phonenumber = phonenumber

                slug = slugify(property_name)

                category = request.POST.get('pro_cat')
                cat = Category.objects.get(category_name=category)
                single_product.category = cat
                single_product.save()
                messages.success(request, 'Property updated successfully.')
    except Exception as e:
        raise e
    return redirect('Yourproperty')







@login_required(login_url = 'login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'You are logged out.')
    return redirect('login')

def setpassword(request):
    user = request.user
    context = {
        'user':user,
    }
    if request.method == 'POST':
        username = request.POST.get('new_password')
        new_password = request.POST.get('confirm_password')
        if username == new_password:
           user.set_password(new_password)
           user.save()
           update_session_auth_hash(request, user)
           messages.success(request, 'Password updated successfully.')
           return redirect('dashboard')
        else:
            messages.error(request, 'Password does not match!')
            return redirect('setpassword')
    return render(request, 'dashboard/setpassword.html',context)



@login_required(login_url='login')
def changepassword(request):
    user = request.user
    context = {
        'user':user,
    }
    if request.method == 'POST':
        current_password = request.POST.get('current_password')
        print(current_password)
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        # user = Account.objects.get(username__exact=request.user.username)
        user = request.user

        if new_password == confirm_password:
            success=user.check_password(current_password)
            if request.user.check_password(current_password):
                print("mathew")
                user.set_password(new_password)
                user.save()
                update_session_auth_hash(request, request.user)
                # auth.logout(request)
                messages.success(request, 'Password updated successfully.')
                return redirect('changepassword')
            else:
                messages.error(request, 'Please enter valid current password')
                return redirect('changepassword')
        else:
            messages.error(request, 'Password does not match!')
            return redirect('changepassword')
    return render(request, 'dashboard/changepassword.html',context)

@login_required(login_url='login')
def verify(request, pk ):
    if request.method == 'POST':

        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        address1 = request.POST.get('address1')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        phonenumber = request.POST.get('phonenumber')

        user = request.user
        if len(phonenumber)==10:
            try:
               water = UserProfile.objects.get(user=user)
            except UserProfile.DoesNotExist:
                    water=None
            
            if water is not None:
                  water.address_line_1=address1
                  print(address1)
                  water.city=city
                  print(city)
                  water.state=state
                  print(state)
                  water.pincode=pincode
                  water.save()
                  print(pincode)
                  print("india")
            else:
               user.phone_number=phonenumber
               user.first_name=firstname
               user.last_name=lastname
               user.save()
               new_instance = UserProfile(user=user,address_line_1=address1,city=city,state=state,pincode=pincode)
               new_instance.save()
            messages.success(request, "profile updated sucessfully")
        else:
            messages.error(request,'enter a 10 digit phone number')
    
    user= request.user
    try:
        ans = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
           ans = None
    context = {
        'user':user,
        'ans':ans
    }
    return render(request, 'dashboard/updateprofile.html',context)



def messagefrombuyer(request,id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
       property = Product.objects.get(id=id)
       messagefrombuyer = request.POST.get('Message')
       buyerphonenumber = request.POST.get('phonenumber')

             
       user = request.user
       try:
         ans = Messagemodel.objects.get(buyer=user,property=property)
       except Messagemodel.DoesNotExist:
           ans = None

       if ans is not None:
          messages.error(request,'You already made a equiry for a this property')
          print(ans)
          return redirect(url)
          
       if  buyerphonenumber != None and len(buyerphonenumber) < 10 :
          messages.error(request,'phone number cannot be less than 10 digit')
          return redirect(url)   

       if request.user.phone_number == '' and buyerphonenumber:
         user.phone_number = buyerphonenumber
         user.save()
    
       property = Product.objects.get(id=id)
       seller = property.propertyowner
       buyer = request.user
       phonenumber = buyer.phone_number
       print(phonenumber)
       new_instance = Messagemodel(buyer=buyer,property=property,seller=seller,messagebybuyer=messagefrombuyer,buyerphonenumber=phonenumber)
       new_instance.save()
       messages.success(request, "Message Send Successfully!!")
    
    return redirect(url)


