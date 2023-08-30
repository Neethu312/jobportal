from rest_framework.views import APIView, Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from .serializers import *
# Create your views here.


class CompanyRegisterView(APIView):
    authentication_classes = []
    permission_classes = (AllowAny,)

    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password1 = request.data.get('password1')
        password2 = request.data.get('password2')
        if password1 == password2:
            custom_ser = CustomUserSerializer(
                data={
                    'username': username,
                    'email': email,
                    'password': password1,
                    'role': 2
                    }
            )

            if custom_ser.is_valid():
                custom_ser.save()

                company_id = custom_ser.data['id']
                company = CustomUser.objects.filter(id=company_id).first()
                company_ser = CompanyProfileSerializer(data=request.data)

                if company_ser.is_valid():
                    company_ser.save(fk_company=company)
                    return Response(
                    {
                        'success': True,
                        'data':  company_ser.data,
                        'message': 'Company Successfully Registered ',
                        'errors': None
                    })
                return Response(company_ser.errors)

            return Response(custom_ser.errors)

        return Response(
            {
                'success': False,
                'data': None,
                'message': 'Password Mismatch',
                'errors': None
            }
        )



class ApplicantProfileView(APIView):
    authentication_classes = []
    permission_classes = (AllowAny,)

    def post(self,request):
        username = request.data.get('username')
        email = request.data.get('email')
        password1 = request.data.get('password1')
        password2 = request.data.get('password2')
        if password1 == password2:
            custom_ser = CustomUserSerializer(
                data={
                    'username': username,
                    'email': email,
                    'password': password1,
                    'role': 3
                    }
            )

            if custom_ser.is_valid():
                custom_ser.save()

                applicant_id = custom_ser.data['id']
                applicant = CustomUser.objects.filter(id=applicant_id).first()
                applicant_ser = ApplicantProfileSerializer(data=request.data)

                if applicant_ser.is_valid():
                    applicant_ser.save(fk_user=applicant)
                    return Response(
                    {
                        'success': True,
                        'data':  applicant_ser.data,
                        'message': 'Applicant Successfully Registered',
                        'errors': None
                    })
                return Response(applicant_ser.errors)

            return Response(custom_ser.errors)

        return Response(
            {
                'success': False,
                'data': None,
                'message': 'Password Mismatch',
                'errors': None
            }
        )

