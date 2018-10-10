from django.test import TransactionTestCase
from django.utils import timezone

# Create your tests here.
from .models import TextNote


class TextNoteModelTests(TransactionTestCase):

    def test_can_create_note(self):
        time = timezone.now()
        fred = TextNote(title='This is test note', text='Not all those who wander are lost')
        fred.save()
        delta = fred.createdOn - time
        self.assertLessEqual(timezone.timedelta(0), delta, 'created date is in the future???')
        self.assertGreaterEqual(timezone.timedelta(seconds=2), delta, 'created date is too far in past')
