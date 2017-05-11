# -*- coding: utf-8 -*-

import os
import csv

code = ""
name = ""
user_type_id_dash_id = ""
reconcile = ""
chart_template_id = "br_account_chart_template_lexisnexis"
xml_record = ""
record_id_counter = 0
record_id_string = ""
target_file_start = """<odoo>
    <data noupdate="1">
"""
target_file_end = """
    </data>
</odoo>
"""

with open('account.account.csv', 'r') as f:
    reader = csv.reader(f,delimiter=';', quoting=csv.QUOTE_NONE)
    target = open('account_account_template_final.xml', 'w')
    target.write(target_file_start)
    for row in reader:
        if record_id_counter == 0:
            record_id_counter += 1
            continue
        
        code = row[1]
        name = row[2]
        user_type_id_dash_id = row[3]
        reconcile = row[4]
        record_id_string = "account_account_" + str(record_id_counter)

        xml_record = """ 
    <record id=\"%s\" model=\"account.account\">
        <field name=\"code\">%s</field>
        <field name=\"name\">%s</field>
        <field name=\"user_type_id\" search=\"[(\'name\',\'=\',\'%s\')]\" />
        <field name=\"reconcile\">%s</field>
        <field name=\"chart_template_id\" ref=\"%s\"/>
    </record> 
    """ % (record_id_string,code,name,user_type_id_dash_id,reconcile,chart_template_id)
        
        target.write(xml_record)
        record_id_counter += 1
        if record_id_counter > 971:
            break
target.write(target_file_end)
f.close()
target.close()
