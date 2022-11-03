from alphabet2kana import a2k
from alphabet2kana.char_table import A2K
from api.serializers import (
    AlphabetRequestSerializer,
    AlphabetTableSerializer,
    ConverterRequestSerializer,
    ConverterResponseSerializer,
)
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.schemas.openapi import AutoSchema


class ConverterView(RetrieveAPIView):
    schema = AutoSchema()
    serializer_class = ConverterResponseSerializer

    def get(self, request, *args, **kwargs):
        """アルファベットをカタカナに変換するGET method"""
        data = request.GET
        return self.convert(data)

    def post(self, request):
        """アルファベットをカタカナに変換するPOST method"""
        data = request.data
        return self.convert(data)

    def convert(self, data):
        serializer = ConverterRequestSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        result = a2k(**validated_data)

        res_serializer = self.get_serializer(data={"text": result})
        res_serializer.is_valid()
        return Response(res_serializer.validated_data, status=status.HTTP_200_OK)


class AlphabetView(RetrieveAPIView):
    schema = AutoSchema()
    serializer_class = AlphabetTableSerializer

    def get(self, request, *args, **kwargs):
        """アルファベットの変換テーブルとその要素数を返すGET method"""
        data = request.GET
        serializer = AlphabetRequestSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        capital_case = validated_data["capital"]

        items = []
        for k, v in A2K.items():
            if capital_case and k.isupper():
                items.append({"alphabet": k, "katakana": v})
            elif not capital_case and k.islower():
                items.append({"alphabet": k, "katakana": v})

        res_serializer = self.get_serializer(data={"items": items, "num": len(items)})
        res_serializer.is_valid()
        return Response(res_serializer.validated_data, status=status.HTTP_200_OK)
