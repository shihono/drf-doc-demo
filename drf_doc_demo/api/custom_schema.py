import warnings

from rest_framework.schemas.openapi import AutoSchema
from rest_framework.filters import BaseFilterBackend
from rest_framework import exceptions
from rest_framework.fields import BooleanField, IntegerField, FloatField, empty, Field


class CustomSchema(AutoSchema):

    def get_request_serializer(self, path, method):
        """requestBodyのoperationを取得
        get_request_serializerを利用
        """
        view = self.view

        if not hasattr(view, 'get_request_serializer'):
            return super().get_request_serializer(path, method)

        return view.get_request_serializer()


class CustomFilterBackend(BaseFilterBackend):
    @staticmethod
    def get_oai_type(value: Field):
        """oai の data type を設定

        - string, integer, boolean, numberのみ対応
        - array, object は未対応
        """
        value_field = type(value)
        type_ = "string"
        if value_field == IntegerField:
            type_ = "integer"
        elif value_field == BooleanField:
            type_ = "boolean"
        elif value_field == FloatField:
            type_ = "number"
        return type_

    def get_schema_operation_parameters(self, view):
        """parametersを取得
        view.parameter_serializer を利用
        """
        parameter_schema = getattr(view, "parameter_serializer")
        parameter = []
        if parameter_schema is None:
            return parameter

        for name, field in parameter_schema.fields.items():
            p_type = self.get_oai_type(field)
            p_field = {
                "name": name,
                "required": field.required,
                "in": "query",
                "description": field.help_text,
                "schema": {"type": p_type},
            }
            if field.default != empty:
                p_field["default"] = field.default
            parameter.append(p_field)
        return parameter
