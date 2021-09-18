from rest_framework import serializers
from rest_framework import exceptions
from django.conf import settings
from . import models

class LoginSerializer(serializers.ModelSerializer):
    # 覆盖，避免login校验username有数据库唯一字段约束的限制
    username = serializers.CharField()

    class Meta:
        model = models.User
        # username、password可以通过局部钩子指定详细的校验规则
        fields = ('id', 'username', 'password', 'icon')
        extra_kwargs = {
            'id': {
                'read_only': True,
            },
            'icon': {
                'read_only': True,
            },
            'password': {
                'write_only': True,
            }
        }

    def validate(self, attrs):
        # 多方式得到user
        user = self._get_user(attrs)
        # user签发token
        token = self._get_token(user)
        # token用context属性携带给视图类
        self.context['token'] = token

        ''' 自己将user的信息逐个处理，传给视图
        # 前台可能不仅仅只需要登录成功的token，可能还需要用户名、用户头像等
        self.context['username'] = user.username

        # 通过请求头格式化icon
        request = self.context['request']
        icon = 'http://%s%s%s' % (request.META['HTTP_HOST'], settings.MEDIA_URL, user.icon)
        self.context['icon'] = icon
        '''
        # 将登录用户对象直接传给视图
        self.context['user'] = user

        return attrs

    def _get_user(self, attrs):
        import re
        username = attrs.get('username')
        if re.match(r'^1[3-9][0-9]{9}$', username):
            user = models.User.objects.filter(mobile=username).first()
        else:
            user = models.User.objects.filter(username=username).first()
        if not user:
            raise exceptions.ValidationError({'username': 'username error'})

        password = attrs.get('password')
        if not user.check_password(password):
            raise exceptions.ValidationError({'password': 'password error'})

        return user

    def _get_token(self, user):
        from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return token