from django.shortcuts import render, reverse
from django.http import  HttpResponseRedirect
from publishers.models import Section, Article, Sections
from application.form import application_form

# Create your views here.
def homeView(request):
    return render(request,'home/index.html')

def hrView(request):
    return render(request,'home/hr.html')

def legalView(request):
    return render(request,'home/legal.html')

def articleView(request, article_id, article_slug):
    article = None
    try:
        article = Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        return HttpResponseRedirect(reverse('frontview:homeView',
            kwargs={}))       
    article_sections = Sections.objects.filter(article=article)
    section = Section.objects.get(section_article=article)
    articles = section.section_article.filter(
        publish=True, still_open = True)
    nullvalue = "<p>null</p>" or "null"
    history= "HISTORY"
    article.view_count += 1
    article.save(skip_md=False)
    form = application_form()
    message = None
    mostViewed = Article.objects.filter(section=section).filter(
        publish=True,still_open = True).order_by("-view_count")[:10]
    # articles=Article.objects.filter(section=section)
    if request.method == "POST":
        registeration_form = application_form(
        data=request.POST, files=request.FILES)
        if registeration_form.is_valid():
            registeration_form.save()
            message = "Application submitted successfully."
    if article.title_slug != article_slug:
        return render(request, "home/pagenotfound.html", {
            "sections": article_sections, "section": section,
            'articles':articles,"mostviewed": mostViewed})
    return render(request, "home/articleview.html", {"article": article,"sections": article_sections,
                                                     "section": section, "mostviewed": mostViewed, 
                                                     "nullvalue": nullvalue,"HISTORY":history,
                                                     "registrationForm":form,'message':message,
                                                     'articles':articles})


def sectionView(request, section):
    section = Section.objects.get(Name=section)
    articles = Article.objects.filter(section=section).filter(
        publish=True,still_open = True)
    mostViewed = Article.objects.filter(section=section).filter(
        publish=True,still_open = True).order_by("-view_count")[:10]
    return render(request, "home/sectionView.html", {"section": section,'articles':articles,
                                                     "mostviewed": mostViewed})