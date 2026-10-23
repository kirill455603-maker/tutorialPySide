@echo off
chcp 65001 >nul
echo ========================================
echo Конвертация UI и QRC файлов в Python...
echo ========================================
echo.

set UIC_PATH="S:\python\projects\PythonProject_tutorialPySide6\.venv\Lib\site-packages\PySide6\uic.exe"
set RCC_PATH="S:\python\projects\PythonProject_tutorialPySide6\.venv\Lib\site-packages\PySide6\rcc.exe"

echo [1/2] Конвертация UI файлов...
echo ----------------------------------------

%UIC_PATH% -g python ui_page_tokarnaya.ui -o ui_page_tokarnaya.py
%UIC_PATH% -g python ui_page_tokarnaya_start.ui -o ui_page_tokarnaya_start.py
%UIC_PATH% -g python ui_page_select_operation.ui -o ui_page_select_operation.py
%UIC_PATH% -g python ui_page_tokarnaya_podrezka.ui -o ui_page_tokarnaya_podrezka.py
%UIC_PATH% -g python ui_autoinput.ui -o ui_autoinput.py
%UIC_PATH% -g python ui_page_normirovanie.ui -o ui_page_normirovanie.py
%UIC_PATH% -g python ui_page_markirovanie.ui -o ui_page_markirovanie.py
%UIC_PATH% -g python ui_page_kontrol_otk.ui -o ui_page_kontrol_otk.py
%UIC_PATH% -g python ui_page_input_technopro.ui -o ui_page_input_technopro.py
%UIC_PATH% -g python ui_dialog_termichka.ui -o ui_dialog_termichka.py
%UIC_PATH% -g python ui_dialog_slesarnaya.ui -o ui_dialog_slesarnaya.py
%UIC_PATH% -g python ui_dialog_sborka.ui -o ui_dialog_sborka.py
%UIC_PATH% -g python ui_dialog_promivka.ui -o ui_dialog_promivka.py
%UIC_PATH% -g python ui_dialog_predlog.ui -o ui_dialog_predlog.py
%UIC_PATH% -g python ui_dialog_normirovanie_select_turning_operation.ui -o ui_dialog_normirovanie_select_turning_operation.py
%UIC_PATH% -g python ui_dialog_normirovanie_markirovanie.ui -o ui_dialog_normirovanie_markirovanie.py
%UIC_PATH% -g python ui_dialog_find_sverlo.ui -o ui_dialog_find_sverlo.py
%UIC_PATH% -g python ui_dialog_exit.ui -o ui_dialog_exit.py
%UIC_PATH% -g python ui_dialog_clear_table.ui -o ui_dialog_clear_table.py
%UIC_PATH% -g python ui_page_razmetka.ui -o ui_page_razmetka.py
%UIC_PATH% -g python ui_page_sborka.ui -o ui_page_sborka.py
%UIC_PATH% -g python ui_page_sverlilnaya.ui -o ui_page_sverlilnaya.py
%UIC_PATH% -g python ui_page_sverlilnaya_chistovaya.ui -o ui_page_sverlilnaya_chistovaya.py
%UIC_PATH% -g python ui_page_sverlilnaya_expanding_hole.ui -o ui_page_sverlilnaya_expanding_hole.py
%UIC_PATH% -g python ui_page_sverlilnaya_faska.ui -o ui_page_sverlilnaya_faska.py
%UIC_PATH% -g python ui_page_sverlilnaya_rezba.ui -o ui_page_sverlilnaya_rezba.py
%UIC_PATH% -g python ui_page_sverlilnaya_start.ui -o ui_page_sverlilnaya_start.py
%UIC_PATH% -g python ui_page_tehno_iot.ui -o ui_page_tehno_iot.py
%UIC_PATH% -g python ui_page_tokarnaya_angle.ui -o ui_page_tokarnaya_angle.py
%UIC_PATH% -g python ui_page_tokarnaya_faska.ui -o ui_page_tokarnaya_faska.py
%UIC_PATH% -g python ui_page_tokarnaya_podrezka.ui -o ui_page_tokarnaya_podrezka.py
%UIC_PATH% -g python ui_page_tokarnaya_rastachivanie.ui -o ui_page_tokarnaya_rastachivanie.py
%UIC_PATH% -g python ui_page_tokarnaya_rezba.ui -o ui_page_tokarnaya_rezba.py
%UIC_PATH% -g python ui_page_tokarnaya_start.ui -o ui_page_tokarnaya_start.py
%UIC_PATH% -g python ui_page_tokarnaya_sverlenie.ui -o ui_page_tokarnaya_sverlenie.py
%UIC_PATH% -g python ui_page_tokarnaya_tochenie.ui -o ui_page_tokarnaya_tochenie.py
%UIC_PATH% -g python ui_row_detail.ui -o ui_row_detail.py
%UIC_PATH% -g python ui_widget_bolts.ui -o ui_widget_bolts.py
%UIC_PATH% -g python ui_widget_deistvie.ui -o ui_widget_deistvie.py
%UIC_PATH% -g python ui_widget_details.ui -o ui_widget_details.py
%UIC_PATH% -g python ui_widget_normirovanie_button.ui -o ui_widget_normirovanie_button.py
%UIC_PATH% -g python ui_widget_normirovanie_cutting.ui -o ui_widget_normirovanie_cutting.py
%UIC_PATH% -g python ui_widget_normirovanie_shlifovka.ui -o ui_widget_normirovanie_shlifovka.py
%UIC_PATH% -g python ui_widget_normirovanie_sverlilnaya.ui -o ui_widget_normirovanie_sverlilnaya.py
%UIC_PATH% -g python ui_widget_normirovanie_turning.ui -o ui_widget_normirovanie_turning.py
%UIC_PATH% -g python ui_widget_normirovanie_turning_button.ui -o ui_widget_normirovanie_turning_button.py
%UIC_PATH% -g python ui_widget_normirovanie_turning_kanavka.ui -o ui_widget_normirovanie_turning_kanavka.py
%UIC_PATH% -g python ui_widget_normirovanie_turning_podrezka.ui -o ui_widget_normirovanie_turning_podrezka.py
%UIC_PATH% -g python ui_widget_predlogs.ui -o ui_widget_predlogs.py
%UIC_PATH% -g python ui_widget_row.ui -o ui_widget_row.py
%UIC_PATH% -g python ui_page_shlifovanie.ui -o ui_page_shlifovanie.py
%UIC_PATH% -g python ui_page_shlifovanie_start.ui -o ui_page_shlifovanie_start.py
%UIC_PATH% -g python ui_page_shlifovanie_osnovnoe.ui -o ui_page_shlifovanie_osnovnoe.py
%UIC_PATH% -g python ui_page_otreznaya.ui -o ui_page_otreznaya.py


echo.
echo [2/2] Конвертация ресурсов QRC...
echo ----------------------------------------

%RCC_PATH% -g python res/res.qrc -o res_rc.py

echo.
echo ========================================
echo Готово! Все файлы сконвертированы.
echo ========================================
pause