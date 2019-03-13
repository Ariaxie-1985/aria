#!/bin/bash
/root/.local/bin/pipenv run pytest tests/test_zhaopin_app/test_app_b_chat.py tests/test_zhaopin_app/test_app_b_position.py --alluredir report
