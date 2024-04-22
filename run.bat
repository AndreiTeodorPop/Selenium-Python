pytest -v -s -m "sanity and regression" --html=./Reports/report_both.html testCases/ --browser chrome
pytest -v -s -m "sanity and regression" --html=./Reports/report_both.html testCases/ --browser firefox


REM pytest -v -s -m "sanity or regression" --html=./Reports/report_all.html testCases/ --browser chrome
REM pytest -v -s -m "sanity" --html=./Reports/report_sanity.html testCases/ --browser chrome
REM pytest -v -s -m "regression" --html=./Reports/report_regression.html testCases/ --browser chrome