from django.contrib.auth.models import ( BaseUserManager )

class AcccountManager(BaseUserManager):
    def create_user(self, email , username , password=None):
        if not email:
            raise ValueError('Email is required')

        if not username:
            raise ValueError('Username is required')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email , username , password=None):
        user = self.create_user(email , username , password)
        user.superuser=True
        user.admin=True
        user.staff=True
        user.save(using=self.db)
        return user
