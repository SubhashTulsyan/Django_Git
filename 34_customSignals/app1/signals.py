from django.dispatch import Signal, receiver

send_coupon = Signal(providing_args=['Rs 100', 'Rs 200'])

@receiver(send_coupon)
def coupon(sender, *args, **kwargs):
    print('--in coupon signal--')
    print('Sender: ', sender)
    print('args: ', args)
    print('kwargs: ', kwargs)