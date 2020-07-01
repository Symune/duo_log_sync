from duologsync.consumer import base_consumer

class TelephonyConsumer(base_consumer.BaseConsumer):

    def __init__(self, log_queue, writer, g_vars):
        super().__init__(log_queue, writer, g_vars)
        self.log_type = "telephony"
