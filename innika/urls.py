"""innika URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include
from django.contrib.auth import views as auth_views
from adminfunction.forms import LoginForm
from django.views.generic import TemplateView
from adminfunction import views as admin_view
from location import views as location_view
from page import views as page_view
from faqs import views as faqs_view
from menu import views as menu_view
from testimonial import views as testimonial_view
from properties import views as properties_view
from frontend import views as frontend_view
from contactus import views as contactus_view
from makeenquery import views as makeenquery_view
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # path('admin/', admin.site.urls),
    #Admin URL
    path('dj-admin',admin_view.admin_login,name='adminlogin'),
    path('admin/dashboard',admin_view.dashboard,name='dashboard'),
    path('logout',admin_view.handlelogout),
    path('admin/addlocation',location_view.addlocation,name='addlocation'),
    path('admin/location',location_view.location,name='location'),
    path('admin/deletelocation/<int:locationid>',location_view.deletelocation),
    path('admin/editlocation/<int:locationid>',location_view.editlocation),
    path('admin/page',page_view.page,name='page'),
    path('admin/addpage',page_view.addpage,name='addpage'),
    path('admin/editpage/<int:pageid>',page_view.editpage,name='editpage'),
    path('admin/deletepage/<int:pageid>',page_view.addpage,name='deletepage'),
    path('admin/faqs/add',faqs_view.addfaqs,name='addfaqs'),
    path('admin/faqs/edit/<int:faqsid>',faqs_view.editfaqs,name='editfaqs'),
    path('admin/faqs',faqs_view.faqs,name='adminfaqs'),
    path('admin/faqs/delete/<int:faqsid>',faqs_view.deletefaqs,name='deletefaqs'),
    path('admin/testimonial/add',testimonial_view.add,name='addtestimonial'),
    path('admin/testimonial',testimonial_view.index,name='admintestimonial'),
    path('admin/testimonial/edit/<int:testimonialid>',testimonial_view.edit,name='edittestimonial'),
    path('admin/testimonial/delete/<int:testimonialid>',testimonial_view.delete,name='deletetestimonial'),
    path('admin/change-password/',admin_view.PasswordChangeView.as_view(template_name='admintemplates/change-password.html'),name='change_password'),
    path('admin/user-profile/',admin_view.PasswordChangeView.as_view(template_name='admintemplates/user-profile.html'),name='user_profile'),
    path('admin/properties',properties_view.index,name='adminproperties'),
    path('admin/properties/edit/<int:propertiesid>',properties_view.edit,name='editproperties'),
    path('admin/properties/create',properties_view.create,name='createproperties'),
    path('admin/properties/delete/<int:propertiesid>',properties_view.delete,name='deleteimageproperties'),
    path('admin/properties/deleteproperties/<int:propertiesid>',properties_view.deleteproperties,name='deleteproperties'),
    path('admin/properties/deleteproperties/<int:propertiesid>',properties_view.deleteproperties,name='deleteproperties'),
    path('admin/menu',menu_view.menu,name='menu'),
    path('admin/contactus',contactus_view.index,name='contactus'),
    path('admin/enquery',makeenquery_view.index,name='enquery'),
    path('ckeditor',include('ckeditor_uploader.urls')),
    #Frontend URL
    path('',frontend_view.home,name='home'),
    path('page/<str:pageslug>',frontend_view.index,name='index'),
    path('location/',frontend_view.location,name='location1'),
    path('properties/',frontend_view.properties,name='properties'),
    path('propertiesdetails/<str:slug>/',frontend_view.property_details,name='propertiesdetails'),
    path('testimonial',frontend_view.testimonial,name='testimonial'),
    path('faqs',frontend_view.faqs,name='faqs'),
    path('addcontactus',contactus_view.contactuspost),
    path('addcontactus',contactus_view.contactuspost),
    path('enquery',frontend_view.makeenquery,name='makeenquery'),
    path('addenquery',makeenquery_view.addmakeenquery,name='addmakeenquery'),
# )
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

