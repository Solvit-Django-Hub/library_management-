
from django.conf import settings
from django.db import models
from books.models import Book
from datetime import date

# Create your models here.
class Borrowing(models.Model):
    BORROWED="Borrowed"
    RETURNED="Returned"
    OVERDUE="Overdue"

    STATUS_CHOICES=[
        (BORROWED, "Borrowed"),
        (RETURNED, "Returned"),
        (OVERDUE,"Overdue"),
    ]
    member=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="borrowings")
    book = models.ForeignKey(Book,on_delete=models.CASCADE,related_name="borrowings")
    borrowed_date=models.DateField(auto_now_add=True)
    due_date = models.DateField()
    returned_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=BORROWED)
  

    def __str__(self):
        return f'{self.member.username} borrowed {self.book.title}'
    
    def check_overdue(self):
        today = date.today()
        if self.status == self.BORROWED and self.due_date < today:
            self.status = self.OVERDUE
            self.save()
class Fine(models.Model):
    borrowing=models.OneToOneField(Borrowing,on_delete=models.CASCADE,related_name="fine")
    amount=models.DecimalField(max_digits=10,decimal_places=2,default=0)
    paid=models.BooleanField(default=False)
    created_at=models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Fine for {self.borrowing.member.username} - {self.amount}'
    
