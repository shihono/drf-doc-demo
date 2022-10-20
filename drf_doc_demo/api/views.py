from alphabet2kana import a2k
from alphabet2kana.char_table import A2K
from api.serializers import (
    AlphabetRequestSerializer,
    AlphabetTableSerializer,
    ConverterRequestSerializer,
    ConvertResponseSerializer,
)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class ConverterView(APIView):
    def get(self, request):
        data = request.GET
        return self.convert(data)

    def post(self, request):
        data = request.data
        return self.convert(data)

    def convert(self, data):
        serializer = ConverterRequestSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        result = a2k(**validated_data)

        res_serializer = ConvertResponseSerializer(data={"text": result})
        res_serializer.is_valid()
        return Response(res_serializer.validated_data, status=status.HTTP_200_OK)


class AlphabetView(APIView):
    upper_items = [
        {"alphabet": k, "katakana": v} for k, v in A2K.items() if k.isupper()
    ]
    lower_items = [
        {"alphabet": k, "katakana": v} for k, v in A2K.items() if k.islower()
    ]

    def get(self, request):
        data = request.GET
        serializer = AlphabetRequestSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        capital_case = validated_data["capital"]

        if capital_case:
            items = self.upper_items
        else:
            items = self.lower_items

        res_serializer = AlphabetTableSerializer(
            data={"items": items, "num": len(items)}
        )
        res_serializer.is_valid()
        return Response(res_serializer.validated_data, status=status.HTTP_200_OK)
