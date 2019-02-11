#!/bin/bash
/usr/local/python3/bin/pipenv run pytest tests/test_Akeytorefresh.py tests/test_B_calling.py tests/test_B_energycard.py tests/test_B_refresh.py tests/test_LagouPlus.py tests/test_Refreshed.py tests/test_SwitchingContract.py tests/test_app_b_position.py tests/test_sub_account.py
python3 utils/send_email.py