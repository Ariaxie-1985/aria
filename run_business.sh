#!/bin/bash
/root/.local/bin/pipenv run pytest tests/test_business/ --html=backend/templates/business_report.html --self-contained-html


