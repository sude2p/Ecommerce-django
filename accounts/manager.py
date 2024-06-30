from django.contrib.auth.models import BaseUserManager

#creating normal user
class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('The Email field must be set')
        
        if not username:
            raise ValueError('Use must have an username')
        
        # email = self.normalize_email(email)
        user = self.model(
                        email=self.normalize_email(email), 
                        username=username,
                        first_name=first_name,
                        last_name=last_name
                        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    
    
    #creating Superuser
    def create_superuser(self, first_name, last_name, email, username, password):

        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name

        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user