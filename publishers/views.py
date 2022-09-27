from django.shortcuts import render, reverse
from django.http import  HttpResponseRedirect
from .models import Section, Publisher, Article, Sections
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from .form import (CreateUserForm, EditUserForm, EditPublisherForm, Section_Form,
                   SectionForm, ArticleCreationForm, ArticleModelForm, 
                   PublishArticleForm)
from django.forms import  inlineformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import re
from django.core.mail import send_mail

# Create your views here.


def register(request):
    if request.method == "POST":
        section_pk = int(request.POST["section"])
        section = Section.objects.get(pk=section_pk)
        description = request.POST["description"]
        form = CreateUserForm(request.POST)
        if form.is_valid():
            # form.save()
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            send_mail("Hello Boss", f"There is a new publisher at Illumpedia. Email: {email}", "Illumepedia", [
                'pascalemy2010@gmail.com'], fail_silently=False,)
            user = form.save()
            if not user:
                sections = Section.objects.all()
                form = CreateUserForm()
                return render(request, "publisher/register.html", {"form": CreateUserForm(), "sections": sections})
            Publisher.objects.create(account=user, first_name=first_name,
                                     last_name=last_name, section=section, description=description)
           # return HttpResponseRedirect(reverse("login:loginView"))
            form = AuthenticationForm()
            return render(request, "login/login.html", {"form": form})
        else:
            form = CreateUserForm(request.POST)
            sections = Section.objects.all()
            return render(request, "publisher/register.html", {"form": form, "sections": sections})

    else:
        sections = Section.objects.all()
        form = CreateUserForm()
        return render(request, "publisher/register.html", {"form": CreateUserForm(), "sections": sections})


@login_required(login_url="login:loginView")
def editProfile(request):
    user = request.user
    publisher = Publisher.objects.get(account=user)
    Userform = EditUserForm(instance=user)
    PublisherForm = EditPublisherForm(instance=publisher)
    return render(request, "publisher/editprofile.html", {"userform": Userform, "publisherform": PublisherForm})


@login_required(login_url="login:loginView")
def editProfilePro(request):
    user = request.user
    publisher = Publisher.objects.get(account=user)
    Userform = EditUserForm(data=request.POST, instance=user)
    PublisherForm = EditPublisherForm(data=request.POST, instance=publisher)
    if Userform.is_valid() and PublisherForm.is_valid():
        Userform.save()
        PublisherForm.save()
        username = user.username
        messages.add_message(request, messages.INFO,
                             "Profile Updated Successfully")
        return HttpResponseRedirect(reverse("publisher:publisherView", kwargs={"username":request.user.username,
                                                                               "sectionId":0,"action":"add"}))

@login_required(login_url="login:loginView")
def publisherView(request, username,sectionId,action):
    user = User.objects.get(username=username)
    sections = Section.objects.all()
    try:
        publisher = Publisher.objects.get(account=user)
    except Publisher.DoesNotExist:
        logout(request)
        return HttpResponseRedirect(reverse("publisher:register"))
    if not publisher.verified :
            return render(request, "publisher/nonpublisherview.html", {"username":user.username})
        
    article_form = ArticleCreationForm()
    if sectionId != 0:   
        section_instance = Section.objects.get(id=sectionId)
    
    if request.method == "POST" and action == "add":
        form = Section_Form(data= request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('publisher:publisherView',
            kwargs={"username":user.username,"sectionId":0,"action":"view"}))
        else:
            return render(request,"publisher/publisherview.html",
                  {'article_form':article_form,"form":form,"sectionId":0,"sections":sections,"user": user})  
              
    if action == "edit":
        if request.method == "POST":
            form = Section_Form(data= request.POST,instance=section_instance)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('publisher:publisherView',
                        kwargs={"username":user.username,"sectionId":0,"action":"view"}))
            else:
                return render(request,"publisher/publisherview.html",
                  {'article_form':article_form,"form":form,"sectionId":section_instance.id})
        else:
            return render(request,"publisher/publisherview.html",
                  {"form":Section_Form(instance=section_instance),
                   "sectionId":section_instance.id,"action":"edit",
                   "user": user, "article_form": article_form,
                   "sections":sections,})
    
    if action == "delete":
        section_instance.delete()
        return HttpResponseRedirect(reverse('publisher:publisherView',
            kwargs={"username":user.username,"sectionId":0,"action":"view"}))
    
    return render(request, "publisher/publisherview.html", {"user": user, "article_form": article_form,
                                                                "sections":sections,"form":Section_Form(),
                                                                "sectionId":0,"action":"add"})   


@login_required(login_url="login:loginView")
def ArticleCreateView(request, username):
    user = User.objects.get(username=username)
    publisher = Publisher.objects.get(account=user)
    if request.method == "POST":
        form = ArticleCreationForm(data=request.POST)
        if form.is_valid():
            article = form.save()
            article.publisher.add(publisher)
            return HttpResponseRedirect(reverse('publisher:articleCreationView',
                                                kwargs={"username": username, 'article_id': article.id}))
        else:
            return render(request, "publisher/publisherview.html", {"user": user, "form": form})
    return HttpResponseRedirect(reverse('publisher:articleCreateView', kwargs={"username": username}))



@login_required(login_url="login:loginView")
def ArticleCreationView(request, username, article_id):
    user = User.objects.get(username=username)
   # publisher=Publisher.objects.get(account=user)
    article = Article.objects.get(pk=article_id)
    formsets = inlineformset_factory(
        Article, Sections, form=SectionForm,extra=1)
    SectionForms = formsets(instance=article)
    form = ArticleModelForm(instance=article)
    # referenceForm = ReferenceForm(instance=article)
    if request.method == "POST":
        form = ArticleModelForm(
            data=request.POST, files=request.FILES, instance=article)
        SectionForms = formsets(
            data=request.POST, files=request.FILES, instance=article)
        # referenceForm = ReferenceForm(
            # data=request.POST,  instance=article)
        # if form.is_valid() and SectionForms.is_valid() and referenceForm.is_valid():
        if form.is_valid() and SectionForms.is_valid():
            form.save()
            SectionForms.save()
            # referenceForm.save()
            return HttpResponseRedirect(reverse('publisher:articlePublisherView',
                                                kwargs={"article_id": article.id, "article_slug": article.title_slug}))
        else:
            return render(request, 'publisher/createarticle.html', {'form': form,
                                                                    'sectionsForm': SectionForms, 'article': article, 'user': user})
    return render(request, 'publisher/createarticle.html', {'form': form,
                                                            'sectionsForm': SectionForms, 'article': article, 'user': user})


@login_required(login_url="login:loginView")
def articlePublisherView(request, article_id, article_slug):
    article = Article.objects.get(pk=article_id)
    article_sections = Sections.objects.filter(article=article)
    form = PublishArticleForm(instance=article)
    nullvalue = "<p>null</p>" or "null"
    return render(request, "publisher/articlePublisherView.html",
                  {"article": article, "sections": article_sections, "form": form, "nullvalue": nullvalue})


@login_required(login_url="login:loginView")
def publishView(request, article_id, article_slug):
    user = request.user
    article = Article.objects.get(pk=article_id)
    form = PublishArticleForm(request.POST, instance=article)
    if form.is_valid():
        removeaddedslug = article.title_slug
        article.title_slug = re.sub(
            r"(-transformedslugdjango)", "", removeaddedslug)
        article.save()
        form.save()
        messages.add_message(request, messages.INFO,
                                 "Article published Successfully")
        return render(request, "publisher/articlePublisherView.html",
                          {"article": article, "user": user})
    else:
        return render(request, "publisher/articlePublisherView.html",
                          {"article": article, "user": user, "message": "An Error occured"})


@login_required(login_url="login:loginView")
def controlView(request,sectionId):
    publisher = Publisher.objects.get(account=request.user)
    section = Section.objects.get(id=sectionId)
    article = section.section_article.all()
    return render(request, "publisher/controlview.html", {'publisher': publisher, "section":section,
                                                          'article': article, "user": request.user})


@login_required(login_url="login:loginView")
def editView(request, username, article_id):
    # referenceForm = ReferenceForm(instance=article)
    if request.method == "POST":
        article = Article.objects.get(pk=article_id)
        formsets = inlineformset_factory(
        Article, Sections, form=SectionForm, extra=1)
        SectionForms = formsets(instance=article)
        form = ArticleModelForm(instance=article)
        return render(request, "publisher/editview.html", {'form': form, 'sectionsForm': SectionForms,
                                                           'article': article})
    return HttpResponseRedirect(reverse("publisher:publisherView",
            kwargs={"username":request.user.username,"sectionId":0,"action":"add"}))


@login_required(login_url="login:loginView")
def editPro(request, username, article_id):
    formsets = inlineformset_factory(
        Article, Sections, form=SectionForm, extra=0)
    if request.method == "POST":
        article = Article.objects.get(id=article_id)
        form = ArticleModelForm(
            data=request.POST, files=request.FILES, instance=article)
        # referenceForm = ReferenceForm(data=request.POST, instance=article)
        SectionForms = formsets(
            data=request.POST, files=request.FILES, instance=article)
        if form.is_valid() and SectionForms.is_valid():
            form.save()
            SectionForms.save()
            article.publish = False
            article.save()
            # referenceForm.save()
            return HttpResponseRedirect(reverse('publisher:articlePublisherView',
                                                kwargs={"article_id": article.id, "article_slug": article.title_slug}))
        else:
            return render(request, "publisher/editview.html", {'form': form, 'sectionsForm': SectionForms, 'article': article})

    return HttpResponseRedirect(reverse("publisher:publisherView",
            kwargs={"username":request.user.username,"sectionId":0,"action":"add"}))


@login_required(login_url="login:loginView")
def articleWithdrawView(request, article_id):
    article = Article.objects.get(pk=article_id)
    user = request.user
    if request.method == "POST":
        article.publish = False
        slug = article.title_slug
        transformedSlug = f"{slug}-transformedslugdjango"
        article.title_slug = transformedSlug
        article.save(),
        return HttpResponseRedirect(reverse('publisher:controlView',
                                            kwargs={"sectionId": article.section.id}))


@login_required(login_url="login:loginView")
def articleDeleteView(request, article_id):
    article = Article.objects.get(pk=article_id)
    user = request.user
    if request.method == "POST":
        article.delete()
        return HttpResponseRedirect(reverse('publisher:controlView', kwargs={"sectionId": article.section.id}))

@login_required(login_url="login:loginView")
def close_application(request, article_id, action):
    article = Article.objects.get(pk=article_id)
    user = request.user
    if request.method == "POST" and action == "close":
        article.still_open = False
        article.save()
    else:
        article.still_open = True
        article.save()
    return HttpResponseRedirect(reverse('publisher:controlView', kwargs={"sectionId": article.section.id}))