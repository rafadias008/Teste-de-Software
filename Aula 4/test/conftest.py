import os
import pytest

from src.carteira_3 import CarteiraDigital


@pytest.fixture
def carteira_com_log():
    log_path = "carteira.log"

    # Setup
    if os.path.exists(log_path):
        os.remove(log_path)

    carteira = CarteiraDigital(log_path=log_path)

    try:
        yield carteira
    finally:
        # Teardown
        if os.path.exists(log_path):
            os.remove(log_path)