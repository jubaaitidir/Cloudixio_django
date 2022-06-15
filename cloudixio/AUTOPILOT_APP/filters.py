import django_filters
from .models import Consultant, Competences

class ConsultantFilter(django_filters.FilterSet):
    
    order=(
        ('ascending','Ascending'),
        ('descending','Descending')
    )
    
    choices_id=[(id,id) for id in Consultant.objects.all().values_list('idConsultant', flat=True).distinct()]
    choices_nom=[(n,n) for n in Consultant.objects.all().values_list('nom', flat=True).distinct()]
    choices_competences=[(n,n) for n in Competences.objects.all().values_list('description', flat=True).distinct()]
    
    
    ordering_by_id= django_filters.ChoiceFilter(label='ordonner par id', empty_label="order", choices=order, method='order_by_id')
    filtering_by_id= django_filters.ChoiceFilter(label='idCondultant', choices=choices_id,empty_label="ID", method='filter_by_id')
    filtering_by_nom = django_filters.ChoiceFilter(label='Nom', choices=choices_nom, empty_label="Nom",method='filter_by_nom')
    filtering_by_competence = django_filters.MultipleChoiceFilter(
        label='competences',
        lookup_expr='contains',
        conjoined=True,  # uses AND instead of OR
        choices=choices_competences,
        method='filter_by_competence'
    )
   
   
   
    def __init__(self, *args, **kwargs):
        super(ConsultantFilter, self).__init__(*args, **kwargs)

        for field_name in self.Meta.fields:
            field = self.Meta.fields.get(field_name)
            print(field)
            # field.widget.attrs['placeholder'] = field.label
            #field.label = ''
    
    class Meta:
        model = Consultant
        fields = {
            'nom':['icontains'], 
            'prenom':['icontains'],
            }
  
        
    def order_by_id(self, queryset, name, value):
        expression = 'idConsultant' if value=='ascending' else '-idConsultant'
        return queryset.order_by(expression) 
    
    def filter_by_id(self, queryset, name, value):
        # expression = '1' if value=='1' else '2'
        return queryset.filter(idConsultant=value) 

    def filter_by_nom(self, queryset, name, value): 
        # expression = '1' if value=='1' else '2'
        print(value)
        return queryset.filter(nom=value) 
    
    def filter_by_competence(self, queryset, name, value):
        # expression = '1' if value=='1' else '2'
        print(value)
        if len(value)==1:
            comp=value[0]
            list_competences=Competences.objects.filter(description=comp)
        elif len(value)>1:
            # comp=value[0]+" "+value[1]
            list_competences=Competences.objects.filter(description__in=value)
        # print(list_competences)
        return queryset.filter(competences__in=list_competences).distinct()