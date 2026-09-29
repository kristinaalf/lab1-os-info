import platform
import os
import sys
import json
import shutil
from datetime import datetime


def get_os_info():
    """Собирает информацию о системе."""
    
    # Определяем ОС
    system_name = platform.system()
    
    # Собираем информацию о диске
    disk = shutil.disk_usage("/")
    disk_total = round(disk.total / (1024 ** 3), 2)
    disk_free = round(disk.free / (1024 ** 3), 2)
    
    # Информация о процессоре
    processor = platform.processor()
    
    # Версия Python
    python_version = platform.python_version()
    python_impl = platform.python_implementation()
    
    # Данные пользователя
    username = os.getenv("USERNAME") or os.getenv("USER")
    home_dir = os.path.expanduser("~")
    comp_name = os.getenv("COMPUTERNAME") or platform.node()
    
    # Формируем итоговый словарь
    info = {
        "operating_system": {
            "name": system_name,
            "release": platform.release(),
            "version": platform.version(),
            "machine": platform.machine(),
            "processor": processor,
        },
        "python": {
            "version": python_version,
            "implementation": python_impl,
            "executable": sys.executable,
        },
        "user": {
            "username": username,
            "home_directory": home_dir,
            "computer_name": comp_name,
        },
        "hardware": {
            "cpu_count": os.cpu_count(),
            "disk_total_gb": disk_total,
            "disk_free_gb": disk_free,
        },
        "collected_at": datetime.now().isoformat(),
    }
    
    return info


def save_to_json(data, filename="os_info.json"):
    """Сохраняет данные в JSON-файл."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f"Данные сохранены в {filename}")


if __name__ == "__main__":
    os_info = get_os_info()
    save_to_json(os_info)