from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw


# Create your models here.

class Website(models.Model):
    name = models.CharField(max_length=256)
    qr_code = models.ImageField(upload_to='qr_codes', blank=True)

    def __str__(self):
        return str(self.name)
    
    # overide save method
    def save(self, *args, **kwargs):
        # create qrc based on a name field above
        qrcode_img = qrcode.make(self.name)
        # construct image based on some params
        canvas = Image.new('RGB', (290, 290), 'white')
        # draw
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        # create file name
        fname = f'qr_code-{self.name}.png'
        # create In-Memeory File Object
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)


    