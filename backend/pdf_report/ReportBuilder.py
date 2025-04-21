from Report import Report

class ReportBuilder:
    def __init__(self):
        self.include_logo = False
        self.title = "Reporte de Pago"
        self.include_payment_details = False
        self.include_user_info = False
        self.theme = "LIGHT"
        self.include_timestamp = False
        self.footer_message = ""
        self.format = "A4"

    def set_include_logo(self, include_logo):
        self.include_logo = include_logo
        return self

    def set_title(self, title):
        self.title = title
        return self

    def set_include_payment_details(self, include_payment_details):
        self.include_payment_details = include_payment_details
        return self

    def set_include_user_info(self, include_user_info):
        self.include_user_info = include_user_info
        return self

    def set_theme(self, theme):
        self.theme = theme
        return self

    def set_include_timestamp(self, include_timestamp):
        self.include_timestamp = include_timestamp
        return self

    def set_footer_message(self, footer_message):
        self.footer_message = footer_message
        return self

    def set_format(self, format):
        self.format = format
        return self

    def build(self):
        return Report(
            include_logo=self.include_logo,
            title=self.title,
            include_payment_details=self.include_payment_details,
            include_user_info=self.include_user_info,
            theme=self.theme,
            include_timestamp=self.include_timestamp,
            footer_message=self.footer_message,
            format=self.format,
        )