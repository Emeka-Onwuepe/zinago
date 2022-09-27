from publishers.models import Section
def context_processor(request):
    unsorted_sections = Section.objects.filter(section_article__publish = True)
    sorted_sections = []
    for section in unsorted_sections:
        if section not in sorted_sections:
            sorted_sections.append(section)
    return {"sorted_sections":sorted_sections}