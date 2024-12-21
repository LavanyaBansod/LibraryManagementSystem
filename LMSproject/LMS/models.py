from django.db import models

class Member(models.Model):
    membership_no = models.CharField(max_length=20, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    address = models.TextField()
    email = models.EmailField()
    phone_no = models.CharField(max_length=15)
    account_no = models.CharField(max_length=20)
    identity_number = models.CharField(max_length=50)
    membership_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    book_id = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    pages = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.title

class Copy(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    sub_id = models.CharField(max_length=20)
    is_issued = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.book.title} - {self.sub_id}"

class IssuedBook(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    copy = models.ForeignKey(Copy, on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now_add=True)
    reissue_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.member} - {self.book.title}"
