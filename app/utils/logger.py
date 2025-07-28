import logging
import os

os.makedirs("logs", exist_ok=True)

app_logger = logging.getLogger("app_logger")
app_logger.setLevel(logging.INFO)
app_handler = logging.FileHandler("logs/app.log")
app_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
app_logger.addHandler(app_handler)

admin_logger = logging.getLogger("admin_logger")
admin_logger.setLevel(logging.INFO)
admin_handler = logging.FileHandler("logs/admin.log")
admin_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
admin_logger.addHandler(admin_handler)

error_logger = logging.getLogger("error_logger")
error_logger.setLevel(logging.ERROR)
error_handler = logging.FileHandler("logs/errors.log")
error_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
error_logger.addHandler(error_handler)
