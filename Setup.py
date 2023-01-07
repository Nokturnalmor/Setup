from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWinExtras import QtWin
import Cust_Qt as CQT
CQT.conver_ui_v_py()
from Setup_gui import Ui_MainWindow
import Cust_Functions as F
import os
import sys
import platform


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.PUT_PO_UMOLCH = F.put_po_umolch() + F.sep() + 'MES' + F.sep()
        self.inic()
        if F.nalich_file(self.PUT_PO_UMOLCH) == False:
            F.sozd_dir(self.PUT_PO_UMOLCH)
        self.ui.le_putust.setText(self.PUT_PO_UMOLCH)

        self.ui.rbtn_reload.clicked.connect(self.click_reload)
        self.ui.rbtn_ust.clicked.connect(self.click_setup)
        self.ui.btn_tool.clicked.connect(self.vibor_papki)
        #=======================================
        self.ui.btn_ok.clicked.connect(self.btn_ok)
        #self.ui.rbtn_reload.setEnabled(False)
        print(platform.win32_ver())

    def inic(self):
        tbl = self.ui.tbl_spis_prog
        CQT.clear_tbl(tbl)
        file_list_prog = F.scfg('dir_list_prog') + F.sep() + 'list.txt'
        if F.nalich_file(file_list_prog) == False:
            CQT.msgbox('Не найден список')
            sys.exit(app.exec())
        # ========================Таблица
        spis_prog = F.otkr_f(file_list_prog, utf8=True, separ='|')
        spis_prog.insert(0, ['Имя', "Путь", "Исп.", "Статус", ''])
        for i in range(1, len(spis_prog)):
            spis_prog[i].append('')
            spis_prog[i].append('')
        CQT.zapoln_wtabl(self, spis_prog, tbl, separ='', isp_shapka=True)
        nk_ima = CQT.nom_kol_po_imen(tbl, 'Имя')
        nk_put = CQT.nom_kol_po_imen(tbl, 'Путь')
        nk_isp_f = CQT.nom_kol_po_imen(tbl, 'Исп.')
        nk_stat = CQT.nom_kol_po_imen(tbl, 'Статус')
        nk_zap = CQT.nom_kol_po_imen(tbl, '')
        tbl.setColumnHidden(nk_put, True)
        tbl.setColumnHidden(nk_isp_f, True)
        for i in range(tbl.rowCount()):
            CQT.add_check_box(tbl, i, nk_stat)
            CQT.add_btn(tbl, i, nk_zap, 'Запуск', self.check_ustanovky(tbl.item(i, nk_ima).text()), self.zapusk_prog)
        # =======================================

    def check_ustanovky(self, ima):
        if F.nalich_file(self.PUT_PO_UMOLCH + 'cache.txt'):
            spis_cache = F.otkr_f(self.PUT_PO_UMOLCH + 'cache.txt', True, '|')
            put = ''
            for i in range(len(spis_cache)):
                if spis_cache[i][0] == ima:
                    put = spis_cache[i][1]
                    break
            if put == '':
                return False
            if F.nalich_file(put + F.sep() + 'embed' + F.sep() + 'window_free.vbs'):
                return True
        return False


    def zapusk_prog(self,row,col):
        spis= CQT.spisok_iz_wtabl(self.ui.tbl_spis_prog,'',True)
        nk_ima = F.nom_kol_po_im_v_shap(spis,'Имя')
        if F.nalich_file(self.PUT_PO_UMOLCH + 'cache.txt'):
            spis_cache = F.otkr_f(self.PUT_PO_UMOLCH + 'cache.txt', True, '|')
            put = ''
            for i in range(len(spis_cache)):
                if spis_cache[i][0] == spis[row+1][nk_ima]:
                    put = spis_cache[i][1]
                    break
            if put == '':
                CQT.msgbox('Не найдена папка')
                return
            if F.nalich_file(put + F.sep() + 'embed' + F.sep() + 'window_free.vbs'):
                F.zapyst_file(put + F.sep() + spis[row+1][nk_ima] + '.lnk')
                sys.exit()
            else:
                CQT.msgbox('Не найден файл запуска')



    def click_reload(self):
        self.ui.le_putust.setText('')
        self.ui.le_putust.setEnabled(False)


    def click_setup(self):
        self.ui.le_putust.setText(self.PUT_PO_UMOLCH)
        self.ui.le_putust.setEnabled(True)


    def vibor_papki(self):
        rez = CQT.getDirectory(self,self.ui.le_putust.text())
        if rez == '.' or rez == None:
            return
        self.ui.le_putust.setText(rez)

    def btn_ok(self):
        rez = self.check_put()
        if rez != True:
            CQT.msgbox(rez)
            return
        rez = self.check_spis()
        if rez != True:
            CQT.msgbox(rez)
            return
        rez = self.check_reszhim()
        if rez != True:
            CQT.msgbox(rez)
            return
        spisok_putey = self.spisok_putey()

        os.system(r'net use z: \\powerz.ru\share')
        for i in range(len(spisok_putey)):
            put_ishod_dir = spisok_putey[i][0]
            if platform.win32_ver()[0] == '7':
                spis_ishod_dir = put_ishod_dir.split(F.sep())
                spis_ishod_dir.insert(-1,'win7')
                put_ishod_dir = F.sep().join(spis_ishod_dir)
            ima_new_papki = F.clear_pod_ima_faila(F.transliteration(spisok_putey[i][1]))
            if self.ui.rbtn_ust.isChecked() == True:
                put_new_embed = self.ui.le_putust.text() + ima_new_papki + F.sep() + 'embed'
                put_new =self.ui.le_putust.text() + ima_new_papki
            else:
                path = self.cache_load(spisok_putey[i][1])
                if path == None:
                    CQT.msgbox('Не обнаружен каталог')
                    return
                put_new = path
                put_new_embed = put_new + F.sep() + 'embed'
            if self.ui.rbtn_ust.isChecked() == True:
                if F.nalich_file(put_new):
                    try:
                        F.udal_papky(put_new)
                    except:
                        CQT.msgbox('Папка с программой занята, необходимо закрыть все используемые файлы '
                                   'или перезагрузить компьютер')
                        return
            else:
                if F.nalich_file(put_new_embed + F.sep() + 'mydesign.py'):
                    F.udal_file(put_new_embed + F.sep() + 'mydesign.py')
            if F.nalich_file(put_ishod_dir) == False:
                CQT.msgbox('Не найден исходный каталог.')
                return
            if self.ui.rbtn_ust.isChecked() == True:
                F.copytree(put_ishod_dir,put_new)
                CQT.statusbar_text(self, f'Установка {spisok_putey[i][1]}...')
                spis_files = F.spis_files(put_new)
            else:
                CQT.statusbar_text(self, f'Обновление {spisok_putey[i][1]}...')
                F.copytree(put_ishod_dir, path)
                spis_files = F.spis_files(path)

            for block in spis_files:
                for file in  block[2]:
                    if F.ostavit_rasshir(file) == '.ui':
                        F.udal_file(block[0] + F.sep() + file)

            spis_run = [['@echo off'],[f'python {spisok_putey[i][2]}']]
            F.zap_f(put_new_embed  + F.sep() + 'run.bat', spis_run, separ='|', utf8=True)

            # ==========================================FREE===============
            file_zapysk = put_new_embed  + F.sep() + 'window_free.vbs'

            F.udal_file(file_zapysk)
            spis = ['Set WshShell = CreateObject("WScript.Shell")',
                    rf'WshShell.Run chr(34) & "{put_new_embed}\run.bat" & Chr(34), 0',
                    'Set WshShell = Nothing']
            F.zap_f(file_zapysk,spis,separ='',utf8=True)

            put_ico = put_new_embed + F.sep() + r'icons\1.ico'
            ico = ''
            if F.nalich_file(put_ico):
                ico = put_ico
            F.sozd_yarlik(file_zapysk, put_new, spisok_putey[i][1], ico)

            #=========================================================

            file_zapysk = put_new_embed + F.sep() + 'window.vbs'

            F.udal_file(file_zapysk)
            spis = ['Set WshShell = CreateObject("WScript.Shell")',
                    rf'WshShell.Run chr(34) & "{put_new_embed}\run.bat" & Chr(34)']
            F.zap_f(file_zapysk, spis, separ='', utf8=True)

            put_ico = put_new_embed + F.sep() + r'icons\1.ico'
            ico = ''
            if F.nalich_file(put_ico):
                ico = put_ico
            F.sozd_yarlik(file_zapysk, put_new ,spisok_putey[i][1]+'_win',ico)
#====================================================
            self.cache_add(spisok_putey[i][1],put_new)#обновить список установленных мес программ
            if self.ui.rbtn_ust.isChecked() == True:
                CQT.msgbox(f'{spisok_putey[i][1]} успешно установлено')
                CQT.statusbar_text(self, f'')
                self.inic()
            else:
                CQT.msgbox(f'{spisok_putey[i][1]} успешно обновлено')
                CQT.statusbar_text(self, f'')
            F.otkr_papky(put_new)

    def cache_load(self,ima):
        if F.nalich_file(self.PUT_PO_UMOLCH + 'cache.txt'):
            spis_cache = F.otkr_f(self.PUT_PO_UMOLCH + 'cache.txt', True, '|')
            for i in range(len(spis_cache)):
                if spis_cache[i][0] == ima:
                    return spis_cache[i][1]


    def cache_add(self,ima,path):
        if F.nalich_file(self.PUT_PO_UMOLCH + 'cache.txt'):
            spis_cache = F.otkr_f(self.PUT_PO_UMOLCH + 'cache.txt', True, '|')
        else:
            spis_cache = []
        put_old = ''
        for i in range(len(spis_cache)):
            if spis_cache[i][0] == ima:
                put_old = spis_cache[i][1]
                spis_cache[i][1] = path
                break
        if put_old == '':
            spis_cache.append([ima,path])
        F.zap_f(self.PUT_PO_UMOLCH + 'cache.txt', spis_cache, '|', utf8=True)

    def check_put(self):
        if F.check_for_russian(self.ui.le_putust.text()) == True:
            return f'Не допустима киррилица в пути к папке'
        if F.nalich_file(self.ui.le_putust.text()) == False:
            return f'Путь установки не существует'
        return True

    def spisok_putey(self):
        tbl = self.ui.tbl_spis_prog
        spis_putey = []
        nk_stat = CQT.nom_kol_po_imen(tbl, 'Статус')
        nk_put = CQT.nom_kol_po_imen(tbl, 'Путь')
        nk_ima = CQT.nom_kol_po_imen(tbl, 'Имя')
        nk_isp_f = CQT.nom_kol_po_imen(tbl, 'Исп.')
        for i in range(tbl.rowCount()):
            if tbl.cellWidget(i, nk_stat).checkState():
                spis_putey.append([tbl.item(i, nk_put).text(),tbl.item(i, nk_ima).text(),tbl.item(i, nk_isp_f).text()])
        return spis_putey

    def check_spis(self):
        if self.spisok_putey() == []:
            return 'Не выбраны программы'
        return True

    def check_reszhim(self):
        if self.ui.rbtn_ust.isChecked() == False and self.ui.rbtn_reload.isChecked() == False:
            return 'Не выбран режим'
        return True

app = QtWidgets.QApplication(sys.argv)

args = sys.argv[1:]

myappid = 'Powerz.BAG.SustControlWork.0.0.0'  # !!!
QtWin.setCurrentProcessExplicitAppUserModelID(myappid)
app.setWindowIcon(QtGui.QIcon(os.path.join("icons", "icon.png")))
print(QtWidgets.QStyleFactory.keys())
S = F.scfg('Stile').split(",")
if len(S) > 1:
    app.setStyle(S[1])

application = mywindow()
application.show()


sys.exit(app.exec())

# pyinstaller.exe --onefile --icon=1.ico --noconsole Setup.py