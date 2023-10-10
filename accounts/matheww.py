


class Plans(models.Model):
    max_content_length      = 20000
    rgb                     = models.CharField(blank=True, max_length=256)

    name                    = models.CharField(max_length=50)
    long_name               = models.CharField(blank=True, null=True, max_length=100)
    description             = models.TextField(max_length=max_content_length, blank=True, validators=[MaxLengthValidator(max_content_length)])
    schedule                = models.TextField(max_length=max_content_length, blank=True, validators=[MaxLengthValidator(max_content_length)])

    ## Price for a month
    price                   = models.CharField(max_length=20)
    price_description       = models.CharField(max_length=250)

    ## Price for six months
    six_months_price        = models.CharField(max_length=20)
    six_months_description  = models.CharField(max_length=250)

    ## Price for a year
    year_price              = models.CharField(max_length=20)
    year_description        = models.CharField(max_length=250)

    ## Level will be used to give access to videos
    level                   = models.IntegerField(blank=True, null=True)

    ## Aditional information about the plan
    option1                 = models.CharField(max_length=50)
    option2                 = models.CharField(max_length=50)
    option3                 = models.CharField(max_length=50)

    ## Markdown content of the
    markdown_content    = models.TextField(max_length=max_content_length, blank=True, validators=[MaxLengthValidator(max_content_length)])

    ## When actual service agrement was created
    created_date        = models.DateTimeField(auto_now=True, help_text="HH:MM:SS DD Mmm YY, YYYY PST")

    ## When service agrement will was update
    updated_date        = models.DateTimeField(auto_now=True, help_text="HH:MM:SS DD Mmm YY, YYYY PST")

    ACCESS_CHOICES = [
        ('limited', 'Limited Access'),
        ('full', 'Full Access'),
    ]
      
    highlight_info=models.CharField(max_length=200)

    highlight_desc=models.CharField(max_length=200)

    classes=models.CharField(max_length=200)

    standups=models.CharField(max_length=200)

    source_code=models.CharField(max_length=10, choices=ACCESS_CHOICES)

    ticket=models.CharField(max_length=70)

    tools=models.BooleanField(default=False)

    video_desc=models.CharField(max_length=100)

    Help_session=models.CharField(max_length=100)

    sprint_plan=models.CharField(max_length=100)
    individual_meet=models.BooleanField(default=False)
    objects = subscription_plansManager()


    def _str_(self):
        return self.name

    class Meta:
        verbose_name_plural = "plans"
        ordering = ['level']





## The main model for subscriptions
class Subscriber(models.Model):
    ## Paypal Time format
    time_format = '%Y-%m-%dT%H:%M:%SZ'

    ## User who is doing subscription
    user                    = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    ## Geting users infromation for later refernce
    first_name              = models.CharField(max_length=50, null=True)
    last_name               = models.CharField(max_length=50, null=True)
    email                   = models.EmailField(max_length=120,null=True)
    address                 = models.CharField(max_length=200, null=True)
    city                    = models.CharField(max_length=200, null=True)
    state                   = models.CharField(max_length=200, null=True)
    zip_code                = models.CharField(max_length=75, null=True)
    phone                   = models.CharField(max_length=15, null=True)

    # secure_shell            = models.ForeignKey(SecureShell, on_delete=models.CASCADE, null=True)

    ## Type of the subscription which from plans model
    plan                    = models.ForeignKey(Plans, on_delete=models.CASCADE, null=True)

    ## If payment was confirmed
    payment_confirmation    = models.BooleanField(default=False)

    ## When actual subscription was created
    created_date            = models.DateTimeField(blank=True, null=True, help_text="HH:MM:SS DD Mmm YY, YYYY PST")

    ## When subscription will be expired
    expire_date             = models.DateTimeField(blank=True, null=True, help_text="HH:MM:SS DD Mmm YY, YYYY PST")

    def _str_(self):
        return  self.user.username

    def extend(self, period):

        if period == '1-month':
            billing_cycle = 31

        elif period == '6-month':
            billing_cycle = 183

        else:
            billing_cycle = 366

        self.now                    = timezone.now()
        self.created_date           = self.now.strftime('%Y-%m-%dT%H:%M:%SZ')
        self.expire_date            = self.now + timedelta(billing_cycle)
        self.save()

    def is_payment_confirmed(self):
        return self.payment_confirmation != False

    def is_expired(self):
        """
        Method responsible to verify expiration date of the user
        Basic users needs to be enabled manually so it will be managed from FuchiCorp management team
        """
        self.now                    = timezone.now()
        return self.expire_date <= self.now


class Content(models.Model):
    max_content_length  = 20000

    ## Long name of the condition <FuchiCorp Academy Terms and Conditions>
    long_name           = models.CharField(max_length=100)

    ## Which admin user did update
    user                = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    ## Markdown content of the
    markdown_content    = models.TextField(max_length=max_content_length, blank=True, validators=[MaxLengthValidator(max_content_length)])

    ## Should be created <DPA> <Terms of Condition> <Privacy>
    conent_type         = models.CharField(max_length=20)

    ## When actual service agrement was created
    created_date        = models.DateTimeField(auto_now_add=True, help_text="HH:MM:SS DD Mmm YY, YYYY PST")

    ## When service agrement will was update
    updated_date        = models.DateTimeField(auto_now=True, help_text="HH:MM:SS DD Mmm YY, YYYY PST")

    ## When we update it should send an email
    publish             = models.BooleanField(default=False)

    def _str_(self):
        return  self.conent_type






