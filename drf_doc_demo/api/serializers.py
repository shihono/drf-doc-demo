from rest_framework import serializers


class ConverterRequestSerializer(serializers.Serializer):
    text = serializers.CharField()
    delimiter = serializers.CharField(required=False, help_text="区切り文字")
    numeral = serializers.BooleanField(required=False, help_text="数字も変換するフラグ")


class ConvertResponseSerializer(serializers.Serializer):
    text = serializers.CharField()


class AlphabetRequestSerializer(serializers.Serializer):
    capital = serializers.BooleanField(
        required=False, default=True, help_text="大文字アルファベット"
    )


class AlphabetItemField(serializers.DictField):
    alphabet = serializers.CharField(help_text="アルファベット")
    katakana = serializers.CharField(help_text="カタカナ")


class AlphabetTableSerializer(serializers.Serializer):
    items = serializers.ListField(child=AlphabetItemField(), allow_empty=False)
    num = serializers.IntegerField(help_text="数")
