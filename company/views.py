from rest_framework.views import APIView, Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from accounts.models import *
from .serializers import *

# Create your views here.

class JobAddView(APIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        company = request.user
        company_id = CompanyProfile.objects.filter(fk_comapny=company).first()
        jobadd_ser = JobAddSerializer(data=request.data)
        if jobadd_ser.is_valid():
            jobadd_ser.save(fk_comapny_pro=company_id)
            return Response(
                                {
                                    'success': True,
                                    'data': jobadd_ser.data,
                                    'message': 'Job added Successfully',
                                    'errors': None
                                }
                            )
        else:
            return Response(
                        {
                            'success': False,
                            'data': None,
                            'message': 'Unsuccessful',
                            'errors': jobadd_ser.errors,
                        }
                    )




