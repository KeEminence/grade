#resources.py
from import_export import resources
from .models import User

class UserResource(resources.ModelResource):

    class Meta:
        model = User       
        #exclude = ('id', )
        import_id_fields=('user_id',)
        #skip_unchanged = True
        fields = ('user_id','user_password',)
        #export_order = ('user_id','user_password')