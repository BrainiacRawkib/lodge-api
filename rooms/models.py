from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Block(models.Model):
    name = models.CharField(max_length=5)
    total_rooms = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])

    def __str__(self):
        return self.name


class Room(models.Model):
    code = models.CharField(max_length=10)
    room_block = models.ForeignKey(Block, related_name='rooms', on_delete=models.CASCADE)
    room_no = models.CharField(max_length=10)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.room_block.name} {self.room_no}'
