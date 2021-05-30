from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .models import aerifyDailyAPI, aerifyMonthlyAPI, aerifyYearlyAPI


class aerifyDailyAPISerializer(ModelSerializer):

    class Meta:
        model = aerifyDailyAPI
        fields = '__all__'


class aerifyDailyAPIViewSet(ReadOnlyModelViewSet):
    """
        list:
        Returns a list of all the existing data.

        read:
        Returns the data of a particular id.
    """
    queryset = aerifyDailyAPI.objects.all()
    serializer_class = aerifyDailyAPISerializer


# class aerifyDailyAPIViewSet(ReadOnlyModelViewSet):
#     """
#         list:
#         Returns a list of all the existing data.
#
#         read:
#         Returns the data of a particular id.
#     """
#     queryset = aerifyDailyAPI.objects.filter(city="delhi".capitalize())
#     serializer_class = aerifyDailyAPISerializer


class aerifyMonthlyAPISerializer(ModelSerializer):

    class Meta:
        model = aerifyMonthlyAPI
        fields = '__all__'


class aerifyMonthlyAPIViewSet(ReadOnlyModelViewSet):
    """
        list:
        Returns a list of all the existing data.

        read:
        Returns the data of a particular id.
    """
    queryset = aerifyMonthlyAPI.objects.all()
    serializer_class = aerifyMonthlyAPISerializer


class aerifyYearlyAPISerializer(ModelSerializer):

    class Meta:
        model = aerifyYearlyAPI
        fields = '__all__'


class aerifyYearlyAPIViewSet(ReadOnlyModelViewSet):
    """
        list:
        Returns a list of all the existing data.

        read:
        Returns the data of a particular id.
    """
    queryset = aerifyYearlyAPI.objects.all()
    serializer_class = aerifyYearlyAPISerializer

